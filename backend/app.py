from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import uvicorn
import re
load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)



app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


SYSTEM = (
    "You are a world-class Marketing Strategist who has consulted businesses "
    "of all sizes and scales. You specialize in creating digital marketing strategies "
    "that help companies grow and scale effectively. dont put any other things like stars or any other thing."
)

class StrategyRequest(BaseModel):
    business_type: str
    budget: str
    target_audience: str
    productdescription: str  # Match your frontend field name

class StrategyResponse(BaseModel):
    business_type: str
    budget: str
    target_audience: str
    product_description: str
    strategy: str


@app.post("/api/generatestrategy")
async def generatestrategy(request: Request):
    data = await request.json()
    
    business_type = data.get("business_type", "general business")
    budget = data.get("budget", "unspecified")
    target_audience = data.get("target_audience", "general customers")
    productdescription = data.get("product_description", "")

    user = f"""
    I run a {business_type}. My marketing budget is {budget}.
    My target audience is {target_audience}.
    My product description is: {productdescription}.
    Suggest a detailed digital marketing strategy with:
    -Recommended channels
    -Content ideas
    -Budget allocation
    - who could be our potential client
    """

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user}
        ],
        max_tokens=2000,
        temperature=0.7
    )
    # raw_strategy = response.choices[0].message.content
    # clean_strategy = re.sub(r'#+ ', '', raw_strategy)
    
    # # Remove bullets (- or *)
    # clean_strategy = re.sub(r'^[-*]\s+', '', clean_strategy, flags=re.MULTILINE)
    raw_strategy = response.choices[0].message.content

# Remove markdown headings, bullets, bold/italics
    clean_strategy = re.sub(r'#+ ', '', raw_strategy)   # remove ##
    clean_strategy = re.sub(r'\*\*(.*?)\*\*', r'\1', clean_strategy)  # bold
    clean_strategy = re.sub(r'\*(.*?)\*', r'\1', clean_strategy)      # italics
    clean_strategy = re.sub(r'^[-*]\s+', '', clean_strategy, flags=re.MULTILINE)  # bullets
    return {
        "business_type": business_type,
        "budget": budget,
        "target_audience": target_audience,
        "product_description": productdescription,
        "strategy": clean_strategy 
    }

# Debug/Test run (optional)
if __name__ == "__main__":
    
    # uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
    # generatestrategy()
    port = int(os.environ.get("PORT", 5000))  # Render gives PORT
    uvicorn.run(app, host="0.0.0.0", port=port)

