//On change Event in Javascript:-
<input type="text" id="name" onchange="change()">
<script>
function change() {
 var x = document.getElementById("name");
 x.value= x.value.toUpperCase();
}
</script>
