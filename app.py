from flask import Flask, request, render_template
from text_comparator import compare_texts

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        file1 = request.files["file1"]
        file2 = request.files["file2"]

        file1.save("file1.txt")
        file2.save("file2.txt")

        result = compare_texts("file1.txt", "file2.txt")
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)