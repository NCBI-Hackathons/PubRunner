<html>

<body>

<p>Little upload test to push a JSON file.</p>

<form enctype="multipart/form-data" method="post" action="update.php">
   <input id="fileupload" name="jsonFile" type="file" />
   <input type="hidden" name="MAX_FILE_SIZE" value="100000" /> 
   <input type="submit" value="submit" id="submit" />
</form>

</body>

</html>