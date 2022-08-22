from db.run_sql import run_sql

from models.gym_session import GymSession
from models.member import Member

def save(session):
    sql = "INSERT INTO gym_sessions(description, duration) VALUES (%s, %s) RETURNING id"
    values = [session.description, session.duration]
    results = run_sql( sql, values )
    session.id = results[0]['id']
    return session

def select_all():
    gym_sessions = []

    sql = "SELECT * FROM gym_sessions"
    results = run_sql(sql)

    for row in results:
        gym_session = GymSession(row['description'], row['duration'], row['id'])
        gym_sessions.append(gym_session)
    return gym_sessions

def delete_all():
    sql = "DELETE FROM gym_sessions"
    run_sql(sql)

def select(id):
    gym_session = None
    sql = "SELECT * FROM gym_sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_session = GymSession(result['description'], result['duration'], result['id'] )
    return gym_session

def members(gym_session):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN booked_sessions ON booked_sessions.member_id = members.id WHERE gym_session_id = %s"
    values = [gym_session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['name'], row['id'])
        members.append(member)

    return members