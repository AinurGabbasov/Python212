let otgadka = document.querySelector("input[type='button']");

otgadka.addEventListener('click', otgad);

function otgad(){
    let f = document.forma;

    for(let i=0; i<f.otv.length; i++){
        if(f.otv[i].checked){
            let m = f.otv[i].value
            confirm("Это " + m + "\n\nУгадали?" + "\n\nВыберите следующую загадку!");
        }
    }
}