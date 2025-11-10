import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ✅ Load your OpenAI API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Initialize OpenAI client (default base_url is correct)
client = OpenAI(api_key=OPENAI_API_KEY)


def get_model(fallback="gpt-4.1-mini", peferred="gpt-4o-mini"):
    """
    Returns the preferred OpenAI model if available,
    otherwise falls back to a lightweight alternative.
    """
    try:
        models = client.models.list()
        available = [m.id for m in models.data]

        if preferred in available:
            print(f"✅ Using {preferred}")
            return preferred
        elif fallback in available:
            print(f"⚡ Falling back to {fallback}")
            return fallback
        else:
            raise ValueError(f"❌ No compatible OpenAI model found. Available: {available}")
    except Exception as e:
        print(f"⚠️ Model listing failed: {e}")
        return fallback
