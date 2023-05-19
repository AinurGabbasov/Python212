let who = function(){
    return 'Я ' + this.name + ' мне ' + this.age + ' лет. Я работаю ' + this.job + 'ом' + "<br>";
}

let person = new Object();
person.name = "Дмитрий";
person.age = 26;
person.job = "Дизайнер";
person.who = who

let person1 = new Object();
person1.name = "Станислав";
person1.age = 29;
person1.job = "Программист";
person1.who = who

let person2 = new Object();
person2.name = "Сергей";
person2.age = 35;
person2.job = "Менеджер";
person2.who = who


document.write(person.who());
document.write(person1.who());
document.write(person2.who());