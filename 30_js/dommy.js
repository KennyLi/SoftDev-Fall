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

var changeHeading = function(e) {
    var heading = document.getElementById("h");
    heading.innerHTML = this.innerHTML
};

var removeItem = function(e) {
    this.remove()
};

var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading);
    lis[i].addEventListener("mouseout", function() {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    lis[i].addEventListener("click", removeItem);
};

var addItem = function(e) {
    // console.log("added element");
    var node  = document.createElement("li");
    node.innerHTML = "WORD";
    document.getElementById('thelist').appendChild(node);
};

document.getElementById('b').addEventListener("click", addItem);


// document.getElementById('fb').addEventListener("click",function(e){
//     console.log(f);
// });
