from flask import Flask, request, Response, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    env = Environment(loader=PackageLoader('app', 'templates'), autoescape=select_autoescape(['html']))
    template = env.get_template('index.html')
    return template.render()


@app.route('/upload', methods=['POST'])
def upload():
    env = Environment(loader=PackageLoader('app', 'templates'), autoescape=select_autoescape(['html']))
    try:
        imagefile = request.files['picture']
        return Response(imagefile.getvalue(), mimetype='image/jpeg')
    except Exception as err:
        print(err)
        return render_template(env.get_template('picture.html'))

if __name__ == '__main__':
    app.run()
