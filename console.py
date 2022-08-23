import pdb

from models.member import Member
import repositories.member_repository as member_repository

from models.gym_session import GymSession
import repositories.gym_session_repository as gym_session_repository

from models.bookings import Bookings
import repositories.bookings_repository as bookings_repository



member_repository.delete_all()
gym_session_repository.delete_all()
bookings_repository.delete_all()


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

booking1 = Bookings(member3, session2)
bookings_repository.save(booking1)

booking2 = Bookings(member2, session2)
bookings_repository.save(booking2)

booking3 = Bookings(member1, session3)
bookings_repository.save(booking3)

pdb.set_trace()