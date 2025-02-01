from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(docs_url=None, redoc_url=None)
templates = Jinja2Templates(directory='app/frontend/templates')
app.mount('/static', StaticFiles(directory='app/frontend/static'), name='static')
app.mount('/media', StaticFiles(directory='app/frontend/media'), name='media')


@app.get('/', name='index')
async def index(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/index.html', context=context)


@app.get('/about', name='about')
async def about(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/about.html', context=context)


@app.get('/contact', name='contact')
async def contact(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/contact.html', context=context)


@app.get('/pricing', name='pricing')
async def pricing(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/pricing.html', context=context)


@app.get('/faq', name='faq')
async def faq(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/faq.html', context=context)


@app.get('/blog', name='blog')
async def blog(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/blog.html', context=context)


@app.get('/blog_post', name='blog_post')
async def blog_post(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/blog_post.html', context=context)


@app.get('/portfolio', name='portfolio')
async def portfolio(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/portfolio.html', context=context)


@app.get('/portfolio_item', name='portfolio_item')
async def portfolio_item(request: Request):
    context = {'request': request}

    return templates.TemplateResponse('home/portfolio_item.html', context=context)


if __name__ == '__main__':  # pragma: no cover
    import uvicorn

    uvicorn.run(app='app.main:app', host='0.0.0.0', port=8383, log_level='info', reload=True)
