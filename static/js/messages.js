const djangoMessages = document.getElementsByClassName('alert-success');

setTimeout(function(){
    for (let i = 0; i < djangoMessages.length; i++) {
        djangoMessages[i].setAttribute('style', 'display: none !important;');
    }
}, 5000);



