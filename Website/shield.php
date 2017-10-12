<?php

if (!isset($_GET['name']))
	exit();

$name = $_GET['name'];

$currentStatusFile = "restricted/currentstatus.json";
$currentStatusData = json_decode(file_get_contents($currentStatusFile), true);

foreach ($currentStatusData as $record)
{
	if ($record['name'] == $name)
	{
		$lastRun = $record['lastRun'];
		$success = $record['success'];
		
		if ($success && $lastRun != 'N/A')
		{
		
			$olddate = DateTime::createFromFormat('m-d-Y', $lastRun);    // for example, see manual for formats
			$today = new DateTime();

			$diff = $today->diff($olddate);
			$days = $diff->days;
			if ($days < 32)
				$color = "brightgreen";
			else
				$color = "orange";
			
			if ($days == 1)
				$plural = "";
			else
				$plural = "s";
			
			
			$shieldURL = "https://img.shields.io/badge/PubRunner-$days day$plural ago-$color.svg";
		}
		else
		{
			$shieldURL = "https://img.shields.io/badge/PubRunner-Run Failed-red.svg";
			
		}
		
		header("Location: $shieldURL");
		break;
	}
}

?>