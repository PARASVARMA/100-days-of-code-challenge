$people = array(
   'online'=>array('David', 'Amy'),
   'offline'=>array('John', 'Rob', 'Jack'),
   'away'=>array('Arthur', 'Daniel')
);
echo $people['online'][0]; //Outputs "David"

echo $people['away'][1]; //Outputs "Daniel"
