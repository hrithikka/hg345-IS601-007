import os
import sys
# Get the parent directory of the current script (api.py)
CURR_DIR = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
PARENT_DIR = os.path.join(CURR_DIR, "..")  # Go up one level from utils to project folder
sys.path.append(PARENT_DIR)
from dotenv import load_dotenv
import requests
#from movies import movies
from flask import redirect, Blueprint
from sql.db import DB

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/fetch', methods=['GET'])
def fetch_media():

    load_dotenv()

    url = os.getenv("OTT_URL")
    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("RAPIDAPI_HOST")

    querystring = {
        "start_year": "1970",
        "end_year": "2022",
        "min_imdb": "6",
        "max_imdb": "7.8",
        "genre": "horror",
        "language": "english",
        "page": "1"
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": api_host
    }

    response = requests.get(url, headers=headers, params=querystring)

    response = response.json()

    for item in response.get('results', []):
        image_urls = item.get('imageurl')
        if image_urls:
            image_url = image_urls[0]
        else:
            image_url = None
        imdb_id = item.get('imdbid')

        # Check if the record with the same imdb_id already exists
        record = DB.selectOne(
            "SELECT * FROM movies WHERE imdb_id = %s", imdb_id)
        if record.row:
            continue

        # Insert data into the MySQL database
        DB.insertOne(
            "INSERT INTO movies (imageURL, genre, imdb_id, title, imdbrating, released, type, synopsis) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            image_url, ",".join(item.get('genre')), imdb_id, item.get(
                'title'), item.get('imdbrating'),
            item.get('released'), item.get('type'), item.get('synopsis'))

    return redirect("/movies")
