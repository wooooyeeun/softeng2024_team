function calculate() {
    let a = document.getElementById("inputA").value;
    let b = document.getElementById("inputB").value;
    let select = document.getElementById("operator").value;
    let result
    if (select === "+") {
        result = Number(a) + Number(b);
    }
    else if (select === "-") {
        result = Number(a) - Number(b);
    }
    else if (select === "*") {
            result = Number(a) * Number(b);
    }
    else if (select === "/") {
        if (b === 0) {
            result = "<h1><strong>0으로 나눌 수 없습니다.</strong></h1>"
        } else {
            result = Number(a) / Number(b);
        }
    }
    else {
        result = "<h1><strong>잘못된 연산자입니다.</strong></h1>"
    }
    document.getElementById("calculate_result").innerHTML = result;}

