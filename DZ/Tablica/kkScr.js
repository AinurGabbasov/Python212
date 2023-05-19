document.write("<table border='1' bgcolor='silver' width='400' height='400' align='center'>");
for(let i=0; i<11; i++){
    document.write("<tr align='center'>");
    for(let j=0; j<11; j++){
        if(i == 0 || j == 0){
            document.write("<td bgcolor='white'>" + (i + j) + "</td>");
        }
        else if(i % 2 == j % 2){
            document.write("<td bgcolor='purple'>" + i*j + "</td>");
        }
        else{
            document.write("<td bgcolor='green'>" + i*j + "</td>");
        }
    }
    document.write("</tr>");
}
document.write("</table>");