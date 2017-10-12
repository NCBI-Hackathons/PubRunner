<?php

$currentStatusFile = "restricted/currentstatus.json";
$currentStatusData = json_decode(file_get_contents($currentStatusFile), true);

foreach ($currentStatusData as $key => $record)
{
	unset($record['authentication']);
}

header('Content-Type: application/json');
echo json_encode($currentStatusData);

?>