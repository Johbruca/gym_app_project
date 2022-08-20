from db.run_sql import run_sql

from models.members_in_session import MemberInSession
from models.gym_session import GymSession
from models.member import Member

import repositories.member_respository as member_repository
import repositories.gym_session_repository as gym_session_repository


def save(members_in_session):
    sql = "INSERT INTO members_in_session ( member_id, gym_session_id ) VALUES ( %s, %s ) RETURNING id"
    values = [members_in_session.member.id, members_in_session.gym_session.id]
    results = run_sql( sql, values )
    members_in_session.id = results[0]['id']
    return members_in_session

def select_all():
    members_in_sessions = []

    sql = "SELECT * FROM members_in_session"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['user_id'])
        gym_session = gym_session_repository.select(row['gym_session_id'])
        members_in_session = MemberInSession(member, gym_session, row['review'], row['id'])
        members_in_sessions.append(members_in_session)
    return members_in_sessions

def delete_all():
    sql = "DELETE FROM members_in_session"
    run_sql(sql)