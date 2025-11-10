# AI Claims Assistant

An AI-powered assistant for processing and assessing boat insurance claims using FastAPI and LangGraph.

## Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/manidhar/ai-claims-assistant.git
   cd ai-claims-assistant
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   touch .env

   # Add your environment variables to .env file:
   # OPENAI_API_KEY=your_api_key_here
   # PORT=8000 (optional, defaults to 8000)
   ```

## Running the Application

1. **Start the FastAPI server**
   ```bash
   cd ai_agent
   uvicorn app:app --reload
   ```

2. **Access the application**
   - The API will be available at: http://127.0.0.1:8000
   - API documentation (Swagger UI) will be at: http://127.0.0.1:8000/docs
   - Alternative API documentation (ReDoc): http://127.0.0.1:8000/redoc

## API Endpoints

### POST `/assess`
Submit a claim for assessment.
- Accepts claim text and optional images
- Returns assessment results

### GET `/`
Health check endpoint that returns basic API information.

## Development

- The main application code is in `ai_agent/app.py`
- LangGraph workflow is defined in `ai_agent/graph/workflow.py`
- Environment variables are loaded from `.env` file

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your chosen license here]