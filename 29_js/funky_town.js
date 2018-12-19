//KC -- Kenny & Cheryl
//Softdev pd8
//K29 -- Sequential Progression II: Electric Boogaloo
//2018-12-19

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

document.getElementById('fib').addEventListener("click", function() {
    console.log(fibonacci(10));
    document.getElementById("paragraph").innerHTML = fibonacci(10);
});

document.getElementById('gcd').addEventListener("click", function() {
    console.log(gcd(10,100));
    document.getElementById("paragraph").innerHTML = gcd(10, 100);
});

document.getElementById('randomStudent').addEventListener("click", function() {
    console.log(randomStudent());
    document.getElementById("paragraph").innerHTML = randomStudent();
});