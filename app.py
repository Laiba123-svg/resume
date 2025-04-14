from flask import Flask, render_template_string
import json

app = Flask(__name__)

@app.route('/')
def show_resume():
    with open('resume.json') as f:
        data = json.load(f)
    
    html = """
    <html>
    <head>
      <style>
        body {
          font-family: Arial, sans-serif;
          margin: 20px;
        }
        .name {
          text-align: center;
        }
        .info {
          text-align: left;
        }
        .objective-heading {
          text-align: center;
          font-weight: bold;
          margin-top: 40px;
          
        }
        .summary {
          text-align: center;
          margin-top: 10px;
          font-style: italic;
        }
      </style>
    </head>
    <body>
      <h1 class="name">{{ name }}</h1>
      <div class="info">
       <div class="info">
  <p>📧 Email: {{ email }}</p>
  <p>📱 Phone: {{ phone }}</p>
  <p>🏠 Address: {{ address }}</p>
</div>
      </div>

      <div class="objective-heading">Objective</div>
      <div class="summary">
        <p>{{ summary }}</p>
      </div>
      
      <h3>Skills</h3>
<ul style="list-style-type: none; padding-left: 0;">
  {% for skill in skills %}
  <li><strong style="color: black;">&#9679;</strong> {{ skill }}</li>
  {% endfor %}
</ul>

<h3>Work Experience</h3>
<ul>
  {% for job in experience %}
  <li>
    <strong>{{ job.position }}</strong> at <em>{{ job.company }}</em><br>
    <small>{{ job.duration }}</small><br>
    <p>{{ job.description }}</p>
  </li>
  {% endfor %}
</ul>

    </body>
    </html>
    """
    return render_template_string(html, **data)

if __name__ == '__main__':
    app.run(debug=True)


