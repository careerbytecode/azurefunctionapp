import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Enhanced HTML content for the webpage
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bavithran M | Senior Software Engineer (DevOps)</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f3f4f6;
                color: #333;
            }
            .header {
                background-color: #0078D4;
                color: white;
                padding: 20px 0;
                text-align: center;
            }
            .header h1 {
                margin: 0;
                font-size: 2.5em;
            }
            .header p {
                margin: 10px 0 0;
                font-size: 1.2em;
            }
            .container {
                max-width: 900px;
                margin: 40px auto;
                background: white;
                border-radius: 8px;
                padding: 20px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .profile-pic {
                display: block;
                margin: 0 auto;
                border-radius: 50%;
                width: 150px;
                height: 150px;
                object-fit: cover;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .content h2 {
                text-align: center;
                color: #0078D4;
            }
            .content p {
                line-height: 1.6;
                margin: 15px 0;
                text-align: justify;
            }
            .social-links {
                text-align: center;
                margin-top: 20px;
            }
            .social-links a {
                text-decoration: none;
                color: white;
                background-color: #0078D4;
                padding: 10px 20px;
                margin: 0 10px;
                border-radius: 5px;
                font-weight: bold;
                display: inline-block;
                transition: background-color 0.3s ease;
            }
            .social-links a:hover {
                background-color: #0056A3;
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
            <h1>Bavithran M</h1>
            <p>Senior Software Engineer (DevOps) | Cloud Native Enthusiast</p>
        </div>
        <div class="container">
            <img src="https://via.placeholder.com/150" alt="Profile Picture" class="profile-pic">
            <div class="content">
                <h2>About Me</h2>
                <p>
                    I am a DevOps professional with experience in cloud-native technologies, Kubernetes, and CI/CD automation.
                    Currently working as a Senior Software Engineer (DevOps) at Amantya Technologies, I focus on delivering scalable 
                    and efficient solutions for on-premises and cloud-based environments.
                </p>
                <h2>Achievements</h2>
                <ul>
                    <li>Certified in Azure and AWS Cloud Platforms</li>
                    <li>Expert in CI/CD tools like Jenkins, Terraform, and Ansible</li>
                    <li>Contributor to open-source projects and active community builder</li>
                </ul>
            </div>
            <div class="social-links">
                <a href="https://linkedin.com/in/bavicnative" target="_blank">Connect on LinkedIn</a>
                <a href="https://github.com/bavicnative" target="_blank">Explore My GitHub</a>
                <a href="https://careerbytecode.substack.com/" target="_blank">Read My Blogs</a>
            </div>
        </div>
        <div class="footer">
            <p>&copy; 2024 Bavithran M | DevOps | Cloud Native | Kubernetes</p>
        </div>
    </body>
    </html>
    """

    return func.HttpResponse(
        html_content,
        status_code=200,
        mimetype="text/html"
    )
