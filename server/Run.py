import json
from Runner import *

# Load list of available tools
with open('tools.json') as toolsJSON:
    toolList = json.load(toolsJSON)

updatedList = []
for tool in toolList:
    # Only launch those that are active
    if tool["active"] == True:
        runner = Runner(tool["name"], tool["command"], tool["main"], tool["timeout"], tool["successed"], tool["lastRun"], tool["active"])
        runner.run()
        updatedList.append(runner.__dict__)
    else:
        updatedList.append(tool)

with open("tools.json", "w") as f:
    json.dump(updatedList, f, indent = 4)
