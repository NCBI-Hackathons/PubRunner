<?php

	$name = strip_tags ($_POST['name']);
	$email = strip_tags ($_POST['email']);
	$codeurl = strip_tags ($_POST['codeurl']);
	$description = strip_tags ($_POST['description']);

	$currentStatusFile = "currentstatus.json";
	$currentStatusData = json_decode(file_get_contents($currentStatusFile), true);

	$newTool = [];
	$newTool['name'] = $name;
	$newTool['email'] = $email;
	$newTool['codeurl'] = $codeurl;
	$newTool['dataurl'] = "";
	$newTool['description'] = $description;
	
	$newTool['version'] = "N/A";
	$newTool['command'] = "N/A";
	$newTool['main'] = "N/A";
	$newTool['timeout'] = 60;
	$newTool['success'] = false;
	$newTool['lastRun'] = "N/A";
	$newTool['active'] = true;
	
	$authentication = uniqid();
	$newTool['authentication'] = $authentication;
	
	$currentStatusData[] = $newTool;
	file_put_contents($currentStatusFile,json_encode($currentStatusData, JSON_PRETTY_PRINT));
	
	
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="/asset/img/favicon.ico">

    <title>PubRunner - Added Tool</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/custom.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation"><a href="index.html">Home</a></li>
            <li role="presentation"><a href="results.html">Results</a></li>
            <li role="presentation" class="active"><a href="addtool.html">Add Tool</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">
          <img src="assets/img/pubrunner.png" width="200"/>
        </h3>
      </div>

      <div class="jumbotron">
        <h1>Yay, tool added</h1>
        <p class="lead">Below is a little bit of JSON. If you follow the tutorial for getting your own PubRunner instance working, you'll see that you need to put this JSON into your tools.json file.</p>
      </div>

	  <div>
		
		  <?php 
				echo "<pre>";
				
				echo json_encode($newTool, JSON_PRETTY_PRINT);
				
				echo "</pre>";
			?>
	  </div>

      <footer class="footer">
        <p>&copy; 2017 PubRunner and friends.</p>
      </footer>

    </div> <!-- /container -->


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>
	
    <script src="assets/js/jquery-1.7.2.min.js"></script>
    <script src="assets/js/bootstrap.js"></script>
    <script src="assets/js/jquery.metadata.js"></script>
    <script src="assets/js/jquery.tablesorter.min.js"></script>
    <script src="assets/js/jquery.tablecloth.js"></script>
	<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.1/angular.min.js"></script>
	
  </body>
</html>
