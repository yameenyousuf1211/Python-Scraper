from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.helper import generateResponse
from controller.root_controller import router as root_router
from controller.scrape_controller import router as scrape_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return generateResponse("Welcome to the Chat Bot API")


app.include_router(root_router) 
app.include_router(scrape_router) 
