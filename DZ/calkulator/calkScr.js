"use strict"

let solution = confirm("Желаете произвести вычисления?");

if (solution){
    let operator = prompt('Выберите действие: +, -, *, /, %, **, !, #(кв корень)\n\n"Факториал и Корень квадратный вычисляется для Первого введенного числа!"');

    let num1 = +prompt("Введите первое число: ");
    
    let num2 = +prompt("Введите второе число(степень возведения): ");

    if (operator == "+"){
        alert("Сумма: " + (num1 + num2));
    }
    else if (operator == "-"){
        alert("Разность: " + (num1 - num2));
    }
    else if (operator == "*"){
        alert("Произведение: " + num1 * num2);
    }
    else if (operator == "/"){
        alert("Частное: " + num1 / num2);
    }
    else if (operator == "%"){
        alert("Остаток от деления: " + num1 % num2);
    }
    else if (operator == "**"){
        alert("Число " + num1 + " в " + num2 + " степени: " + num1 ** num2);    
    }
    else if (operator == "#"){
        alert("Квадратный корень из "+ num1 + " равен: " + num1 ** 0.5);
    }
    else if (operator == "!"){
        let y = 1;
        for (i = 1; i <= num1; i += 1) {
            y *= i;
            }
        alert("Факториал " + num1 + " равен: " + y);
    }
    else{
        alert("Выберите оператор и предложенных вариантов!");
    }
}    
else{
    alert("Всего доброго, приходите еще!");
}