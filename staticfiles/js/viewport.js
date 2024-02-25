let totalHeight = document.body.scrollHeight;

let footerPositioning = function() {

    let windowHeight = window.innerHeight;

    if (totalHeight > windowHeight) {
        document.querySelector('footer').style='position: relative; bottom: 0;';
    } else {
        document.querySelector('footer').style = 'position: absolute; bottom: 0;';
    }

}

footerPositioning();

window.addEventListener('resize', footerPositioning);