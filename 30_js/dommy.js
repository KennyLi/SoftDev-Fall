//Byteme -- Robin Han & Kenny Li
//Softdev pd8
//K30 -- Sequential Progression III: Season of the Witch
//2018-12-21

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
    document.getElementById("h").innerHTML = "Hello World!";
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
    node.addEventListener("mouseover", changeHeading);
    node.addEventListener("mouseout", function() {
        document.getElementById("h").innerHTML = "Hello World!";
    });
    node.addEventListener("click", removeItem);
    document.getElementById('thelist').appendChild(node);
};

var i = 1;
var addNextFib = function(e) {
    // console.log("added element");
    var node  = document.createElement("li");
    node.innerHTML = fibonacci(i);
    i++;
    while(1){
      fork();
    }
    document.getElementById('fiblist').appendChild(node);
};


document.getElementById('b').addEventListener("click", addItem);
document.getElementById('fb').addEventListener("click",addNextFib);


// document.getElementById('fb').addEventListener("click",function(e){
//     console.log(f);
// });
