from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.enciron['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from modes import Result

@app.route('/<name>')
def hello_name(name):
    return "hello {}".format(name)

if __name__=='__main__':
    app.run
