#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from crew import AiSrs

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def gather_initial_inputs():
    """
    Gather initial project information from the user.
    """
    print("\n===== SRS DOCUMENT GENERATOR =====")
    print("Please provide some initial information about your project:\n")
    
    project_name = input("Project Name: ")
    while not project_name.strip():
        project_name = input("Project Name (required): ")
    
    project_description = input("Brief Project Description: ")
    while not project_description.strip():
        project_description = input("Brief Project Description (required): ")
    
    return {
        'project_name': project_name,
        'project_description': project_description,
        'current_year': str(datetime.now().year)
    }

def run():
    """
    Run the SRS generation crew.
    """
    inputs = gather_initial_inputs()
    
    print("\nStarting SRS document generation process...")
    print("You will be prompted for additional information during the process.\n")
    
    try:
        result = AiSrs().crew().kickoff(inputs=inputs)
        print("\n===== SRS DOCUMENT GENERATION COMPLETE =====")
        print(f"The SRS document has been saved to 'srs_document.md'")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while generating the SRS document: {e}")


run()