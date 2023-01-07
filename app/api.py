from flask import render_template, jsonify, request
from app import app
from app.models import db, Stuff


@app.route('/', methods=['GET'])
def home():
    stuff = [s.json() for s in Stuff.query.all()]
    return render_template('home.html', stuff=stuff)


@app.route('/api/get/stuff', methods=['GET'])
def api_get_stuff():
    stuff = [s.json() for s in Stuff.query.all()]
    print('getting stuff: {}'.format(stuff))
    return jsonify(stuff)


# NOTE this will not be used on netlify
# as far as I know post requests do not work
# with Flask-freeze
@app.route('/api/add/stuff', methods=['POST'])
def api_add_stuff():
    name = request.json.get('name')
    age = request.json.get('age')

    new_stuff = Stuff(
        name=name,
        age=age
    )
    db.session.add(new_stuff)
    db.session.commit()

    print('adding stuff: {}'.format(new_stuff.json()))
    return jsonify(new_stuff.json())

