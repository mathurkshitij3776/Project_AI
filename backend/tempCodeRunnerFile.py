# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# import os
# from openai import OpenAI
# from dotenv import load_dotenv
# from pydantic import BaseModel
# import uvicorn

# load_dotenv()


# endpoint = "https://models.github.ai/inference"
# model = "openai/gpt-5"

# client = OpenAI(
#     base_url=endpoint,
#     api_key=token,
# )



# app = FastAPI()

# # CORS for frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",
#         "http://127.0.0.1:5173",
#         "http://localhost:3000",  # In case you're using different port
#         "http://127.0.0.1:3000"
#     ],
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["*"],
# )
# SYSTEM = (
#     "You are a world-class Marketing Strategist who has consulted businesses "
#     "of all sizes and scales. You specialize in creating digital marketing strategies "
#     "that help companies grow and scale effectively."
# )

# class StrategyRequest(BaseModel):
#     business_type: str
#     budget: str
#     target_audience: str
#     productdescription: str  # Match your frontend field name

# class StrategyResponse(BaseModel):
#     business_type: str
#     budget: str
#     target_audience: str
#     product_description: str
#     strategy: str


# @app.post("/api/generatestrategy")
# async def generatestrategy(request: Request):
#     data = await request.json()
    
#     business_type = data.get("business_type", "general business")
#     budget = data.get("budget", "unspecified")
#     target_audience = data.get("target_audience", "general customers")
#     productdescription = data.get("product_description", "")

#     user = f"""
#     I run a {business_type}. My marketing budget is {budget}.
#     My target audience is {target_audience}.
#     My product description is: {productdescription}.
#     Suggest a detailed digital marketing strategy with:
#     -Recommended channels
#     -Content ideas
#     -Budget allocation
#     """

#     response = client.chat.completions.create(
#         model=model,
#         messages=[
#             {"role": "system", "content": SYSTEM},
#             {"role": "user", "content": user}
#         ],
#         max_tokens=2000,
#         temperature=0.7
#     )

#     return {
#         "business_type": business_type,
#         "budget": budget,
#         "target_audience": target_audience,
#         "product_description": productdescription,
#         "strategy": response.choices[0].message.content
#     }

# # Debug/Test run (optional)
# if __name__ == "__main__":
#     # response = client.chat.completions.create(
#     #     model=model,
#     #     messages=[
#     #         {"role": "system", "content": SYSTEM},
#     #         {"role": "user", "content": "Suggest a digital marketing strategy for a SaaS startup with $10,000 budget."}
#     #     ]
#     # )
#     # print(response.choices[0].message.content)
#     uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
#     # generatestrategy()

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
    model=model
)

print(response.choices[0].message.content)
