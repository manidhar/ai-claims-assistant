import os
import sys
from fastapi import FastAPI, Form, UploadFile
import tempfile
import shutil

# 🧭 --- Fix for import errors ---
# Add current directory to Python path so `graph` is recognized
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 🧩 --- LangGraph and workflow imports ---
from graph.workflow import build_graph

# Initialize FastAPI app
app = FastAPI(title="AI Claims Assistant for Boats")

# Build LangGraph
graph = build_graph()
compiled_graph = graph.compile()


@app.post("/assess")
async def assess_claim(claim_text: str = Form(...), images: list[UploadFile] = []):
    """
    Main endpoint for claim assessment.
    - Accepts claim text and damage images.
    - Passes them through the LangGraph pipeline (parser → vision → policy → assessor).
    """

    # Store uploaded images temporarily
    tmp_files = []
    for file in images:
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        shutil.copyfileobj(file.file, temp)
        tmp_files.append(temp.name)

    # Input to LangGraph pipeline
    state = {"claim_text": claim_text, "images": tmp_files}

    # Run the compiled graph
    try:
        result = compiled_graph.invoke(state)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "success", "result": result}


@app.get("/")
def home():
    """
    Basic health check endpoint.
    """
    return {
        "message": "🚤 AI Claims Assistant is running!",
        "endpoints": ["/assess (POST)"],
        "model": "gemini-1.5-flash (via OpenAI interface)",
    }


if __name__ == "__main__":
    import uvicorn

    # Run Uvicorn with proper import path context
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )