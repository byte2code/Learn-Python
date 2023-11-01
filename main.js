
const displayArea = document.getElementById("display-area");
const displayData = document.getElementById("display-data");
const randomInput = document.getElementById("input_random");

const maxValue = 200;
const minValue = 20;

function generateRandomArray(length, min = 0, max = 0){
    let arr = [];
    for(let i = 0; i < length; i++) { 
        arr.push(Math.ceil(Math.random() * (max || maxValue)) + (minValue || min))
    }
    return arr;
}

function createElement(element){
    return document.createElement(`${element}`)
}

function generateLabel(val){
    const label = document.createElement("label");
    label.id = `label-${val}}`;
    label.classList.add("label");
    label.innerText = val;

    return label;
}

function generateRectangleBlocks(val){
    const rectangle = document.createElement("div");
    rectangle.id = `rectangle-block-${val}`;
    rectangle.classList.add("rectangle");
    rectangle.style.height = `${val}px`;
    rectangle.style.backgroundColor = "blue";
    rectangle.style.borderRadius = "2px 2px 0 0";

    return rectangle;
}

function generateBlocks(index){
    const block = document.createElement("div");
    block.id = `block-${index}`
    block.classList.add("block-container")
    block.style.transform = `translate(${index*30}px)`;

    return block;
}

function displayBlocks(array){
    displayArea.innerHTML = "";
    for(let i = 0; i < array.length; i++){
        let container = generateBlocks(i)
        container.appendChild(generateLabel(array[i]));
        container.appendChild(generateRectangleBlocks(array[i]));
        displayArea.appendChild(container);
    }
    displayArea.style.width = `${(array.length * 20) + (10 * array.length)-5}px`
    displayArea.style.marginLeft = "auto"
    displayArea.style.marginRight = "auto"
}

async function nextAction(){
    const dt = InsertionSort()
    dt.next();
}




window.addEventListener("DOMContentLoaded", displayBlocks(generateRandomArray(10)));