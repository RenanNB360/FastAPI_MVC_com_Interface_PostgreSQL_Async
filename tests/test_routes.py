import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    'route',
    [
        ('/', 'index'),
        ('/about', 'about'),
        ('/contact', 'contact'),
        ('/pricing', 'pricing'),
        ('/faq', 'faq'),
        ('/blog', 'blog'),
        ('/blog_post', 'blog_post'),
        ('/portfolio', 'portfolio'),
        ('/portfolio_item', 'portfolio_item'),
    ],
)
def test_routes_return_200(route):
    url, _ = route
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK, f'Erro: {url} não retornou 200'
    assert 'text/html' in response.headers['content-type'], f'Erro: {url} não retornou HTML'
