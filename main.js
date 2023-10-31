const displayArea = document.getElementById("display-area");
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

function swapBlocksPos(elem1, elem2){
    return new Promise((resolve) => {
        let temp = elem1.style.transform;
        elem1.style.transform = elem2.style.transform
        elem2.style.transform = temp;

        window.requestAnimationFrame(function() {
            setTimeout(() => {
                displayArea.insertBefore(elem2, elem1);
                resolve()
            }, 500)
        })
    })
}

async function BubbleSort(){
    let blocks = document.querySelectorAll(".block-container")

    for(let i = 0; i < blocks.length - 1; i++){
        for(let j = 0; j < blocks.length - i - 1; j++){
            blocks[j].childNodes[1].style.backgroundColor = "green";
            blocks[j+1].childNodes[1].style.backgroundColor = "green";

            await new Promise((resolve) => {
                setTimeout(() => resolve(), 3e2);
            })

            let firstVal = Number(blocks[j].childNodes[0].innerHTML);
            let secondVal = Number(blocks[j+1].childNodes[0].innerHTML);

            if(firstVal > secondVal){
                await swapBlocksPos(blocks[j], blocks[j+1]);
                blocks = document.querySelectorAll(".block-container")
            }
            blocks[j].childNodes[1].style.backgroundColor = "blue"
            blocks[j+1].childNodes[1].style.backgroundColor = "blue"
        }
        blocks[blocks.length - i - 1].childNodes[1].style.backgroundColor = "purple";
    }
}

window.addEventListener("DOMContentLoaded", displayBlocks(generateRandomArray(Number(randomInput.value))));