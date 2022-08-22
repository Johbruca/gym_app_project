from db.run_sql import run_sql

from models.booked_session import BookedSession
from models.gym_session import GymSession
from models.member import Member

import repositories.member_repository as member_repository
import repositories.gym_session_repository as gym_session_repository


def save(booked_session):
    sql = "INSERT INTO booked_sessions ( member_id, gym_session_id ) VALUES ( %s, %s ) RETURNING id"
    values = [booked_session.member.id, booked_session.gym_session.id]
    results = run_sql( sql, values )
    booked_session.id = results[0]['id']
    return booked_session

def select_all():
    booked_sessions = []

    sql = "SELECT * FROM booked_sessions"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['user_id'])
        gym_session = gym_session_repository.select(row['gym_session_id'])
        booked_session = BookedSession(member, gym_session, row['id'])
        booked_sessions.append(booked_session)
    return booked_sessions

def delete_all():
    sql = "DELETE FROM booked_sessions"
    run_sql(sql)

def gym_session(booked_session):
    sql = "SELECT * FROM gym_sessions WHERE id = %s"
    values = [booked_session.gym_session.id]
    results = run_sql(sql, values)[0]
    gym_session = GymSession(results['description'], results['id'])
    return gym_session

def member(booked_session):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booked_session.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['name'], results['id'])
    return member