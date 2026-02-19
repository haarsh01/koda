from fastapi import FastAPI
from app.api import router  # This will now work!

app = FastAPI(title="Koda AI")

# Connect the "nerves" to the "brain"
app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Koda Backend Entry Point"}