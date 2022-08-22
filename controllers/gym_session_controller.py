from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_session import GymSession
from repositories.booked_session_repository import gym_session
import repositories.gym_session_repository as gym_session_repository

gym_sessions_blueprint = Blueprint("gym_sessions", __name__)

@gym_sessions_blueprint.route("/gym_sessions")
def gym_sessions():
    gym_sessions = gym_session_repository.select_all() 
    return render_template("gym_sessions/index.html", gym_sessions = gym_sessions)

@gym_sessions_blueprint.route("/gym_sessions/<id>")
def show(id):
    gym_session = gym_session_repository.select(id)
    members = gym_session_repository.members(gym_session)
    return render_template("gym_sessions/show.html", gym_session=gym_session, members=members)

@gym_sessions_blueprint.route("/gym_sessions/<id>", methods=['POST'])
def update_session(id):
    description = request.form['description']
    gym_session = GymSession(description, id)
    gym_session_repository.update(gym_session)
    return redirect('/gym_sessions')