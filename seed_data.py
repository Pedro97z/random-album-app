from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener URI de MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")

# Conectar a MongoDB
client = MongoClient(MONGODB_URI)
# db = client.album_database
db = client.Cluster1
album_collection = db.albums

# Datos de muestra
sample_albums = [
    {
        "name": "Cavalcade",
        "artist": "black midi",
        "release_year": 2021,
        "media_url": "https://open.spotify.com/intl-es/album/7AsC27VDa3yOksZrfBSD6D?si=6HSbqMKuTD2fsBPhudPw8w",
        "cover_image_url": "https://i.scdn.co/image/ab67616d0000b2734121faee8df82c526cbab2be",
        "genres": ["rock", "experimental"],
        "tracks_count": 9
    },
    {
        "name": "Animaru",
        "artist": "Mei Semones",
        "release_year": 2025,
        "media_url": "https://open.spotify.com/intl-es/album/6giorr9WTWilWHmD0Ox4ow?si=x4MTEwFeS16zDQU87Wz_Jg",
        "cover_image_url": "https://i.scdn.co/image/ab67616d0000b273d9194aa18fa4c9362b47464f",
        "genres": ["folk", "bossa nova"]
    },
    {
        "name": "V",
        "artist": "The Horrors",
        "release_year": 2017,
        "media_url": "https://open.spotify.com/intl-es/album/5F7t2oVAxnazEU21nbUZGc?si=JTRjxlIGSYuH6kgJGWqyPA",
        "cover_image_url": "https://i.scdn.co/image/ab67616d0000b2734e04281773490d990c20dabb",
        "genres": ["alternative rock", "industrial"]
    }
]

def seed_database():
    # Comprobar si ya hay datos
    existing_count = album_collection.count_documents({})
    
    if existing_count > 0:
        print(f"La base de datos ya contiene {existing_count} álbumes. No se insertaron datos.")
    else:
        # Insertar los datos de muestra
        result = album_collection.insert_many(sample_albums)
        print(f"Se insertaron {len(result.inserted_ids)} álbumes en la base de datos.")

if __name__ == "__main__":
    seed_database()