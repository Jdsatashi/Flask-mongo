# Introduction
This is a simple template CRUD of Flask using Mongodb Atlas.
## Setup project
Create virtual env
```sh
virtualenv venv
```
Activate virtual env
- Windows:
```sh
venv\scripts\activate
```
- Linux
```sh
source venv/bin/activate
```
Install packages and libraries
```sh
pip install -r requirements.txt
```
Copy .env.sample or rename it to .env
- Windows:
```sh
copy .env.sample .env
```
- Linux:
```sh
cp .env.sample .env
```
Create SECRET_KEY
```sh
import secrets
secret_key = secrets.token_hex(32)
print("Generated Secret Key:", secret_key)
```
Go to https://cloud.mongodb.com and get connection string

Then fill all the .env file
## Usage
Use
```sh
python3 run.py
```
Or
```sh
flask run
```
# Author
This template was created by Jdsatashi
