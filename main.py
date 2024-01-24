from fastapi import FastAPI
from sentimentModel import analyze_sentiment
import os
from dotenv import load_dotenv
load_dotenv()
baseURL = os.environ.get("BASE_URL")

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)


@app.get("/")
def root():
    return {"Message": "I'm alive"}

@app.get(F"{baseURL}/sentiment")
def sentiment(message: str):
    s = analyze_sentiment(message)
    return {"Sentiment": s}
