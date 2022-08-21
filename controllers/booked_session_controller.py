from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booked_session import BookedSession
import repositories.booked_session_repository as booked_session_repository
import repositories.member_respository as member_repository
import repositories.gym_session_repository as gym_session_repository

booked_session_blueprint = Blueprint("booked_sessions", __name__)