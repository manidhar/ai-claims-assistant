import re
import requests
from graph.state_schema import ClaimState
from graph.utils.logging_utils import log_node

@log_node("policy")
def policy_verifier(state: ClaimState) -> ClaimState:
    claim_text = state.get("claim_text", "")
    policy_id = None

    match = re.search(r"POL\d+", claim_text)
    if match:
        policy_id = match.group(0)

    if not policy_id:
        state["policy"] = {"error": "No policy ID found in claim text"}
        return state

    try:
        resp = requests.get(f"http://localhost:8080/api/policy/{policy_id}", timeout=3)
        state["policy"] = resp.json()
    except Exception as e:
        state["policy"] = {"error": str(e)}
    
    return state
