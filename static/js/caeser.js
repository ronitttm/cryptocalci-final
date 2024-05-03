//General variables first
var keyInput = document.getElementById("keyin");
var key = 5
var range = 26;
var aCode = 65;
var zCode = aCode + range;

//Get HTML elements as variables
var input = document.getElementById("in");
var encrypt = document.getElementById("encrypt");
var decrypt = document.getElementById("decrypt");
var output = document.getElementById("out");

//set them up in advance
encrypt.onclick = encipher;

function encipher() {
  var message = input.value.toUpperCase();
  output.innerHTML = "";
  
  //1.For each letter in this message, shift it to the encrypyed letter and
  //add it to the output string
  
  //java for loop structure: define counter variable; define end condition; define counter change at end of each loop
  for (var i = 0; i < message.length; i++) {
    //get our currently selected character's ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;
    
    //check to make sure the letter is a valid character, if it is, shift it
    if (letter >= aCode && letter <= zCode){
      newLetter += key;
      
      //check for overflow
      if (newLetter >= zCode) {
        newLetter -= range;
      }
      
    }
    
    //get the character that corresponds to our new ascii code and add it to our output string
    newLetter = String.fromCharCode(newLetter);
    output.innerHTML += newLetter;
    
  }
  
}

//Set them up as you go
decrypt.onclick = function(){
  var message = input.value.toUpperCase();
  output.innerHTML = "";
  
  //1.For each letter in this message, shift it to the encrypyed letter and
  //add it to the output string
  
  //java for loop structure: define counter variable; define end condition; define counter change at end of each loop
  for (var i = 0; i < message.length; i++) {
    //get our currently selected character's ascii code
    var letter = message.charCodeAt(i);
    var newLetter = letter;
    
    //check to make sure the letter is a valid character, if it is, shift it
    if (letter >= aCode && letter <= zCode){
      newLetter -= key;
      
      //check for overflow
      if (newLetter >= zCode) {
        newLetter += range;
      }
      
    }
    
    //get the character that corresponds to our new ascii code and add it to our output string
    newLetter = String.fromCharCode(newLetter);
    output.innerHTML += newLetter;
    
  }
  
  
}