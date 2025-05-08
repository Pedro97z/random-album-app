from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routes import router
from .database import initialize_db

# Crear la aplicación FastAPI
app = FastAPI(
    title="Random Album API",
    description="API para obtener información de álbumes musicales aleatorios",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origenes en desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir las rutas
app.include_router(router)

# Configurar punto de entrada HTML simple
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Puedes incluir una página HTML simple
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Random Album API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                }
                .album-container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    margin-top: 30px;
                }
                .album-cover {
                    max-width: 300px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    margin-bottom: 20px;
                }
                .album-info {
                    text-align: center;
                }
                button {
                    background-color: #1DB954;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 30px;
                    cursor: pointer;
                    font-size: 16px;
                    margin-top: 20px;
                }
                button:hover {
                    background-color: #1ed760;
                }
                .spotify-link {
                    display: inline-block;
                    background-color: #1DB954;
                    color: white;
                    text-decoration: none;
                    padding: 8px 16px;
                    border-radius: 20px;
                    margin-top: 10px;
                }
            </style>
        </head>
        <body>
            <h1>Álbum Aleatorio</h1>
            <div class="album-container" id="album-display">
                <p>Pulsa el botón para obtener un álbum aleatorio</p>
            </div>
            <div style="text-align: center;">
                <button id="random-button">Obtener Álbum Aleatorio</button>
            </div>
            
            <script>
                document.getElementById('random-button').addEventListener('click', async () => {
                    try {
                        const response = await fetch('/random');
                        if (!response.ok) {
                            throw new Error('Error al cargar datos');
                        }
                        const data = await response.json();
                        const album = data.album;
                        
                        document.getElementById('album-display').innerHTML = `
                            <img src="${album.cover_image_url}" alt="${album.name}" class="album-cover">
                            <div class="album-info">
                                <h2>${album.name}</h2>
                                <h3>${album.artist}</h3>
                                <p>Año: ${album.release_year}</p>
                                <p>Género(s): ${album.genres.join(', ')}</p>
                                <a href="${album.media_url}" target="_blank" class="spotify-link">Escuchar en Spotify</a>
                            </div>
                        `;
                    } catch (error) {
                        console.error('Error:', error);
                        document.getElementById('album-display').innerHTML = `
                            <p>Error al cargar el álbum. Por favor, intenta de nuevo.</p>
                        `;
                    }
                });
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Verificar conexión a la base de datos al iniciar
@app.on_event("startup")
async def startup_db_client():
    db_initialized = initialize_db()
    print(f"Base de datos inicializada: {db_initialized}")