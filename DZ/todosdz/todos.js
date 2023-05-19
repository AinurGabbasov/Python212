document.querySelector("#load").addEventListener("click", load);

function load(){
    let url = "https://jsonplaceholder.typicode.com/todos";
    fetch(url)
        .then(function (response){
            return response.json();
        })
        .then(function(data){
            let ul = document.querySelector("#list");
            let html = data.map(function(item){
                if(item.completed === true){
                    return "<li>" + "Номер работника " + item.userId + " Номер задачи " + item.id  + "  " +  item.title + "</li>";
                }
            })
            ul.insertAdjacentHTML("afterbegin", html.join(" "));
        })
}