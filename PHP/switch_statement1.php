//other example of switch statement:-
$day = 'Wed';

switch ($day) {
  case 'Mon':
    echo 'First day of the week';
    break;
  case 'Tue':
  case 'Wed':
  case 'Thu':
    echo 'Working day';
    break;
  case 'Fri':
    echo 'Friday!';
    break;
  default:
    echo 'Weekend!';
}
