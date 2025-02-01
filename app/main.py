from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory='frontend/templates')
app.mount('/static', StaticFiles(directory='restapi/frontend/static'), name='static')
app.mount('/media', StaticFiles(directory='restapi/frontend/media'), name='media')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='restapi.main:app', host='0.0.0.0', port=8383, log_level='info', reload=True)
