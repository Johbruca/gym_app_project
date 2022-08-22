import pdb

from models.member import Member
import repositories.member_repository as member_repository

from models.gym_session import GymSession
import repositories.gym_session_repository as gym_session_repository

from models.booked_session import BookedSession
import repositories.booked_session_repository as booked_session_repository



member_repository.delete_all()
gym_session_repository.delete_all()
booked_session_repository.delete_all()


member1 = Member('Ona Madorell')
member_repository.save(member1)

member2 = Member('Cindy Potgieter')
member_repository.save(member2)

member3 = Member('Nick Parker')
member_repository.save(member3)

session1 = GymSession('Spinning')
gym_session_repository.save(session1)

session2 = GymSession('Yoga')
gym_session_repository.save(session2)

session3 = GymSession('Boxing')
gym_session_repository.save(session3)

booked_session1 = BookedSession(member3, session2)
booked_session_repository.save(booked_session1)

booked_session2 = BookedSession(member2, session2)
booked_session_repository.save(booked_session2)

booked_session3 = BookedSession(member1, session3)
booked_session_repository.save(booked_session3)

pdb.set_trace()