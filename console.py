import pdb

from models.member import Member
import repositories.member_respository as member_repository

from models.session import Session
import repositories.session_repository as session_repository

from models.member_in_session import MemberInSession
import repositories.member_in_session_repository as member_in_session_repository



member_repository.delete_all()
session_repository.delete_all()
member_in_session_repository.delete_all()


member1 = Member('Ona Madorell')
member_repository.save(member1)

member2 = Member('Cindy Potgieter')
member_repository.save(member2)

member3 = Member('Nick Parker')
member_repository.save(member3)

session1 = Session('Spinning')
session_repository.save(session1)

session2 = Session('Yoga')
session_repository.save(session2)

session3 = Session('Boxing')
session_repository.save(session3)

member_in_session1 = MemberInSession(member3, session2)
member_in_session_repository.save(member_in_session1)

member_in_session2 = MemberInSession(member2, session2)
member_in_session_repository.save(member_in_session2)

member_in_session3 = MemberInSession(member1, session3)
member_in_session_repository.save(member_in_session3)

pdb.set_trace()