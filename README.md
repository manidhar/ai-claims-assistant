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

2. **Navigate to project directory, create and activate the virtual environment**
   ```bash
   # Change to project directory
   cd ai_agent

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
   # On macOS/Linux:
   touch .env

   # On Windows (using Command Prompt):
   type nul > .env

   # On Windows (using PowerShell):
   New-Item -Path ".env" -ItemType "file"

   # Add the following variables to your .env file:
   # OPENAI_API_KEY=your_api_key_here
   # PORT=8000 (optional, defaults to 8000)
   # POLICY_SERVICE_URL=http://localhost:8080 (Spring Boot service URL)
   ```

## Running the Application

### Policy Service (Spring Boot)

1. **Prerequisites**
   - Java 17 or higher
   - Maven 3.8+ or higher

2. **Start the Policy Service**
   ```bash
   # Navigate to policy-service directory
   cd policy-service

   # Build the service
   mvn clean install

   # Run the service
   mvn spring-boot:run
   ```

   The Policy Service will start on http://localhost:8080

### Claims Assistant Service (FastAPI)

1. **Start the FastAPI server**
   ```bash
   # Make sure you're in the ai_agent directory with the virtual environment activated
   uvicorn app:app --reload
   ```

2. **Access the services**
   
   Claims Assistant Service (FastAPI):
   - Main API: http://127.0.0.1:8000
   - API documentation (Swagger UI): http://127.0.0.1:8000/docs
   - Alternative API documentation (ReDoc): http://127.0.0.1:8000/redoc

   Policy Service (Spring Boot):
   - Main API: http://localhost:8080
   - API documentation (Swagger UI): http://localhost:8080/swagger-ui.html
   - Alternative API documentation: http://localhost:8080/v3/api-docs

## API Endpoints

### Claims Assistant Service (FastAPI)

#### POST `/assess`
Submit a claim for assessment.
- Accepts claim text and optional images
- Returns assessment results

#### GET `/`
Health check endpoint that returns basic API information.

### Policy Service (Spring Boot)

#### GET `/api/v1/policies`
Retrieve all available insurance policies.

#### GET `/api/v1/policies/{id}`
Retrieve a specific policy by ID.

#### POST `/api/v1/policies/validate`
Validate a claim against policy terms and conditions.
- Accepts claim details and policy ID
- Returns validation results

## Development

### Claims Assistant Service
- Main application code: `ai_agent/app.py`
- LangGraph workflow: `ai_agent/graph/workflow.py`
- Environment variables: `.env` file

### Policy Service
- Main application code: `policy-service/src/main/java/com/claims/policy/`
- Configuration: `policy-service/src/main/resources/application.properties`
- Database migrations: `policy-service/src/main/resources/db/migration/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your chosen license here]