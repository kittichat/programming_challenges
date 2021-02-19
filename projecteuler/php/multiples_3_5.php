<?php

$y = 1000;
$x = 1;
$z = array(0);
while ($x < $y){

  if ( $x % 3 == 0 || $x % 5 == 0){
    array_push($z , $x );
  }

  $x++;
}
$value = 0;
foreach($z as $value1){
  $value += $value1;
}

echo $value;


?>