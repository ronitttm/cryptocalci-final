var a = prompt("Please Enter first number:")
var b = prompt("please enter second number: ")

function modcalc(num1 , num2 ){

    var mod = num1 % num2 ;
    return mod;


}
console.log("The mod of" , a , "and" , b, "is:")
console.log(modcalc(a,b))