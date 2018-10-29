//Reading a file with Array:-
$read = file('names.txt');
$count = count($read);
$i = 1;
foreach ($read as $line) {
  echo $line;
  if($i < $count) {
    echo ', ';
  }
  $i++;
}
