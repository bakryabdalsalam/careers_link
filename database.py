from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
load_dotenv()

db_connection_str = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(db_connection_str, connect_args={'ssl':{'ssl_ca':"/etc/ssl/cert.pem"}})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row)
        return jobs