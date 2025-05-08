from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Album(BaseModel):
    """Modelo de datos para un álbum de música"""
    name: str
    artist: str
    release_year: int
    media_url: str
    cover_image_url: str
    genres: list[str] = []

    class Config:
        schema_extra = {
            "example": {
                "name": "Emita Ox",
                "artist": "Hello Mary",
                "release_year": 2024,
                "media_url": "https://open.spotify.com/intl-es/album/13eIbvtsIMuTfvN7v3nK4X?si=tCzKfK7NQqaDNzbGGQ38xA",
                "cover_image_url": "https://i.scdn.co/image/ab67616d0000b2734121faee8df82c526cbab2be",
                "genres": ["pop", "disco", "funk"]
            }
        }

class AlbumResponse(BaseModel):
    """Modelo de respuesta para un álbum aleatorio"""
    album: Album
    timestamp: datetime = Field(default_factory=datetime.now)
