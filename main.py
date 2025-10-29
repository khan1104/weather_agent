from fastapi import FastAPI,status
from pydantic import BaseModel
import uvicorn
from agent.llm_agent import ask


app=FastAPI(title="Weather AI Agent")

class AskRequest(BaseModel):
    query:str

class AskResponse(BaseModel):
    response:str

@app.get("/")
def health():
    return {"message":"server is running fine and up"}


@app.post("/ask",status_code=status.HTTP_200_OK,response_model=AskResponse)
async def ask_ai(user_query:AskRequest):
    response=ask(user_query.query)
    return {"response": response}


if __name__=="__main__":
    uvicorn.run("main:app",reload=True)
