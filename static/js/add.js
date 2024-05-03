// General variables
var key = 5;
var range = 26;
var aCode = 65;
var zCode = aCode + range;

// Get HTML elements as variables
var input = document.getElementById("in");
var encrypt = document.getElementById("encrypt");
var decrypt = document.getElementById("decrypt");
var output = document.getElementById("out");
var outputLine = document.getElementById("out_line");

// Function to perform encryption
function encipher(event) {
  event.preventDefault(); // Prevent default form submission behavior

  var message = input.value.toUpperCase();
  output.innerHTML = ""; // Clear main output
  outputLine.innerHTML = ""; // Clear step-by-step output

  // Loop through each character in the message
  for (var i = 0; i < message.length; i++) {
    var letter = message.charCodeAt(i);
    var newLetter = letter;
    var step = "";

    if (letter >= aCode && letter <= zCode) {
      newLetter += key;

      if (newLetter > zCode) {
        newLetter -= range;
      }

      step = `${message[i]} (${letter}) => ${String.fromCharCode(newLetter)} (${newLetter})`;
    } else {
      step = `${message[i]} (Not encrypted)`;
    }

    // Append each step to the output line
    outputLine.innerHTML += `<p>${step}</p>`;

    // Get the character corresponding to the new ASCII code and add it to the main output
    newLetter = String.fromCharCode(newLetter);
    output.innerHTML += newLetter;
  }
}

// Bind the encipher function to the "Encrypt" button click
encrypt.addEventListener("click", encipher);

// Function to perform decryption
decrypt.onclick = function () {
  var message = input.value.toUpperCase();
  output.innerHTML = ""; // Clear main output
  outputLine.innerHTML = ""; // Clear step-by-step output

  // Loop through each character in the message
  for (var i = 0; i < message.length; i++) {
    var letter = message.charCodeAt(i);
    var newLetter = letter;
    var step = "";

    if (letter >= aCode && letter <= zCode) {
      newLetter -= key;

      if (newLetter < aCode) {
        newLetter += range;
      }

      step = `${message[i]} (${letter}) => ${String.fromCharCode(newLetter)} (${newLetter})`;
    } else {
      step = `${message[i]} (Not decrypted)`;
    }

    // Append each step to the output line
    outputLine.innerHTML += `<p>${step}</p>`;

    // Get the character corresponding to the new ASCII code and add it to the main output
    newLetter = String.fromCharCode(newLetter);
    output.innerHTML += newLetter;
  }
};
