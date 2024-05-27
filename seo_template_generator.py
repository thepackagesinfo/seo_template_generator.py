# seo_template_generator.py

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Your description here">
    <meta name="keywords" content="keyword1, keyword2, keyword3">
    <meta name="author" content="Your Name">
    <title>Your Page Title</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a basic HTML template with SEO meta tags.</p>
</body>
</html>
"""

# Save the HTML template to a file
with open("index.html", "w") as file:
    file.write(html_template)

print("HTML template with SEO meta tags has been generated as 'index.html'.")
