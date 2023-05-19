//ПЕРВЫЙ ВАРИАНТ(этот лучше)
let button = document.querySelectorAll(".remove-button");
    
for (let i = 0; i < button.length; i++) {
    button[i].addEventListener('click',function () {      
        button[i].parentNode.remove();
    } , false);
}

//ВТОРОЙ ВАРИАНТ(этот понятнее)

// let div = document.querySelectorAll(".pane");

// let button = document.querySelectorAll(".remove-button");
    
// for (let i = 0; i < button.length; i++) {
//    button[i].addEventListener('click',function (rmParent) {      
//        div[i].remove();
//    } , false);
// }

