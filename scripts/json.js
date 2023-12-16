const section1 = document.querySelector('.conference-hall-top');
const section2 = document.querySelector('.type-halls');

const requestURL = 'https://anastasiiayakymiv.github.io/json/conferencehall.json'

const request = new XMLHttpRequest();
request.open('GET', requestURL);

request.responseType = 'json';
request.send();

request.onload = function() {
    const conferencehall = request.response
    populateSection1(conferencehall)
    populateSection2(conferencehall)
    console.log(conferencehall)
}

function populateSection1(jsonData) {
    let Section = document.querySelector('.conference-hall-top .content-wrap .hall-wrap');

    let sectiontitle = document.createElement('h2');
    sectiontitle.classList.add('conferencehall-title');
    sectiontitle.textContent = jsonData["title"];
    Section.appendChild(sectiontitle)

    let halldescription = document.createElement('div');
    halldescription.classList.add('hall-description');
    halldescription.textContent = jsonData["description"];
    Section.appendChild(halldescription);

    let hallimg = document.createElement('img');
    hallimg.classList.add('section1-img');
    hallimg.src = jsonData["img1"];
    Section.appendChild(hallimg);
}

function populateSection2(jsonData) {
    let Section2 = document.querySelector('.type-halls .content-wrap .type-hall-wrap');
    let SectionWrap = document.querySelector('.type-halls .content-wrap .type-hall-wrap .imghall-wrap')
    let SectionWrap2 = document.querySelector('.type-halls .content-wrap .type-hall-wrap .imghall-wrap2')

    let shorttext1 = document.createElement('div');
    shorttext1.classList.add('short-text-hall');
    shorttext1.textContent = jsonData["shorttext1"];
    Section2.appendChild(shorttext1);

    let arthallimg1 = document.createElement('img');
    arthallimg1.classList.add('art-hall-img1')
    arthallimg1.src = jsonData["img2"];
    SectionWrap.appendChild(arthallimg1);
    let arthallimg2 = document.createElement('img');
    arthallimg2.classList.add('art-hall-img2')
    arthallimg2.src = jsonData["img3"];
    SectionWrap.appendChild(arthallimg2);

    let artdescription = document.createElement('div')
    artdescription.classList.add('arthall-description');
    artdescription.textContent = jsonData["arthall-description"];
    Section2.appendChild(artdescription);

    let shorttext2 = document.createElement('div');
    shorttext2.classList.add('short-text-hall2');
    shorttext2.textContent = jsonData["shorttext2"];
    Section2.appendChild(shorttext2);

    let congressimg1 = document.createElement('img');
    congressimg1.classList.add('congress-img1')
    congressimg1.src = jsonData["img4"];
    SectionWrap2.appendChild(congressimg1);
    let congressimg2 = document.createElement('img');
    congressimg2.classList.add('congress-img2')
    congressimg2.src = jsonData["img5"];
    SectionWrap2.appendChild(congressimg2);

    let congressdescription = document.createElement('div')
    congressdescription.classList.add('congresshall-description');
    congressdescription.textContent = jsonData["congresshall-description"];
    Section2.appendChild(congressdescription);

}