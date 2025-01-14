from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_texts():
    data = request.json
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')

    # Простое сравнение текстов
    similarity = "Тексты одинаковые" if text1 == text2 else "Тексты разные"

    return jsonify({"result": similarity})

if __name__ == '__main__':
    app.run(debug=True)
