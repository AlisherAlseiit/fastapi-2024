from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
# from .config import settings
# models.Base.metadata.create_all(bind=engine)

app = FastAPI() 


# CORSP section before deployment
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root(): 
    return {"message": "HELLO FROM DOCKER!"}
    




    