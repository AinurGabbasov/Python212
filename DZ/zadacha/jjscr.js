document.write("<div id = 'risk'></div>");
let risk = document.getElementById("risk");
risk.innerHTML = "Дюбель — конструктивный элемент, который используется для укрепления винта или предмета на стене, на потолке или на полу в помещении или под открытым небом в различных материалах (бетон, кирпич и прочее). Сам дюбель удерживается в конструкции при помощи сил трения. С некоторого времени элементы связи и укрепления, дюбели и винт (шуруп) объединяют в одно целое и используются, прежде всего, для тяжёлых нагрузок. Дюбели предлагаются в различных величинах, которые руководствуются диаметром дюбеля (и соответственно необходимым отверстием), измеренным в миллиметрах..";
risk.style.background = "#f0f";
risk.style.color = "#99ffff";
risk.style.width = "50%";
risk.style.outline = "10px dotted #000";

risk.className = "resetFont";
let rf = document.getElementsByClassName("resetFont")[0];

rf.style.fontSize = "12pt";
rf.style.fontWeigt = "bold";
rf.style.textDecoration = "line-through";