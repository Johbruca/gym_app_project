import unittest

from models.member import Member, Mmeber
from models.bookings import Bookings
from models.gym_session import GymSession

class Bookings(unittest.TestCase):

    def setUp(self):
        self.gym_session_1 = GymSession("Spinning")
        self.gym_session_2 = GymSession("Yoga")
        self.gym_session_3 = GymSession("Boxing")

        self.gym_sessions = [self.gym_session_1, self.gym_session_2, self.gym_session_3]

        self.ona = Member("Ona Madorell", )