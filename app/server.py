from fastapi import FastAPI
from app.api.promtior import router as promtior_router

app = FastAPI()
app.include_router(promtior_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.server:app", host="0.0.0.0", port=8000, reload=True)