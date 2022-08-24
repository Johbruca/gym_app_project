import unittest

from models.member import Mmeber
from models.bookings import Bookings
from models.gym_session import GymSession

class Member(unittest.TestCase):

    def setup(self):
        self.member = Member("Ona Madorell")
        self.member = Member("Nick Parker")
        self.member = Member("Cindy Potgieter")

        self.gym_sessions = [self.gym_session_1, self.gym_session_2, self.gym_session_3]

        gym_session = GymSession("Boxing")
        self.member = Member("Ona Madorell", gym_session)


    def test_member_has_name(self):
        self.assertEqual("Ona Madorell", self.member.name)