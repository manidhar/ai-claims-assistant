import re, json
from graph.utils.logging_utils import log_node
from graph.state_schema import ClaimState
from graph.config.openai_client import client,get_model


@log_node("parser")
def document_parser(state: ClaimState) -> ClaimState:
    claim_text = state.get("claim_text", "")
    model_name = get_model()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Extract structured insurance claim data."},
            {"role": "user", "content": claim_text}
        ]
    )

    raw_output = response.choices[0].message.content

    # ✅ Clean JSON inside Markdown block
    json_match = re.search(r"```json\s*(.*?)\s*```", raw_output, re.DOTALL)
    if json_match:
        try:
            parsed = json.loads(json_match.group(1))
        except Exception:
            parsed = {"raw_output": raw_output}
    else:
        parsed = {"raw_output": raw_output}

    state["parsed_claim"] = parsed
    return state