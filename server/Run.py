from Utilities import *
from Runner import *

# Load tool list
tools = loadTools()

# Now launch tools
updatedTools = []
for tool in tools:
    # Only launch those that are active
    if tool["active"] == True:
        print("yup")
        runner = Runner(tool)
        runner.run()
        updatedTools.append(runner.__dict__)
    else:
        updatedTools.append(tool)

# Update the tools.json file
updateTools(updatedTools)

# TODO: push the new JSON file to website
