from db.run_sql import run_sql

from models.bookings import Bookings
from models.gym_session import GymSession
from models.member import Member

import repositories.member_repository as member_repository
import repositories.gym_session_repository as gym_session_repository


def save(booking):
    sql = "INSERT INTO bookings ( member_id, gym_session_id ) VALUES ( %s, %s ) RETURNING id"
    values = [booking.member.id, booking.gym_session.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking

def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_session = gym_session_repository.select(row['gym_session_id'])
        booking = Bookings(member, gym_session, row['id'])
        bookings.append(booking)
    return bookings

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def gym_session(booking):
    sql = "SELECT * FROM gym_sessions WHERE id = %s"
    values = [booking.gym_session.id]
    results = run_sql(sql, values)[0]
    gym_session = GymSession(results['description'], results['id'])
    return gym_session

def member(booking):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [booking.member.id]
    results = run_sql(sql, values)[0]
    member = Member(results['name'], results['id'])
    return member

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)