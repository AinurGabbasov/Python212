class Business{
    constructor(img, h2){
        this.src = img,
        this.h2 = h2
    }
    render(id){
        let out = `
            <img src="${this.src}">
            <h2>${this.h2}</h2>
        `;
        document.querySelector(`#${id}`).innerHTML = out;
    }
}

let img1 = "https://cdn3.iconfinder.com/data/icons/friends-holding-banner/238/people-holding-banner-003-64.png";
let img2 = "https://cdn0.iconfinder.com/data/icons/advertisement-marketing-strategy/280/marketing-012-64.png";
let img3 = "https://cdn2.iconfinder.com/data/icons/indoor-display-advertising-marketing-services/321/indoor-display-advertisement-3-64.png";
let img4 = "https://cdn2.iconfinder.com/data/icons/indoor-display-advertising-marketing-services/380/indoor-display-advertisement-8-64.png";
let img5 = "https://cdn2.iconfinder.com/data/icons/indoor-display-advertising-marketing-services/499/indoor-display-advertisement-12-64.png";
let img6 = "https://cdn2.iconfinder.com/data/icons/indoor-display-advertising-marketing-services/391/indoor-display-advertisement-2-64.png";
let img7 = "https://cdn2.iconfinder.com/data/icons/outdoor-display-advertisement/457/-outdoor-display-advertisement-3-64.png";
let img8 = "https://cdn2.iconfinder.com/data/icons/outdoor-display-advertisement/582/-outdoor-display-advertisement-4-64.png";
let img9 = "https://cdn2.iconfinder.com/data/icons/indoor-display-advertising-marketing-services/580/indoor-display-advertisement-1-64.png";

let header = new Business(img1, "Наши сотрудники на всех улицах города");
header.render("poster1");
let header2 = new Business(img2, "Работаем на большинстве стен домов");
header2.render("poster2");
let header3 = new Business(img3, "На презентациях крупных проектов");
header3.render("poster3");
let header4 = new Business(img4, "В топовых офисах города");
header4.render("poster4");
let header5 = new Business(img5, "На лифтах бизнес центров");
header5.render("poster5");
let header6 = new Business(img6, "На торговых автоматах");
header6.render("poster6");
let header7 = new Business(img7, "На досках для объявлений");
header7.render("poster7");
let header8 = new Business(img8, "На общественных остановках");
header8.render("poster8");
let header9 = new Business(img9, "На витринах магазин и торговых центров");
header9.render("poster9");