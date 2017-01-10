from settings import *
import json
import os

def loadTools():
    """
    Loads the tools.json file

    Args:
		None
	Returns:
		An array containing the tools
    """
    with open('tools.json') as f:
        tools = json.load(f)
    return tools

def updateTools(tools):
    """
    Updates the tools.json file

    Args:
		tools (Python array): List of tool objects
	Returns:
		Nothing
    """
    with open("tools.json", "w") as f:
        json.dump(tools, f, indent = 4)

def addTool(params):
    """
    Adds a tool by creating the required folders, updating the JSON, etc.

    Args:
		params (Python dictionary): List of tool attributes as per the tools.json file
	Returns:
		Nothing

    TODO: support to move files in the newly created tool directory
    """

    # First, augment attributes
    params["successed"] = None
    params["lastRun"] = None
    params["active"] = True

    # Check if a tool with the same name exists First
    tools = loadTools()
    exists = False
    for tool in tools:
        if tool["name"] == params["name"]:
            # Cancel if it's the same version
            if tool["version"] == params["version"]:
                return
            # If it's not, update the version and reset a few parameters
            exists = True
            tool["version"] = params["version"]
            tool["successed"] = params["successed"]
            tool["lastRun"] = params["lastRun"]

    # Update the JSON file
    if not exists:
        tools.append(params)
    updateTools(tools)

    # Create the FTP folder
    ftpPath = FTP+params["name"]+"/"+params["version"]
    if not os.path.exists(ftpPath):
        os.makedirs(ftpPath)

    # Create the tool folder
    toolPath = TOOLS+params["name"]+"/"+params["version"]
    if not os.path.exists(toolPath):
        os.makedirs(toolPath)
