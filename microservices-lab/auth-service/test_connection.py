import os
from dotenv import load_dotenv
import psycopg2
import redis
import sys

load_dotenv()  # carga .env si existe

PG_USER = os.getenv("POSTGRES_USER", "devuser")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD", "devpass")
PG_DB = os.getenv("POSTGRES_DB", "main_db")
PG_HOST = os.getenv("POSTGRES_HOST", "postgres")  # en docker-compose el servicio se llama postgres
PG_PORT = os.getenv("POSTGRES_PORT", "5432")

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def test_postgres():
    try:
        conn = psycopg2.connect(
            dbname=PG_DB, user=PG_USER, password=PG_PASSWORD, host=PG_HOST, port=PG_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        r = cur.fetchone()
        cur.close()
        conn.close()
        print("POSTGRES: OK -> SELECT 1 returned:", r)
        return True
    except Exception as e:
        print("POSTGRES: ERROR ->", e)
        return False

def test_redis():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=5)
        r.set("micro_lab_test_key", "ok", ex=10)
        v = r.get("micro_lab_test_key")
        print("REDIS: OK -> value:", v)
        return True
    except Exception as e:
        print("REDIS: ERROR ->", e)
        return False

if __name__ == "__main__":
    pg_ok = test_postgres()
    redis_ok = test_redis()
    if pg_ok and redis_ok:
        print("CONEXIONES: OK")
        sys.exit(0)
    else:
        print("CONEXIONES: FALLARON")
        sys.exit(1)
