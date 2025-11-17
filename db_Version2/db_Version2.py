import mysql.connector
from config import DB_CONFIG

def conectar():
    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"],
        autocommit=False
    )

def fetchall_dict(query, params=None):
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute(query, params or ())
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows

def fetchone_dict(query, params=None):
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute(query, params or ())
    row = cur.fetchone()
    cur.close()
    con.close()
    return row

def execute(query, params=None):
    con = conectar()
    cur = con.cursor()
    cur.execute(query, params or ())
    con.commit()
    lastrowid = cur.lastrowid
    cur.close()
    con.close()
    return lastrowid