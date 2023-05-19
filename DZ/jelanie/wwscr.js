let a = document.querySelector("#cl");
a.addEventListener('click', myMove);

function myMove(){
    a.style.display = 'none';
    let elem = document.getElementById("animate");

    let pos = 0
    let id = setInterval(frame, 10);

    function frame(){
        if(pos == 473){
            a.style.display = 'block';
            clearInterval(id);
        }
        else{
            pos++;
            elem.style.top = pos + 'px';
            elem.style.left = pos + 'px'; 
        }
    }
}