from flask import Blueprint, flash, render_template, request, redirect, url_for,session,jsonify
import requests
from movies.forms import MovieForm
from sql.db import DB # Import your DB class
from roles.permissions import admin_permission
from flask_login import current_user, login_required

movies = Blueprint('movies', __name__, url_prefix='/movies',template_folder='templates')


@movies.route('/', methods=['GET'])
def list_movie():
    user_id = session.get('_user_id')

    if user_id is None:
        return jsonify({'status': 'error', 'message': 'User not authenticated'}), 401
    movies = DB.selectAll(
        "SELECT * FROM movies order by created_at desc")
    favourite_movies = DB.selectAll(
        "SELECT movie_id from favourites where user_id = %s", user_id)
    fav_movie_ids = [record.get("movie_id")
                     for record in favourite_movies.rows]
    for movie in movies.rows:
        if movie.get("id") in fav_movie_ids:
            movie["is_favourite"] = True
        else:
            movie["is_favourite"] = False

    return render_template('movie_list.html', movie_list=movies.rows)


# @movies.route('/<string:imdb_id>', methods=['GET'])
# def get_movie(imdb_id):
#     record = DB.selectOne("SELECT * FROM movies WHERE imdb_id = %s", imdb_id)
#     if record.row:
#         return render_template('templates/movie_detail.html', movie=record)
#     else:
#         return jsonify({"message": "movie not found"}), 404
@movies.route('/details/<string:id>', methods=['GET'])
def movie_details(id):
    # Retrieve the movie details from the database
    movie = DB.selectOne("SELECT * FROM movies WHERE id = %s", id)
    
    # Check if the movie with the given ID exists
    if movie.row:
        return render_template('movie_details.html', movie=movie.row)
    else:
        return jsonify({"message": "Movie not found"}), 404


@movies.route('/add', methods=['GET', 'POST'])
@admin_permission.require(http_exception=403)
def add_movie():
    form = MovieForm()
    if request.method == 'GET':
        # Render the form for adding a new movie
        return render_template('add_movie.html', form=form)
    elif request.method == 'POST':
        # Process the form submission for adding a new movie
        data = request.form

        # Perform validation on the form data as needed
        # Check if the movie already exists in the database
        existing_movie = DB.selectOne("SELECT * FROM movies WHERE title = %s", form.title.data)

        print("Form Title:", form.title.data)
        print("Existing Movie:", existing_movie)

        # Access the 'rows' attribute of the DBResponse object
        if not existing_movie.rows:
            # Movie with the same title does not exist, proceed with insertion
            # Insert the new movie record into the database
            result = DB.insertOne(
                "INSERT INTO movies (imageURL, genre, title, imdbrating, released, type, synopsis) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                form.imageURL.data, form.genre.data, form.title.data,
                form.imdbrating.data, form.released.data, form.type.data, form.synopsis.data)

            print("Insert Result:", result)

            if result.status:
                flash("Movie added successfully", "success")
                # Redirect to the movies listing page after adding
                return redirect("/movies")
            else:
                flash(result.message, "danger")
                # Redirect to the movies listing page even if there's an error
                return jsonify({"message": "Adding failed"}), 404
        else:
            # Movie with the same title already exists
            flash("Movie with the same title already exists", "danger")
            return render_template('add_movie.html', form=form)




@movies.route('/<string:id>', methods=['GET', 'PUT'])
@admin_permission.require(http_exception=403)
def update_movie(id):
    if request.method == 'GET':
        # Retrieve the movie record from the database
        record = DB.selectOne(
            "SELECT * FROM movies WHERE id = %s", id)

        # Check if the record with the IMDb ID exists
        if record:
            return render_template('movie_update.html', movie=record.row)
        else:
            return jsonify({"message": "movie not found"}), 404
    elif request.method == 'PUT':
        # Process the form submission for updating movie
        data = request.form
        print(data.get('imdbrating'))
        # Update the movie record in the database
        result = DB.update(
            "UPDATE movies SET imageURL=%s, genre=%s, title=%s, imdbrating=%s, released=%s, type=%s, synopsis=%s WHERE id=%s",
            data.get('imageURL'), data.get('genre'), data.get(
                'title'), data.get('imdbrating'),
            data.get('released'), data.get('type'), data.get('synopsis'), id)

        if result.status:
            flash("movie updated successfully", "success")
            return jsonify({"message": "Updated"}), 200
            # Redirect to the movies listing page after updating

        else:
            flash(result.message, "danger")
            # Redirect to the movies listing page even if there's an error


@movies.route('/<string:id>', methods=['DELETE'])
@admin_permission.require(http_exception=403)
def delete_movie(id):
    # Check if the record with the IMDb ID exists
    #print("Hello world")
    record = DB.selectOne("SELECT * FROM movies WHERE id = %s", id)
    if record.row:
        DB.delete("DELETE FROM favourites WHERE movie_id = %s", id)
        DB.delete("DELETE FROM movies WHERE id = %s", id)
    return jsonify({"message": "Deleted"}), 204
