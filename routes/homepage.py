from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def homepage():
    return """
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>VerdantAlert API</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f8;
                color: #333;
                margin: 0;
                padding: 0 2rem 3rem 2rem;
                line-height: 1.6;
            }
            header {
                background-color: #2a7f62;
                color: white;
                padding: 1.5rem 2rem;
                text-align: center;
                box-shadow: 0 2px 4px rgb(0 0 0 / 0.1);
            }
            header h1 {
                margin: 0;
                font-weight: 700;
                font-size: 2.4rem;
            }
            main {
                max-width: 900px;
                margin: 2rem auto;
                background: white;
                padding: 2rem 3rem;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgb(0 0 0 / 0.1);
            }
            section {
                margin-bottom: 2.5rem;
            }
            h2 {
                color: #2a7f62;
                border-bottom: 2px solid #2a7f62;
                padding-bottom: 0.3rem;
                margin-bottom: 1rem;
            }
            p, li {
                font-size: 1.1rem;
            }
            a {
                color: #2a7f62;
                text-decoration: none;
                font-weight: 600;
            }
            a:hover {
                text-decoration: underline;
            }
            .note {
                font-size: 0.95rem;
                color: #555;
                font-style: italic;
                margin-top: 0.4rem;
            }
            ul.routes {
                list-style-type: none;
                padding-left: 0;
            }
            ul.routes li {
                background: #e6f0ec;
                margin-bottom: 0.8rem;
                padding: 0.9rem 1.2rem;
                border-radius: 6px;
                font-family: monospace;
                box-shadow: inset 0 0 5px rgba(42,127,98,0.15);
            }
            footer {
                text-align: center;
                font-size: 0.9rem;
                color: #777;
                margin-top: 4rem;
                border-top: 1px solid #ddd;
                padding-top: 1rem;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>🌱 VerdantAlert API</h1>
        </header>

        <main>
            <section>
                <h2>About This API</h2>
                <p>
                    VerdantAlert API connects with the 
                    <a href="https://resourcewatch.org" target="_blank" rel="noopener noreferrer">Global Forest Watch</a> platform,
                    providing authenticated access to important environmental data.
                </p>
                <p>
                    <strong>Note:</strong> The authentication token endpoint (<code>/gfw/token</code>) is intended <em>only</em> for testing and development purposes. 
                    It <strong>must not</strong> be exposed publicly or accessible by external users in a production environment.
                </p>
                <p>
                    This design choice ensures secure handling of sensitive credentials and tokens, 
                    keeping your system robust and compliant with security best practices.
                </p>
            </section>

            <section>
                <h2>Available Endpoints</h2>
                <ul class="routes">
                    <li><a href="/gfw/token">GET /gfw/token</a> — Generate authentication token (test use only)</li>
                    <li><a href="/docs">GET /docs</a> — Interactive API documentation (Swagger UI)</li>
                </ul>
            </section>

            <section>
                <h2>Project &amp; Source Code</h2>
                <p>
                    Explore the full source code and contribute on 
                    <a href="https://github.com/Lignorun/VerdantAlert_API" target="_blank" rel="noopener noreferrer">GitHub</a>.
                </p>
            </section>
        </main>

        <footer>
            &copy; 2025 Diego Lins &mdash; VerdantAlert API
        </footer>
    </body>
    </html>
    """
