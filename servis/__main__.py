from servis import app
from servis.pages import pages
from importlib import import_module
from dotenv import load_dotenv
from os import environ

load_dotenv()

for page in pages:
    import_module("servis.pages." + page)
    
if __name__ == "__main__":
    app.run(host=environ.get("IP", "127.0.0.1"), port=int(environ.get("PORT", 8080)))