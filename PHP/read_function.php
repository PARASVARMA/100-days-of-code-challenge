Reading a file with a read() function:-
$read = file('names.txt');
foreach ($read as $line) {
  echo $line .", ";
}
