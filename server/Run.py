from Utilities import *
from Runner import *
import json
import requests

# Load tool list
tools = loadTools()

# Now launch tools
updatedTools = []
for tool in tools:
    # Only launch those that are active
    if tool["active"] == True:
        print("Running %s" % tool["name"])
        runner = Runner(tool)
        runner.run()

        if runner.success:
            print("Run was successful")
            if USE_FTP:
                print("Pushing results to FTP")
                runner.pushToFTP()
            else:
                print("Pushing results to local directory")
                runner.pushToLocalDirectory()
        else:
            print("Run failed")

        updatedTools.append(runner.__dict__)
    else:
        updatedTools.append(tool)

# Update the tools.json file
updateTools(updatedTools)

# Push the new JSON file to website
print("Sending update to http://www.pubrunner.org")
with open('tools.json') as f:
	r = requests.post('http://www.pubrunner.org/update.php', files={'jsonFile': f})
	#print(r.text)

