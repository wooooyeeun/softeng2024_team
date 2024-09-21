from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def calculate():
    html_str = """
    <!DOCTYPE html>
    <html lang = "kr">
    <head>
        <meta charset = "UTF-8">
        <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    </head>
    <body>
        <form id = "form_id" action = "javascript:post_query()">
            <h1><strong><계산기></strong></h1>
            <label>첫 번째 숫자 :
                <input type = "text" name = "num1">
            </label><br><br>
            <label>연산자 :
                <select name = "operator">
                    <option value = "" selected>선택</option>
                    <option value = "+">덧셈(+)</option>
                    <option value = "-">뺄셈(-)</option>
                    <option value = "*">곱셈(*)</option>
                    <option value = "/">나눗셈(/)</option>
                </select>
            </label><br><br>
            <label>두 번째 숫자 :
                <input type = "text" name = "num2">
            </label><br><br>
            <button type = "submit"><h3>계산</h3></button><br><br>
        </form>
    <div id="results"></div>
    <script>
    function post_query() {
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:5000/calculate/",
            data: $("#form_id").serialize(),
            success: update_result,
            dataType: "html"
        });
    }
    function update_result(data) {
        $("#results").html(data);
    }
    </script>
    </body>
    </html>
    """
    return html_str


@app.route("/calculate/")
def calculate_arg_html():
    num1 = request.args.get("num1","0")
    num2 = request.args.get("num2","0")
    operator = request.args.get("operator", "+")

    try:
        num1 = int(num1)
        num2 = int(num2)
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "<h1><strong>0으로 나눌 수 없습니다.</strong></h1>"
            else:
                result = num1 / num2
        else:
            return "<h1><strong>잘못된 연산자입니다.</strong></h1>"
        return f"<h1>{num1} {operator} {num2} = <strong>{result}</strong></h1>"

    except ValueError:
        return "<h1><strong>숫자를 입력하세요.</strong></h1>"


app.run(debug=True)

