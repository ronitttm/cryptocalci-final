var enbtn = document.getElementById("encrbtnaes");  
var rawdata = document.getElementById("rawdataaes");  
var password = document.getElementById("passwordaes");  
var display1 = document.getElementById("displayaes");  
var endata = document.getElementById("endataaes");  
var password2 = document.getElementById("password1aes");  
var display2 = document.getElementById("display1aes");  
var debtn = document.getElementById("debtnaes")

enbtn.addEventListener("click",function(e){   
var ciphertext = CryptoJS.AES.encrypt(rawdata.value, password.value);  
endata.value =  ciphertext.toString();  
display1.textContent = ciphertext.toString();  
}) 

debtn.addEventListener("click",function(e){  
if(password.value != password2.value){  
alert('password must same as on encrypted');  
return false;  
}    
var Normaltext = CryptoJS.AES.decrypt(endata.value, password2.value);  
display2.textContent = Normaltext.toString(CryptoJS.enc.Utf8);  
});  
