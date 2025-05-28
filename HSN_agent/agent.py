import pandas as pd
from google.adk.agents import Agent
from chromaclient.chromaclient import Chroma
from typing import Union, List

# Load the dataset
csv = pd.read_csv("D:/projects/Google_adk_try/data/HSN_SAC.xlsx - HSN_MSTR.csv")
client = Chroma()

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
    if len(codes)==0:
        return {
            "status":"error",
            "error_message":"Please enter some code no code received"
        }
    for code in codes:
        if not validate_code(code):
            results.append({
                "code": code,
                "status": "error",
                "error_message": f"The HSN code '{code}' is invalid"
            })
            continue

        res = client.getDatasOnIndex(code)
        if res['documents'] and len(res['documents']) > 0:
            description = res['documents'][0]
            results.append({
                "code": code,
                "status": "success",
                "description": description
            })
        else:
            results.append({
                "code": code,
                "status": "error",
                "error_message": f"The HSN code '{code}' is not found in the Chroma collection."
            })

    return {"status": "multi_result", "report": results}
    


def get_description_hsn(description: str) -> dict:
    """Retrieves relevant HSN codes from description."""
    suggestion = client.getDatas(description=description)
    return {
        "status": "success",
        "data": suggestion
    }

root_agent = Agent(
    name="hsn_validation_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent that validates Harmonized System Nomenclature (HSN) codes and provides product descriptions "
        "based on a master dataset. It can confirm whether an HSN code is valid(can be length of 2,4,6,8) and return the associated description. "
        "It can also search for HSN codes based on a description."
    ),
    instruction=(
        "You are an HSN validation agent. When a user provides an HSN code, use the tool to check if it's valid. "
        "Return the product description if found. If the user provides a description, search for relevant HSN codes. "
        "You are allowed to have a conversation with the user."
    ),
    tools=[get_hsn_description, get_description_hsn],
)
