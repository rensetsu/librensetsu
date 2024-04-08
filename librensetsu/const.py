import os

from .prettyprint import PrettyPrint

GITHUB_WORKSPACE = os.getenv("GITHUB_WORKSPACE")
"""The path to the GitHub workspace"""
IS_GITHUB_WORKFLOW = os.getenv("GITHUB_ACTIONS") == "true"
"""Whether the script is running in a GitHub workflow"""
GITHUB_EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
"""The name of the GitHub event"""
IS_GITHUB_WORKFLOW_DISPATCH = GITHUB_EVENT_NAME == "workflow_dispatch"
"""Whether the script is running in a GitHub workflow dispatch event"""

pprint = PrettyPrint()
"""Instance of PrettyPrint for the proccess"""
