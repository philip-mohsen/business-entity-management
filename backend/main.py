# File: backend/main.py
from fastapi import FastAPI
import uvicorn
from src.presentation.web.api.attribute_schema_router import router as attribute_schema_router

app = FastAPI(
    title="Business Entity Management API",
    description="API for managing business entities and attributes.",
    version="1.0.0"
)

# Register routers
app.include_router(attribute_schema_router)

@app.get("/")
def health_check():
    return {"status": "online", "message": "Business Entity Management System is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
