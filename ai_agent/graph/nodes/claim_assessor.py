import json
from graph.config.openai_client import client,get_model
from graph.workflow import ClaimState


def claim_assessment(state: ClaimState) -> ClaimState:
    claim = state.get("parsed_claim", {})
    damage = state.get("damage_report", {})
    policy = state.get("policy", {})
    model_name = get_model()

    messages = [
        {
            "role": "system",
            "content": "You are a senior marine insurance claim assessor. Review all available information and make a final claim decision."
        },
        {
            "role": "user",
            "content": f"""
            Based on the following data, determine claim validity and payout:
            Claim Details: {json.dumps(claim)}
            Damage Report: {json.dumps(damage)}
            Policy Details: {json.dumps(policy)}

            Return a JSON object with these fields:
            {{
              "validity": "Approved" | "Rejected" | "Review",
              "reason": "Brief explanation",
              "approved_amount": number,
              "confidence": float (0.0–1.0)
            }}
            """
        }
    ]

    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    try:
        assessment = json.loads(response.choices[0].message.content)
    except Exception:
        assessment = {"raw_output": response.choices[0].message.content}

    state["claim_decision"] = assessment
    return state