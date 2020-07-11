/*
const one = document.getElementById("one"),
      two = document.getElementById("two"),
      three = document.getElementById("three"),
      view = document.getElementById("view"),
      greeting = document.getElementById("greeting"),
      chapter1 = document.getElementById("chapter1"),
      chapter2 = document.getElementById("chapter2");
      chapter3 = document.getElementById("chapter3");
      welcome = document.getElementById("welcome");

one.addEventListener("click", () => {
        greeting.classList.add("hidden");
        chapter1.classList.remove("hidden");
    }
);

two.addEventListener("click", () => {
    greeting.classList.add("hidden");
    chapter1.classList.remove("hidden");
    chapter2.classList.add("hidden");
   }
);

welcome.addEventListener("click", () => {
        greeting.classList.remove("hidden");
        chapter1.classList.add("hidden");
    }
);

three.addEventListener("click", () => {
    chapter2.classList.remove("hidden");
    chapter3.classList.add("hidden");
});  */
var li = document.querySelectorAll('#chapter li');
//var welcome = getElementById('welcome');
for(var i of li){
  i.addEventListener('click', function(elem){
    var content = document.getElementById(elem.target.classList[0]).innerHTML;
    document.getElementById('result').innerHTML = content;
  });
}

/*
welcome.addEventListener('click', function() => {
 
}

  ); */ 