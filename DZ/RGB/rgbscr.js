let mas = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

for(let i=0; i < mas.length; i++){

    document.write("<div class='foot' align='center'>" + mas[i] + "</div>");

    let rf = document.getElementsByClassName("foot")[i];
    rf.style.fontWeight = "bold";

    let n = document.querySelectorAll("div");

    n[i].style.width = "100%";
    n[i].style.height = "20px";
    n[0].style.marginTop = "100px";
    let createColor = () => {
        let r = Math.floor(Math.random() * 256);
        let g = Math.floor(Math.random() * 256);
        let b = Math.floor(Math.random() * 256);
        n[i].style.background = "rgb(" + r + "," + g + "," + b + ")";
    }
    createColor();
}