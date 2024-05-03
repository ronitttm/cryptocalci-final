var enbtn = document.getElementById("encrbtndes");  
var rawdata = document.getElementById("rawdatades");  
var password = document.getElementById("passworddes");  
var display1 = document.getElementById("displaydes");  
var endata = document.getElementById("endatades");  
var password2 = document.getElementById("password1des");  
var display2 = document.getElementById("display1des");  
var debtn = document.getElementById("debtndes")

enbtn.addEventListener("click",function(e){   
var ciphertext = CryptoJS.DES.encrypt(rawdata.value, password.value);  
endata.value =  ciphertext.toString()  
display1.textContent = endata.value
}) 

debtn.addEventListener("click",function(e){  
if(password.value != password2.value){  
alert('password must same as on encrypted');  
return false;  
}    
var Normaltext = CryptoJS.DES.decrypt(endata.value, password2.value);  
display2.textContent = Normaltext.toString(CryptoJS.enc.Utf8);  
}); 