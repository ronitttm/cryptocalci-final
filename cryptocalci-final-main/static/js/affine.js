
var alphabetUPP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var alphabetLOW = "abcdefghijklmnopqrstuvwxyz";

function encode(text,a,b) {
var alphabetSEL= "";
var buffer = "";

for (var i=0; i<text.length; i++) { 
let capter = text.charCodeAt(i);

				if (capter < 97){ 
        alphabetSEL = alphabetUPP;
        }
        else if (capter > 96){ 
        alphabetSEL = alphabetLOW;
        }

				n = alphabetSEL.indexOf( text.charAt(i) ) ;
				if ( n > -1 ) { buffer += alphabetSEL.charAt( (a*n + Number(b) ) % 26 ) }
        else { buffer += text.charAt(i) }
    }
    alphabetSEL = "";
return (buffer);
}


function decode(text,a,b) {
var alphabetSEL= "";
var buffer = "";

for (var i=0; i<text.length; i++) { 
let capter = text.charCodeAt(i);

				if (capter < 97){ 
        alphabetSEL = alphabetUPP;
        }
        else if (capter > 96){ 
        alphabetSEL = alphabetLOW;
        }

				n = alphabetSEL.indexOf( text.charAt(i) ) ;
				if ( n > -1 ) { 
        temp = n - Number(b);
        while ( (temp % a) != 0 ) { temp += 26;}
        buffer += alphabetSEL.charAt( (temp /a ) % 26 );
        }
        
        else { 
        buffer += text.charAt(i) 
        }
    }
    alphabetSEL = "";
return (buffer);
}