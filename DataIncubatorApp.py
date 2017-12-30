from flask import Flask, request, send_file, Response, render_template
from jinja2 import Template, Environment, PackageLoader, select_autoescape
from base64 import b64encode

app = Flask(__name__)


@app.route('/')
def index():
    env = Environment(loader=PackageLoader('DataIncubatorApp', 'templates'), autoescape=select_autoescape(['html']))
    template = env.get_template('index.html')
    return template.render()


@app.route('/upload', methods=['POST'])
def upload():
    env = Environment(loader=PackageLoader('DataIncubatorApp', 'templates'), autoescape=select_autoescape(['html']))
    try:
        imagefile = request.files['picture'].stream
        img = imagefile.getvalue()
        return Response(img, mimetype='image/jpeg')
    except:
        return render_template(env.get_template('picture.html'))

if __name__ == '__main__':
    app.run()
