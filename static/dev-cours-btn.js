var li = document.querySelectorAll('#chapter li');
const menuBtn = document.querySelector('.menu-btn');
var Btn3 = document.querySelector('#btn3');
var Quizz1 = document.querySelector('#quizz1')
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


Btn3.addEventListener('click', function() {
    alert('Bientot nous serons en mesure de vous donner votre certificat si vous le voulez');

});




