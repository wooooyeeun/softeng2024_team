from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    html_str = """
    <!DOCTYPE html>
    <html lang = "kr">
    <head>
    <meta charset="UTF-8">
    <title>계산기</title>
    </head>
    <body>
    <form method="GET" action="/calculate">
        <h2>계산기</h2>
        <label>첫 번째 숫자:
            <input type="text" name="num1">
        </label><br><br>
        <label>연산자:
            <select name="operator">
                <option value="+">덧셈(+)</option>
                <option value="-">뺄셈(-)</option>
                <option value="*">곱셉(*)</option>
                <option value="/">나눗셈(/)</option>
            </select>
        </label><br><br>
        <label>두 번째 숫자:
            <input type="text" name="num2">
        </label><br><br>
        <button type="submit">계산</button>
    </form>
    </body>
    </html>
    """
    return html_str

@app.route("/calculate/")
def calculate():
    num1 = request.args.get("num1", "0")
    num2 = request.args.get("num2", "0")
    operator = request.args.get("operator", "+")

    try:
        num1 = int(num1)
        num2 = int(num2)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num2 - num1
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "0으로 나눌 수 없습니다."
        else:
            return "잘못된 연산자입니다."

        return f"결과: {num1} {operator} {num2} = {result}"

    except ValueError:
        return "숫자를 입력해주세요."

app.run(debug=True)