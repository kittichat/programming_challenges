<?php

$limit = 4000000;
$arr = array(1,2);
$sum = 0;
$x = 1;
while($sum < $limit){
  $sum = $arr[$x] + $arr[$x-1];
  array_push($arr,$sum);
  $x++;
}
$total = 0;
foreach($arr as $value){
  if($value % 2 ==0){
    $total += $value;
  }
}
echo $total;

?>