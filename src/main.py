"""
AgroCare API
"""
from fastapi import FastAPI
app = FastAPI()
app.title = "AgroCare API"


@app.get('/', tags=['User'])
def create_user():
    """
    Bienvenida
    """
    print("HOLA")
    return ""


@app.delete('/{id}', tags=['User'])
def delete_user():
    """
    Bienvenida
    """
    print("HOLA")
    return ""
