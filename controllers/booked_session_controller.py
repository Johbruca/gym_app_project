from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booked_session import BookedSession
import repositories.booked_session_repository as booked_session_repository
import repositories.member_respository as member_repository
import repositories.gym_session_repository as gym_session_repository

booked_sessions_blueprint = Blueprint("booked_sessions", __name__)

@booked_sessions_blueprint.route("/booked_sessions")
def booked_sessions():
    booked_sessions = booked_session_repository.select_all() 
    return render_template("booked_session/index.html", booked_sessions = booked_sessions)

