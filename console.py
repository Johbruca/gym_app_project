import pdb

from models.member import Member
import repositories.member_respository as member_repository

from models.gym_session import GymSession
import repositories.gym_session_repository as gym_session_repository

from models.members_in_session import MemberInSession
import repositories.members_in_session_repository as members_in_session_repository



member_repository.delete_all()
gym_session_repository.delete_all()
members_in_session_repository.delete_all()


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

member_in_session1 = MemberInSession(member3, session2)
members_in_session_repository.save(member_in_session1)

member_in_session2 = MemberInSession(member2, session2)
members_in_session_repository.save(member_in_session2)

member_in_session3 = MemberInSession(member1, session3)
members_in_session_repository.save(member_in_session3)

pdb.set_trace()