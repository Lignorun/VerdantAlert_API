from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <html>
        <head>
            <title>VerdantAlert API</title>
        </head>
        <body>
            <h1>🌱 VerdantAlert API</h1>
            <p>Bem-vindo! Esta API conecta-se ao <a href="https://resourcewatch.org">Global Forest Watch</a>.</p>
            <ul>
                <li><a href="/gfw/token">/gfw/token</a> – Gerar token de autenticação</li>
                <li><a href="/docs">/docs</a> – Documentação interativa da API</li>
            </ul>
        </body>
    </html>
    """
