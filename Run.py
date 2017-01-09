import json
from Runner import *

with open('tools.json') as toolsJSON:
    toolList = json.load(toolsJSON)

for tool in toolList:
    if tool["active"] == True:
        runner = Runner(tool["name"], tool["command"], tool["main"])
        runner.run()
