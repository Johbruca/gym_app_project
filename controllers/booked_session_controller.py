from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booked_session import BookedSession
import repositories.booked_session_repository as booked_session_repository
import repositories.member_repository as member_repository
import repositories.gym_session_repository as gym_session_repository

booked_sessions_blueprint = Blueprint("booked_sessions", __name__)

@booked_sessions_blueprint.route("/booked_sessions")
def booked_sessions():
    booked_sessions = booked_session_repository.select_all() 
    return render_template("booked_session/index.html", booked_sessions = booked_sessions)

@booked_sessions_blueprint.route("/booked_sessions/new", methods=['GET'])
def new_session():
    members = member_repository.select_all()
    gym_sessions = gym_session_repository.select_all()
    return render_template("booked_sessions/new.html", members = members, gym_sessions = gym_sessions)

@booked_sessions_blueprint.route("/booked_sessions/new",  methods=['POST'])
def create_session():
    member_id = request.form['member_id']
    gym_session_id = request.form['gym_session_id']
    member = member_repository.select(member_id)
    gym_session = gym_session_repository.select(gym_session_id)
    booked_session = BookedSession(member, gym_session)
    booked_session_repository.save(booked_session)
    return redirect('/booked_session')

