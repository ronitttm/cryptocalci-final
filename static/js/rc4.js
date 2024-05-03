var enbtn = document.getElementById("encrbtnrc4");  
var rawdata = document.getElementById("rawdatarc4");  
var password = document.getElementById("passwordrc4");  
var display1 = document.getElementById("displayrc4");  
var endata = document.getElementById("endatarc4");  
var password2 = document.getElementById("password1rc4");  
var display2 = document.getElementById("display1rc4");  
var debtn = document.getElementById("debtnrc4")

enbtn.addEventListener("click",function(e){   
var ciphertext = CryptoJS.RC4.encrypt(rawdata.value, password.value);  
endata.value =  ciphertext.toString()  
display1.textContent = endata.value
}) 

debtn.addEventListener("click",function(e){  
if(password.value != password2.value){  
alert('password must same as on encrypted');  
return false;  
}    
var Normaltext = CryptoJS.RC4.decrypt(endata.value, password2.value);  
display2.textContent = Normaltext.toString(CryptoJS.enc.Utf8);  
}); 
