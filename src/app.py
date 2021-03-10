from flask import Flask
from blueprints.main import main

app = Flask(__name__)
app.register_blueprint(main,url_prefix='')


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
