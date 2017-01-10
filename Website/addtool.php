

<!DOCTYPE html>  
<html lang="en">  
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PubRunner</title>
    <link href="assets/css/bootstrap.css" rel="stylesheet">
    <link href="assets/css/bootstrap-responsive.css" rel="stylesheet">
    <link href="assets/css/tablecloth.css" rel="stylesheet">
    <link href="assets/css/prettify.css" rel="stylesheet"> 
  </head>
  
  <body>
    <div class="container">
      <div class="row">
        <div class="span12" style="padding:20px 0;">
        
          <p>
            <h3>PubRunner</h3>
            PubRunner is a wonderful software tool that does stuff.
          </p>
          
		  
		  <form method="post" action="addtool_tojson.php">
			  <div class="form-group">
				<label for="inputName">Name of tool</label>
				<input type="text" class="form-control" id="name" name="name" placeholder="Enter tool name">
			  </div>
			  <div class="form-group">
				<label for="inputEmail">Email for information and notifications</label>
				<input type="email" class="form-control" id="email" name="email" placeholder="Enter email">
			  </div>
			  <div class="form-group">
				<label for="inputEmail">URL of code</label>
				<input type="text" class="form-control" id="codeurl" name="codeurl" placeholder="Enter URL">
			  </div>
			  <div class="form-group">
				<label for="inputDescription">Description of Tool</label>
				<textarea class="form-control" id="description" name="description" rows="3"></textarea>
			  </div>
			  
			  <button type="submit" class="btn btn-primary">Submit</button>
			</form>
          
        </div>
      </div>
    </div>
  
    
  </body>

    <script src="assets/js/jquery-1.7.2.min.js"></script>
    <script src="assets/js/bootstrap.js"></script>
    <script src="assets/js/jquery.metadata.js"></script>
    <script src="assets/js/jquery.tablesorter.min.js"></script>
    <script src="assets/js/jquery.tablecloth.js"></script>
	<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.0-beta.1/angular.min.js"></script>
  
</html>