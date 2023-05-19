let namee = prompt('Введите ваше имя');
let lastname = prompt('Введите вашу фамилию');
let city = prompt('Введите ваш город проживания');
let age = +prompt('Введите ваш возраст');
let res = confirm("Ваше имя: " + namee + "\nВаша фамилия: " + lastname + "\nВаш город проживания: " + city + "\nВаш возраст: " + age + "\n\nВсе верно?");
if (res){
    alert("Благодарим вас за предоставленную информацию!");
}