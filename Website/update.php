<?php

try {

	if (!isset($_FILES['jsonFile']['error']) || is_array($_FILES['jsonFile']['error'])) {
		throw new RuntimeException('Invalid parameters.');
	}

	// Check $_FILES['jsonFile']['error'] value.
	switch ($_FILES['jsonFile']['error']) {
		case UPLOAD_ERR_OK:
			break;
		case UPLOAD_ERR_NO_FILE:
			throw new RuntimeException('No file sent.');
		case UPLOAD_ERR_INI_SIZE:
		case UPLOAD_ERR_FORM_SIZE:
			throw new RuntimeException('Exceeded filesize limit.');
		default:
			throw new RuntimeException('Unknown errors.');
	}

	// You should also check filesize here.
	if ($_FILES['jsonFile']['size'] > 1000000) {
		throw new RuntimeException('Exceeded filesize limit.');
	}

	$tmpName = $_FILES['jsonFile']['tmp_name'];

	$newStatusData = json_decode(file_get_contents($tmpName), true);
	
	$corruptedMessage = 'File is not a valid JSON file. Possibly corrupted?';
	
	if ($newStatusData === null)
	{
		throw new RuntimeException($corruptedMessage);
	}
	
	// TODO: This should double check that the JSON file has all the expected fields
	
	$currentStatusFile = "currentstatus.json";
	$currentStatusData = json_decode(file_get_contents($currentStatusFile), true);
	
	echo "<pre>";
	print_r($currentStatusData);
	echo "</pre>";
	
	$authentications = [];
	
	foreach ($currentStatusData as $key => $record)
	{
		$authentication = $record['authentication'];
		$authentications[$authentication] = $key;
	}
	
	
	foreach ($newStatusData as $record)
	{
		$authentication = $record['authentication'];
		
		if (in_array($authentication, $authentications))
		{		
			$key = $authentications[$authentication];
			$currentStatusData[$key]['success'] = $record['success'];
			$currentStatusData[$key]['lastRun'] = $record['lastRun'];
		}
	}
	echo "<pre>";
	print_r($currentStatusData);
	echo "</pre>";
	
	file_put_contents($currentStatusFile,json_encode($currentStatusData, JSON_PRETTY_PRINT));
	
}
catch (RuntimeException $e) {
	//echo $e->getMessage();
	
	$message = $e->getMessage();
	//header("Location: error.php?message=".urlencode($message));
	print "<b>ERROR:</b> $message";
	die();
}

$message="Done";
print "<b>SUCCESS:</b> $message";
die();

?>
