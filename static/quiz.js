
const options=document.querySelector(".options").children;
const answerTrackerContainer=document.querySelector(".answers-tracker");
const questionNumberSpan=document.querySelector(".question-num-value");
const totalQuestionSpan=document.querySelector(".total-question");
const correctAnswerSpan=document.querySelector(".correct-answers");
const totalQuestionSpan2=document.querySelector(".total-question2");
const percentage=document.querySelector(".percentage");
const question=document.querySelector(".question")
const op1 = document.querySelector(".option1");
const op2 = document.querySelector(".option2");
const op3 = document.querySelector(".option3");
const op4 = document.querySelector(".option4");
let questionIndex;
let index=0;
let myArray=[];
let myArr=[];
let score=0;

// questions and options and answers

const questions=[

{
q: "Le conflit se definit comme l’affrontement de deux ou plusieurs volontes individuelles ou collectives qui manifestent les unes a l’egard des autres une intention hostile :",
options: ["Par ce qu’il est", "Par ce qu’il fait", "Par ce qu’il devient", "Toutes les reponses sont bonnes"],
answer:3
},


{
q: "Le conflit est un antagonisme,opposition de motivation ou de conceptions contradictoires chez une meme personne ou au sein d’un groupe….selon quelle conception ? ",
options: ["Conception psychologique", "Conception psychanalytique", "conception sociologique", "Toutes les reponses sont bonnes"],
answer:0
},

{
q: "Le conflit a plusieurs acceptions :une premiere qui vient du latin 'configure' qui en francais signifie",
options: ["Choc", "Lutte", "Heurter", "aucune de ces reponses"],
answer:3
},


{
q: "Type de conflit interpersonnel le plus frequent et le plus facile a resoudre. C’est une divergence d’interpretation entre ds personnes",
options: ["Conflit d’objectif", "Conflit de concurrence", "Le malentendu", "Conflit affectif"],
answer:2
},



{
q: "Ce genre de conflit est tres remarquable au sein des organisations. C’est un conflit qui met en opposition des generations differentes",
options: ["Conflit organisationnel", "Conflit intergroupe", "Conflit horizontal", "Conflit de generation"],
answer:3
},

{
q: "Conflit d’acceptation, conflit d’evitement des choses, conflit entre acceptation et evitement sont du type de conflit",
options: ["intragroupe", "intrapersonnel", "interpersonnel", "intergroupe"],
answer:1
}

]

// set questions and options and question number 
// sa pati sa ki responsab poul fe kesyon ak tt chwa yo afiche nan paj html lan

totalQuestionSpan.innerHTML=questions.length;
function load(){
	questionNumberSpan.innerHTML=index+1;
	question.innerHTML=questions[questionIndex].q;
	op1.innerHTML=questions[questionIndex].options[0];
	op2.innerHTML=questions[questionIndex].options[1];
	op3.innerHTML=questions[questionIndex].options[2];
	op4.innerHTML=questions[questionIndex].options[3];
	index++;

}

//fonction sa se pou lhrw klike sou chwa wap fe an
 // menm fonktyon sa ap  pemet ou konnen lhr chwa a bon ou pa
// menm fonktyon sa pemet ou we l tou 


function check(element){
	if(element.id==questions[questionIndex].answer){
		element.classList.add("correct");
		updateAnswerTracker("correct")
		score++;
		console.log("score:"+score)
	}
	else{
		element.classList.add("wrong");
		updateAnswerTracker("wrong")
	} 
	disabledOptions()
}

// sa se yon fonktyon kap pemet ou chwazi youn
function disabledOptions(){
	for(let i=0; i<options.length; i++){
		options[i].classList.add("disabled");
		if(options[i].id==questions[questionIndex].answer){
			options[i].classList.add("correct");
		}
	}
}

//function sa c pou lhr cliquer pou li pa baw menm nan
function enableOptions(){
	for(let i=0; i<options.length; i++) {
		options[i].classList.remove("disabled","correct","wrong");
	}
}



//function sa ap gen yon kondisyon ladan pou diw pa chwazi youn
function validate(){
	if(!options[0].classList.contains("disabled")){
		alert("SVP vous devez choisir une option")
	}
	else{
		enableOptions();
		randomQuestion();
	} 
}

// function ap pemet ou valide
function next(){
	validate();
}


// kounya nou pral fe yon function kap pemet kesyon yo vinn aleatwa
 function randomQuestion(){
 	let randomNumber=Math.floor(Math.random()*questions.length);
 	let hitDuplicate=0;
 	if(index==questions.length){
 		console.log("quiz over")
 		quizOver();
 	}
 	else{
 		// premier
 		if(myArray.length>0){
 			for(let i=0; i<myArray.length; i++){
 				if(myArray[i]==randomNumber){
 					hitDuplicate=1;
 					break;
 				}
 			}
 			if(hitDuplicate==1){
 				randomQuestion();
 			}
 			else{
 				questionIndex=randomNumber;
 				load();
 				myArr.push(questionIndex);
 			}
 			

 		}
 		//deuxieme
 		if(myArray.length==0){
 			questionIndex=randomNumber;
 			load();
 			myArr.push(questionIndex);
 		}

 	
 	    myArray.push(randomNumber);

 	//test dans la console
 	// console.log("myArray:"+myArray)
 	//console.log(questionIndex)
 	
 	 }
 }

 // fonktyon sa pral pemet u konnen lhr li bon ou pa men nan sans konkre
//menm fonktyon sa ap pemet ou kreye yon div 
function answerTracker(){
	for(let i=0; i<questions.length; i++){
		const div=document.createElement("div")
		answerTrackerContainer.appendChild(div);
	}
}

// fonktyon sa ap pemet ou wel 
function updateAnswerTracker(classNam){
	answerTrackerContainer.children[index-1].classList.add(classNam);
}
//function ap pemet ou afiche resulta final moun lan apre quizz lan 
function quizOver(){
	document.querySelector(".quiz-over").classList.add("show");
	correctAnswerSpan.innerHTML=score;
	totalQuestionSpan2.innerHTML=questions.length;
	percentage.innerHTML=(score/questions.length)*100 + "%";

}
// function sa c pouw ka rejwe anko siw vle 
function tryAgain(){
	window.location.reload();
}

window.onload=function(){
	randomQuestion();
	answerTracker();
}
