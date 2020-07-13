import aiohttp
import asyncio
import uvicorn
import os
from fastai import *
from fastai.vision import *
from io import BytesIO
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
import requests

Port = int(os.environ.get('PORT', 5000))

export_file_url = 'https://drive.google.com/file/d/1g0ZbeWZFgU7mL-0EmbOminZ0jeF-kUpu/view?usp=sharing'
export_file_name = 'model_klasifikasi_tumor.pkl'

classes = ["Tumor jinak" , "Tumor ganas"]
path = Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))
app.mount('/prod-view', StaticFiles(directory='app/prod-view'))
