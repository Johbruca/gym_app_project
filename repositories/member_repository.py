from db.run_sql import run_sql

from models.gym_session import GymSession
from models.member import Member
from models.bookings import Bookings

def save(member):
    sql = "INSERT INTO members(name) VALUES ( %s ) RETURNING id"
    values = [member.name]
    results = run_sql( sql, values )
    member.id = results[0]['id']
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        user = Member(row['name'], row['id'])
        members.append(user)
    return members

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        member = Member(result['name'], result['id'] )
    return member

def gym_sessions(member):
    gym_sessions = []

    sql = "SELECT gym_sessions.* FROM gym_sessions INNER JOIN bookings ON bookings.gym_session_id = gym_sessions.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_session = GymSession(row['description'], row['id'])
        gym_sessions.append(gym_session)

    return gym_sessions

def update(member):
    sql = "UPDATE members SET name = (%s) WHERE id = %s"
    values = [member.name, member.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE  FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)
