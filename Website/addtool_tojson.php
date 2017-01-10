<?php

	$name = $_POST['name'];
	$email = $_POST['email'];
	$codeurl = $_POST['codeurl'];
	$description = $_POST['description'];

	$currentStatusFile = "currentstatus.json";
	$currentStatusData = json_decode(file_get_contents($currentStatusFile), true);

	$newTool = [];
	$newTool['name'] = $name;
	$newTool['email'] = $email;
	$newTool['url'] = $codeurl;
	$newTool['description'] = $description;
	
	$newTool['version'] = "N/A";
	$newTool['command'] = "N/A";
	$newTool['main'] = "N/A";
	$newTool['timeout'] = 60;
	$newTool['successed'] = false;
	$newTool['lastRun'] = "N/A";
	$newTool['active'] = true;
	
	$authentication = uniqid();
	$newTool['authentication'] = $authentication;
	
	$currentStatusData[] = $newTool;
	file_put_contents($currentStatusFile,json_encode($currentStatusData, JSON_PRETTY_PRINT));
	
	
?>
<html>
<body>

          <p>
            <h3>Tool added to PubRunner</h3>
            Here is the JSON that should be added to the tools.json file in your copy of PubRunner
			
			
          </p>
		  
		  <p>
		  
		  <?php 
				echo "<pre>";
				
				echo json_encode($newTool, JSON_PRETTY_PRINT);
				
				echo "</pre>";
			?>
		  
		  </p>

</body>
</html>