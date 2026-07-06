from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="GenAI Interview Quiz")

@app.get('/api/items')
async def list_items():
    return []

@app.get('/api/topics')
async def list_topics():
    return []

@app.get('/api/quiz')
async def get_quiz():
    return []

@app.post('/api/quiz/answer')
async def submit_answer():
    return {}

@app.get('/api/quiz/search')
async def search_quiz():
    return []

BUILD_DIR = os.path.join(os.path.dirname(__file__), 'frontend', 'build')
if os.path.isdir(BUILD_DIR):
    app.mount('/static', StaticFiles(directory=os.path.join(BUILD_DIR, 'static')), name='static')

    @app.get('/{full_path:path}')
    async def serve_frontend(full_path: str):
        return FileResponse(os.path.join(BUILD_DIR, 'index.html'))
