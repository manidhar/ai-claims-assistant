# AI Claims Assistant

An AI-powered assistant for processing and assessing boat insurance claims using FastAPI, LangGraph, and open-source LLMs. The system uses locally-hosted open-source models for privacy and cost-effectiveness.

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
   # MODEL_PATH=path/to/your/local/model  # Path to your open-source model
   # PORT=8000 (optional, defaults to 8000)
   # POLICY_SERVICE_URL=http://localhost:8080 (Spring Boot service URL)
   # Optional model configuration:
   # MODEL_TYPE=llama2 # or other supported model type
   # MODEL_DEVICE=cpu  # or cuda for GPU acceleration
   ```

## Running the Application

### Policy Service (Spring Boot)

1. **Prerequisites**
   - Java 17 or higher
   - Gradle 8.0+ or higher

2. **Start the Policy Service**
   ```bash
   # Navigate to policy-service directory
   cd policy-service

   # Build the service
   ./gradlew clean build

   # Run the service
   ./gradlew bootRun
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

## Testing the Application

### Using cURL

1. **Test Policy Service Health Check**
   ```bash
   curl http://localhost:8080/actuator/health
   ```
   Expected Response:
   ```json
   {
     "status": "UP"
   }
   ```

2. **Get Available Policies**
   ```bash
   curl http://localhost:8080/api/v1/policies
   ```
   Expected Response:
   ```json
   [
     {
       "id": "1",
       "name": "Standard Boat Insurance",
       "coverage": ["collision", "theft", "natural disasters"],
       "maxCoverageAmount": 50000
     }
   ]
   ```

3. **Test Claims Assistant Health Check**
   ```bash
   curl http://127.0.0.1:8000
   ```
   Expected Response:
   ```json
   {
     "message": "🚤 AI Claims Assistant is running!",
     "endpoints": ["/assess (POST)"],
     "model": "open-source LLM"
   }
   ```

4. **Submit a Claim Assessment**
   ```bash
   # Without image
   curl -X POST http://127.0.0.1:8000/assess \
     -H "Content-Type: multipart/form-data" \
     -F "claim_text=My boat was damaged during a storm last night. The hull has a crack and the navigation equipment is not working."
   ```
   Expected Response:
   ```json
   {
     "status": "success",
     "result": {
       "claim_id": "claim_123",
       "assessment": {
         "damage_type": ["hull_damage", "equipment_failure"],
         "coverage_status": "covered",
         "estimated_cost": 15000,
         "recommended_action": "approve",
         "confidence_score": 0.85
       },
       "policy_validation": {
         "policy_id": "1",
         "covered_by_policy": true,
         "relevant_terms": ["natural disasters", "equipment damage"]
       }
     }
   }
   ```

### Using Python Requests

```python
import requests

# Submit a claim with an image
def submit_claim():
    url = "http://127.0.0.1:8000/assess"
    
    # Claim text
    data = {
        "claim_text": "My boat was damaged during a storm last night. The hull has a crack."
    }
    
    # Optional: Add image
    files = {
        "images": ("damage.jpg", open("path/to/damage.jpg", "rb"), "image/jpeg")
    }
    
    response = requests.post(url, data=data, files=files)
    print(response.json())

# Test policy service
def get_policies():
    url = "http://localhost:8080/api/v1/policies"
    response = requests.get(url)
    print(response.json())
```

### Using Swagger UI

1. **Access Swagger Documentation**
   - Claims Assistant API: Open http://127.0.0.1:8000/docs in your browser
   - Policy Service API: Open http://localhost:8080/swagger-ui.html in your browser

2. **Test Endpoints**
   - Click on any endpoint to expand it
   - Click "Try it out"
   - Fill in the required parameters
   - Click "Execute"
   - View the response

### Common Testing Scenarios

1. **Basic Claim Assessment**
   - Submit a simple claim without images
   - Verify damage classification
   - Check policy coverage validation

2. **Image-Based Assessment**
   - Submit a claim with damage photos
   - Verify image analysis results
   - Check damage severity assessment

3. **Policy Validation**
   - Test claims against different policy types
   - Verify coverage limits
   - Check excluded damage types

4. **Error Handling**
   - Submit invalid claim format
   - Test with unsupported image types
   - Check API error responses

## Development

### Claims Assistant Service
- Main application code: `ai_agent/app.py`
- LangGraph workflow: `ai_agent/graph/workflow.py`
- Environment variables: `.env` file

### Policy Service
- Main application code: `policy-service/src/main/java/com/claims/policy/`
- Configuration: `policy-service/src/main/resources/application.properties`
- Database migrations: `policy-service/src/main/resources/db/migration/`
- Build configuration: `policy-service/build.gradle`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your chosen license here]