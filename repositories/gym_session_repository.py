from db.run_sql import run_sql

from models.gym_session import GymSession
from models.member import Member

def save(session):
    sql = "INSERT INTO gym_sessions(name) VALUES ( %s ) RETURNING id"
    values = [session.name]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session

def select_all():
    gym_sessions = []

    sql = "SELECT * FROM gym_sessions"
    results = run_sql(sql)

    for row in results:
        gym_session = GymSession(row['name'], row['id'])
        gym_sessions.append(gym_session)
    return gym_sessions

def delete_all():
    sql = "DELETE FROM gym_sessions"
    run_sql(sql)