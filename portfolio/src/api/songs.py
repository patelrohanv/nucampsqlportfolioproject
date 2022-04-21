from flask import Blueprint, jsonify, abort, request
from ..models import Song, db

bp = Blueprint('songs', __name__, url_prefix='/songs')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    songs = Song.query.all()  # ORM performs SELECT query
    result = []
    for s in songs:
        result.append(s.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    pass


@bp.route('', methods=['POST'])
def create():
    if 'title' not in request.json or 'length' not in request.json:
        return abort(400)

    song = Song(
        title=request.json['title'],
        length=request.json['length']
    )

    db.session.add(song) # INSERT INTO users
    db.session.commit()

    return jsonify(song.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    pass

