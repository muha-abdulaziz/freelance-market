import mysql.connector
from mysql.connector import pooling
from ..config import db_host, db_password , db_database , db_user

# Create a connection pool with a max of 5 connections
connection_pool = pooling.MySQLConnectionPool(
    pool_name="freelance_pool",
    pool_size=5,
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

# Function to get a connection from the pool
def get_users():
    conn = connection_pool.get_connection()  # Get a connection from the pool
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    cursor.close()
    conn.close()  # Release connection back to the pool
    return result
