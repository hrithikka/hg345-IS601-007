from flask import Blueprint, redirect, request, render_template, url_for, flash, Flask, request, jsonify, session
import requests
from sql.db import DB

favourites = Blueprint('favourites', __name__, url_prefix='/favourites',
                       template_folder="templates")


@favourites.route("/", methods=["GET"])
def get_favourites():
    user_id = session.get('_user_id')

    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401

    movies = DB.selectAll(
        "SELECT * from favourites f inner join movies m where f.movie_id = m.id and f.user_id = %s", user_id)
    return render_template("favourite_list.html", media_list=movies.rows)


@favourites.route('/<string:movie_id>', methods=['POST'])
def add_favourites(movie_id):
    user_id = session.get('_user_id')

    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401

    favorite = DB.insertOne(
        "INSERT INTO favourites (user_id, movie_id) VALUES (%s, %s)",
        user_id, movie_id)

    return jsonify({"message": "Added as a favourite"}), 200


@favourites.route('/<string:movie_id>', methods=['DELETE'])
def delete_media(movie_id):
    user_id = session.get('_user_id')
    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401

    delete_favourites = DB.delete(
        "delete FROM favourites WHERE movie_id = %s", movie_id)
    return jsonify({"message": "Deleted"}), 204
