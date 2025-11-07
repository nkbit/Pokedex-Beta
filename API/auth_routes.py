from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def Autenticação():
    return {"message": "Area de Autenticação"}
