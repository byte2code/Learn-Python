async function* BubbleSort(){
    let blocks = document.querySelectorAll(".block-container");

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
        yield blocks[blocks.length - i - 1].childNodes[1].style.backgroundColor = "purple";
    }
}

async function* InsertionSort() {
    let blocks = Array.from(document.querySelectorAll(".block-container"));
    // let a = Array.from(blocks).map((block, idx) => block.childNodes[0].innerText);
    // console.log(blocks);
    
    let j, key;
    for (let i = 1; i < blocks.length; i++) {
        j = i - 1;

        key = parseInt(blocks[i].childNodes[0].innerHTML)

        blocks[i].childNodes[1].style.backgroundColor = "green";
        blocks[j].childNodes[1].style.backgroundColor = "green";

        await new Promise((resolve) => {
            setTimeout(() => resolve(), 5e2)
        })

        while(j >= 0 && parseInt(blocks[j].childNodes[0].innerHTML) > key){
            blocks[j].childNodes[1].style.backgroundColor = "green";
            blocks[j+1].childNodes[1].style.backgroundColor = "purple";
            await swapBlocksPos(blocks[j+1], blocks[j]);
            blocks[j].childNodes[1].style.backgroundColor = "blue";
            [blocks[j+1], blocks[j]] = [blocks[j], blocks[j+1]]
            j--;
        }
        yield   blocks[j+1].childNodes[1].style.backgroundColor = "blue";
        // if(j >= 0) blocks[j].childNodes[1].style.backgroundColor = "blue";
    }
}