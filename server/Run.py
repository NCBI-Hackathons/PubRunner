from Utilities import *
from Runner import *

# Load tool list
tools = loadTools()

# Now launch every tool
updatedTools = []
for tool in tools:
    # Only launch those that are active
    if tool["active"] == True:
        runner = Runner(tool)
        runner.run()
        updatedTools.append(runner.__dict__)
    else:
        updatedTools.append(tool)

# Update the tools.json file
updateTools(updatedTools)
