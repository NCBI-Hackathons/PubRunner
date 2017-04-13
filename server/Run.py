from Utilities import *
from Runner import *

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
            if USE_FTP:
                print("Pushing results to FTP")
                runner.pushToFTP()
            else:
                print("Pushing results to local directory")
                runner.pushToLocalDirectory()

        updatedTools.append(runner.__dict__)
    else:
        updatedTools.append(tool)

# Update the tools.json file
updateTools(updatedTools)

# TODO: push the new JSON file to website
