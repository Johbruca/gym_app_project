import unittest

from models.member import Member
from models.bookings import Bookings
from models.gym_session import GymSession

class GymSession(unittest.TestCase):

    def setUp(self):
        self.gym_session = GymSession("Boxing")

    def test_session_has_name(self):
        self.assertEqual("Yoga", self.gym_session.description)