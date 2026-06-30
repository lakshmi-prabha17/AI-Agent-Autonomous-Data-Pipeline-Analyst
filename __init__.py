import sys
import os

# 1. Tell Python to look inside Capstone_Project for tools
sys.path.append(os.path.dirname(__file__))

# 2. Tell the ADK server to load your root_agent variable
from .agent import root_agent