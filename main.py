from fastapi import FastAPI, HTTPException
from services.gfw_auth import get_gfw_token
from routes.homepage import router as homepage_router

app = FastAPI()

app.include_router(homepage_router)

@app.get("/gfw/token")
def read_token():
    token = get_gfw_token()
    if token:
        return {"token": token}
    raise HTTPException(status_code=500, detail="Erro ao obter o token da GFW.")
