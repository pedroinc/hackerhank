# -*- coding: utf-8 -*-
# @Author Pedro Soares (pedro.soares.lacerda@tvglobo.com, pedroinc@gmail.com)

from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import Column, Integer, String

from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()

x = User.query.all()
print(x)

@app.route('/')
def index():
    try:
        name = "Pedro Henrique"
        response = []

        for x in range(0, 3):
            response.insert(x, 'item ' + str(x + 1))

        return render_template('index.html', name=name, locais=response)

    except Exception as e:
        return "Erro: {0}".format(e.message)

    # check the apps that use the appAMI


@app.route('/home', methods=['GET'])
def list_apps_ami():
    try:
        return "pedro"
    except Exception as e:
        return "Erro: {0}".format(e)


app.debug = True
application = app  # for mod_wsgi