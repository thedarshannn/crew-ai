#!/usr/bin/env python
import sys
import os

# Add the src directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from ai_srs.main import run

if __name__ == "__main__":
    run()
