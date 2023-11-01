
function swapBlocksPos(elem1, elem2){
    return new Promise((resolve) => {
        let temp = elem1.style.transform;
        elem1.style.transform = elem2.style.transform
        elem2.style.transform = temp;

        window.requestAnimationFrame(function() {
            setTimeout(() => {
                elem1.parentNode.insertBefore(elem2, elem1);
                resolve()
            }, 1e3)
        })
    })
}