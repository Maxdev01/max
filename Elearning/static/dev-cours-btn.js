var li = document.querySelectorAll('#chapter li');
const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if(!menuOpen) {
        menuBtn.classList.add('open');
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        menuOpen = false;
    }
});

for(var i of li){
    i.addEventListener('click', function(elem){
        var content = document.getElementById(elem.target.classList[0]).innerHTML;
        document.getElementById('result').innerHTML = content;
    });
}

