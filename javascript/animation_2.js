#Creating Animation by set Interval in Javascript:-
// starting position
var pos = 0; 
//our box element
var box = document.getElementById("box");

function move() {
  pos += 1;
  box.style.left = pos+"px"; //px = pixels
}
