from fastapi import APIRouter, HTTPException, status
from datetime import datetime

from .database import get_random_album
from .models import Album, AlbumResponse

router = APIRouter()

@router.get("/", response_description="Obtener la página principal")
async def root():
    """Endpoint raíz"""
    return {"message": "¡Bienvenido a la API de álbumes aleatorios!"}

@router.get("/random", response_description="Obtener un álbum aleatorio", response_model=AlbumResponse)
async def random_album():
    """Endpoint para obtener un álbum aleatorio"""
    album_data = get_random_album()
    
    if not album_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No se encontraron álbumes en la base de datos"
        )
    
    # Convertir el ObjectId de MongoDB a string para evitar problemas de serialización
    if "_id" in album_data:
        album_data["_id"] = str(album_data["_id"])
    
    # Devolver la respuesta formateada
    return AlbumResponse(
        album=Album(**album_data),
        timestamp=datetime.now()
    )