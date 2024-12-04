import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="CareerByteCode", auth_level=func.AuthLevel.ANONYMOUS)
def CareerByteCode(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Enhanced HTML content with contributor details
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CareerByteCode | Your IT Success Hub</title>
        <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #343a40;
            }
            .header {
                background: linear-gradient(90deg, #0078D4, #0056A3);
                color: white;
                text-align: center;
                padding: 40px 20px;
            }
            .header h1 {
                font-size: 3em;
                margin: 0;
            }
            .header p {
                margin: 10px 0;
                font-size: 1.2em;
            }
            .container {
                max-width: 1200px;
                margin: 20px auto;
                padding: 20px;
                background: white;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .section {
                margin-bottom: 30px;
            }
            .section h2 {
                color: #0078D4;
                margin-bottom: 15px;
            }
            .section p, .section ul {
                line-height: 1.6;
            }
            .cta {
                text-align: center;
                margin-top: 30px;
            }
            .cta a {
                text-decoration: none;
                color: white;
                background-color: #0078D4;
                padding: 15px 30px;
                border-radius: 5px;
                font-size: 1.2em;
                transition: background-color 0.3s ease;
            }
            .cta a:hover {
                background-color: #0056A3;
            }
            .contributor {
                background-color: #f3f4f6;
                padding: 20px;
                margin-top: 30px;
                border-top: 1px solid #ddd;
                text-align: center;
                border-radius: 10px;
            }
            .contributor h3 {
                margin-top: 0;
                color: #0078D4;
            }
            .contributor p {
                margin: 5px 0;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                padding: 20px;
                font-size: 0.9em;
                background-color: #f3f4f6;
                border-top: 1px solid #ddd;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>CareerByteCode</h1>
            <p>Your One-Stop IT Success Hub</p>
        </div>
        <div class="container">
            <div class="section">
                <h2>Overview</h2>
                <p>Welcome to CareerByteCode, your one-stop destination for comprehensive and practical training in cloud computing, DevOps, and IT solutions. Our mission is to empower IT professionals, enthusiasts, and beginners with the knowledge and skills needed to excel in today's dynamic tech landscape.</p>
            </div>
            <div class="section">
                <h2>What We Offer</h2>
                <ul>
                    <li>💼 <b>Interview Prep:</b> Get tailored questions and answers for your dream role. Share the job description, and we’ll handle the rest!</li>
                    <li>🌐 <b>Real-Time Use Cases:</b> Facing challenges in cloud, DevOps, data, Python, AI, or machine learning? We provide detailed steps and solutions!</li>
                    <li>📚 <b>Interview Q&A:</b> Need focused prep for an upcoming interview? We’ve got customized questions and answers just for you!</li>
                    <li>🏗️ <b>Becoming a Solution Architect:</b> Share your business cases, and we’ll build detailed solutions with architecture diagrams.</li>
                    <li>🏅 <b>Certification Prep:</b> Let us craft mock exam questions and answers to help you ace it!</li>
                    <li>🔧 <b>Error Troubleshooting:</b> Stuck on an error? We’ll provide step-by-step solutions for any issues in cloud, DevOps, data, Python, AI, and more.</li>
                    <li>📝 <b>Resume Building:</b> Craft a standout resume tailored to your target job with our help!</li>
                </ul>
            </div>
            <div class="cta">
                <a href="https://careerbytecode.substack.com/welcome" target="_blank">Visit CareerByteCode</a>
            </div>
        </div>
        <div class="contributor">
            <h3>Contributor</h3>
            <p><b>Name:</b> Bavithran M</p>
            <p><b>Role:</b> Senior Software Engineer (DevOps)</p>
            <p><b>Details:</b> Cloud Native Enthusiast | DevOps Practitioner | Kubernetes Explorer</p>
            <p><b>Connect:</b> <a href="https://linkedin.com/in/bavicnative" target="_blank">LinkedIn</a> | <a href="https://github.com/bavicnative" target="_blank">GitHub</a></p>
        </div>
        <div class="footer">
            <p>&copy; 2024 CareerByteCode | Empowering IT Professionals</p>
        </div>
    </body>
    </html>
    """
    return func.HttpResponse(
        html_content,
        status_code=200,
        mimetype="text/html"
    )
