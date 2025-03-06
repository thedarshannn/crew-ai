from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class RequirementsGathererInput(BaseModel):
    """Input schema for RequirementsGathererTool."""
    question: str = Field(..., description="Question to ask regarding requirements.")
    context: str = Field(..., description="Context of previous information collected.")

class RequirementsGathererTool(BaseTool):
    name: str = "Requirements Gatherer"
    description: str = (
        "Tool to prompt the user for specific requirements information. "
        "Use this when you need to collect detailed information about project requirements."
    )
    args_schema: Type[BaseModel] = RequirementsGathererInput

    def _run(self, question: str, context: str) -> str:
        print(f"\n===== REQUIREMENTS QUESTION =====")
        print(f"Context: {context}")
        print(f"Question: {question}")
        print("=================================\n")
        
        user_input = input("Your response: ")
        return user_input


class SRSFormatterInput(BaseModel):
    """Input schema for SRSFormatterTool."""
    content: str = Field(..., description="Content to format according to SRS standards.")
    section: str = Field(..., description="SRS section being formatted.")

class SRSFormatterTool(BaseTool):
    name: str = "SRS Formatter"
    description: str = (
        "Tool to format content according to standard SRS document structure and conventions. "
        "Use this to ensure consistency across the document."
    )
    args_schema: Type[BaseModel] = SRSFormatterInput

    def _run(self, content: str, section: str) -> str:
        # Format the content according to SRS standards for the given section
        formatted_content = f"## {section}\n\n{content}"
        
        # Add standard elements based on the section
        if section == "Functional Requirements":
            formatted_content += "\n\n### Priority Levels\n- High\n- Medium\n- Low"
        elif section == "Non-Functional Requirements":
            formatted_content += "\n\n### Categories\n- Performance\n- Security\n- Reliability\n- Usability"
            
        return formatted_content
