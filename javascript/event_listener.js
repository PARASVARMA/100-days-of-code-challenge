//Event Listener example in Javascript:-
<button id="demo">Start</button>

<script>
var btn = document.getElementById("demo");
btn.addEventListener("click", myFunction);

function myFunction() {
  alert(Math.random());
  btn.removeEventListener("click", myFunction);
}
</script>
