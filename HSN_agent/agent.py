import pandas as pd
from google.adk.agents import Agent
from chromaclient import Chroma
from typing import Union, List


client = Chroma()

print(client.getDatas("describe"))
def validate_code(code: str) -> bool:
    valid_length = [2, 4, 6, 8]
    return len(code) in valid_length
def get_hsn_description(codes: List[str]) -> dict:
    """
    Retrieves the description(s) based on a list of HSN codes.

    Args:
        codes (List[str]): A list of HSN codes.

    Returns:
        dict: Dictionary with status and results or error message.
    """
    results = []
    if len(codes) == 0:
        return {
            "status": "error",
            "error_message": "Please enter some code no code received",
        }
    for i in codes:
        if (not validate_code(i)):
            results.append({f"i":"invalid length not in 2,4,6,8 length"})
            codes.remove(i)

    res = client.getDatasOnIndex(code=codes)
    if res:

        results.append(
            {"code": codes, "status": "success", "description": res})
    else:
        results.append(
            {
                "code": codes,
                "status": "error",
                "error_message": f"The HSN code '{codes}' is not found in the Chroma collection.",
            }
        )
    return {
        "result":results
    }


def get_description_hsn(description: str) -> dict:
    """Retrieves relevant HSN codes from description."""
    suggestion = client.getDatas(description=description)
    return {"status": "success", "data": suggestion}


root_agent = Agent(
    name="hsn_validation_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that validates Harmonized System Nomenclature (HSN) codes and provides product descriptions "
        "based on a master dataset. It checks whether an HSN code is valid (i.e., has a length of 2, 4, 6, or 8 digits) "
        "and returns the associated description if found. It can also retrieve possible HSN codes based on a product description."
    ),

    instruction=(
        "You are an HSN validation agent. When a user provides an HSN code, first validate the code to ensure "
        "it has a valid length (2, 4, 6, or 8 digits). If it's valid, use the tool to retrieve its product description. "
        "If the code is invalid, inform the user. When a user provides a product description instead, search and return relevant HSN codes. "
        "You are allowed to have a conversation with the user."
    ),
    tools=[get_hsn_description, get_description_hsn],
)
