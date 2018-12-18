//Byteme -- Robin Han & Kenny Li
//Softdev pd8
//K28 -- Sequential Progression
//2018-12-18

var fibonacci = function(n){
    if (n < 2){
	return n;
    }
    else{
	return fibonacci(n-1) + fibonacci(n-2);
    };
};

var gcd = function(a,b){
    if(b == 0) {
        return a;
    }
    else {
        return gcd(b, a % b);
    };
};

var students = ["a", "b", "c", "d", "e"]

var randomStudent = function(){
    return students[Math.floor(Math.random() * students.length)];
};
