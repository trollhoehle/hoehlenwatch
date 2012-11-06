#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../status.db'
db = SQLAlchemy(app)


class Status(db.Model):
    mac = db.Column(db.String(255), primary_key=True)
    ip = db.Column(db.String(80))
    last_seen = db.Column(db.Date())

    def __init__(self, mac, ip, last_seen):
        self.mac = mac
        self.ip = ip
        self.last_seen = last_seen

    def __repr__(self):
        return '<Status %r>' % self.mac


@app.route('/')
def list():
    stati = Status.query.order_by(Status.mac).all()
    return render_template('list.html', stati=stati)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

