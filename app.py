from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the webpage
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Word Counter</title>
</head>
<body>
  <h1>Hello World</h1>
  <form method="post">
    <textarea name="text" rows="5" cols="30"></textarea><br>
    <input type="submit" value="Count Words">
  </form>
  {% if word_count is not none %}
  <h2>Word Count: {{ word_count }}</h2>
  {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(text.split())
    return render_template_string(HTML_TEMPLATE, word_count=word_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
