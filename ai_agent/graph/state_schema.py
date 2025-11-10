from typing import TypedDict, List, Dict, Any

class ClaimState(TypedDict, total=False):
    claim_text: str
    images: List[str]
    parsed_claim: Dict[str, Any]
    damage_report: Dict[str, Any]
    policy: Dict[str, Any]
    claim_decision: Dict[str, Any]