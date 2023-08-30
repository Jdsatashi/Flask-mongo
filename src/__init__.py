import os

import dotenv
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

dotenv.load_dotenv()

# add mongo atlas URI to pymongo client
mongo_uri = os.environ.get('MONGO_URI')
mongo_client = MongoClient(mongo_uri)

# Get database name
db = mongo_client.get_database('TestDB')

# Get todo table/collection
todo_table = db.get_collection('todo')

# Get the values using Config
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY'),
)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/test/')
def test():
    try:
        database_list = db.list_collection_names()
        return f"Connected to MongoDB. Available databases: {', '.join(database_list)}"
    except Exception as e:
        return f"Connection failed: {e}"


from . import routes
