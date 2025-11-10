import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ✅ Gemini API endpoint (OpenAI-compatible)
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("GEMINI_API_KEY")
print("Base url ",BASE_URL)
print("API_KEY ",API_KEY)

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def get_model(preferred: str = "gemini-1.5-pro", fallback: str = "gemini-2.5-flash") -> str:
    """
    Returns the best available Gemini model.
    Tries 'preferred' first; falls back to 'fallback' if unavailable.
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
            raise ValueError("❌ No Gemini models found. Check API key or endpoint.")
    except Exception as e:
        print(f"⚠️ Model listing failed: {e}. Defaulting to fallback.")
        return fallback