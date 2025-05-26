from fastapi import FastAPI
from app.api.promptior import router as promptior_router

app = FastAPI()
app.include_router(promptior_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.server:app", host="0.0.0.0", port=8000, reload=True)