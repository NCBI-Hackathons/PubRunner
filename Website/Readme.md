# Central website

This directory contains the various files used for the main PubRunner website. Its functionality is based on [Angular](https://angularjs.org/), [Bootstrap](http://getbootstrap.com/), [TableCloth](https://github.com/bwsewell/tablecloth) and a sprinkling of [PHP](http://php.net).

## Key Functionality

The main page (index.html) is a simple angular-based page that shows the currentstatus.json file in a nice table. The currentstatus.json can be updated using the update.php script (which the PubRunner tool will send data to). For easy testing, the update-test.php script makes it straightforward to send a test file to the update script. Finally the addtool.php functionality allows a new tool to be added to the list and gives the JSON data that should be added to the tools.json file in your PubRunner.

## Authentication

When a new tool is added to the PubRunner website, an authentication string is created. This authentication string is used by the website when receiving updates from the tool to confirm that it is the tool (and not some nefarious individuals).


