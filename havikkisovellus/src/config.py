import os

from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    print('File not found!')

DATA_FILENAME = os.getenv("DATA_FILENAME") or "database.sqlite"
ENVIRONMENT = os.getenv("ENVIRONMENT") or "development"
