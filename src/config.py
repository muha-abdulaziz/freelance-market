from dotenv import load_dotenv
import os

load_dotenv()

# Access environment variables using os.environ
secret_key = os.environ.get('SECRET_KEY')
database_url = os.environ.get('DATABASE_URL')
db_host=os.getenv("MYSQL_HOST"),
db_user=os.getenv("MYSQL_USER"),
db_password=os.getenv("MYSQL_PASSWORD"),
db_database=os.getenv("MYSQL_DB")