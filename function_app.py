import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Basic HTML content for the webpage
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bavithran M | DevOps & Cloud Native</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                text-align: center;
                background-color: #f4f4f4;
            }
            .container {
                margin: 20px auto;
                padding: 20px;
                background: white;
                border-radius: 8px;
                max-width: 600px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #333;
            }
            p {
                color: #555;
                font-size: 18px;
            }
            .button {
                text-decoration: none;
                color: white;
                background-color: #0078D4;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 20px;
                display: inline-block;
            }
            .button:hover {
                background-color: #0056A3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, I'm Bavithran M!</h1>
            <p>
                DevOps Enthusiast | Cloud Native Advocate | Full Stack Learner
            </p>
            <p>
                Follow me for insights on DevOps, Kubernetes, and Cloud Native technologies.
            </p>
            <a href="https://linkedin.com/in/bavicnative" class="button" target="_blank">Connect on LinkedIn</a>
        </div>
    </body>
    </html>
    """

    return func.HttpResponse(
        html_content,
        status_code=200,
        mimetype="text/html"
    )
