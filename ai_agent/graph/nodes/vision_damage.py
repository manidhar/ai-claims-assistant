import base64
import json
from graph.config.openai_client import client, get_model
from graph.state_schema import ClaimState
from graph.utils.logging_utils import log_node


def encode_image_to_base64(image_path: str) -> str:
    """Reads an image file and returns its base64 data URI."""
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{img_b64}"


@log_node("vision")
def vision_damage_assessment(state: ClaimState) -> ClaimState:
    """
    Performs visual damage analysis using OpenAI multimodal model (e.g., GPT-4o).
    Handles multiple image uploads by encoding them in base64.
    """
    claim_text = state.get("claim_text", "")
    images = state.get("images", [])
    model_name = get_model(preferred="gpt-4o-mini", fallback="gpt-4o")

    if not images:
        state["damage_report"] = {"error": "No images provided."}
        return state

    # Convert each image path to Base64 data URI
    image_data = []
    for img in images:
        try:
            img_b64 = encode_image_to_base64(img)
            image_data.append({"type": "image_url", "image_url": {"url": img_b64}})
        except Exception as e:
            image_data.append({"type": "text", "text": f"⚠️ Error reading image: {e}"})

    # Build multimodal prompt
    messages = [
        {
            "role": "system",
            "content": "You are a marine insurance visual damage assessor. Analyze boat damage from photos and claim description."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"Claim details: {claim_text}"},
                *image_data
            ]
        }
    ]

    # Send request to OpenAI multimodal endpoint
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )

    try:
        damage_report = json.loads(response.choices[0].message.content)
    except Exception:
        # Fallback if response isn’t structured JSON
        damage_report = {"raw_output": response.choices[0].message.content}

    state["damage_report"] = damage_report
    return state