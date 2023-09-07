from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
db_connection_str = os.getenv('DB_CONNECTION_STRING')

engine = create_engine(db_connection_str, connect_args={'ssl': {'ssl_ca': '/etc/ssl/cert.pem'}})

def fetch_data_as_dicts(query, **params):
    with engine.connect() as conn:
        result = conn.execute(text(query), **params)
        rows = result.fetchall()
        column_names = result.keys()
        data_as_dicts = [dict(zip(column_names, row)) for row in rows]
        return data_as_dicts

def load_jobs_from_db():
    query = "SELECT * FROM jobs"
    return fetch_data_as_dicts(query)

def load_job_from_db(id):
    query = "SELECT * FROM jobs WHERE id = :id"
    params = {"id": id}
    
    with engine.connect() as conn:
        result = conn.execute(text(query).params(**params))
        rows = result.fetchall()
        column_names = result.keys()
        data_as_dicts = [dict(zip(column_names, row)) for row in rows]
        
    return data_as_dicts[0] if data_as_dicts else None


# Store data in the database
def add_application_to_db(job_id, data):
    query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url ) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    
    with engine.connect() as conn:
        conn.execute(text(query).params(
            job_id=job_id,
            full_name=data["full_name"],
            email=data["email"],
            linkedin_url=data["linkedin_url"],
            education=data["education"],
            work_experience=data["work_experience"],
            resume_url=data["resume_url"]
        ))
