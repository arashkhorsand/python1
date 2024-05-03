from flask import Flask, request, render_template_string

# Create a Flask application
app = Flask(__name__)

# HTML template for the homepage
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <title>Hello World</title>
</head>
<body>
  <h1>Hello World!</h1>
  <form method="post">
    <label for="user_input">Enter text:</label>
    <input type="text" id="user_input" name="user_input">
    <button type="submit">Count Words</button>
  </form>
  {% if word_count is not none %}
    <p>Word Count: {{ word_count }}</p>
  {% endif %}
</body>
</html>
"""

# Route for handling the root path
@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    if request.method == 'POST':
        text = request.form.get('user_input', '')
        word_count = len(text.split())
    return render_template_string(HTML_TEMPLATE, word_count=word_count)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)