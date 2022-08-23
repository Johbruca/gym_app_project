from crypt import methods
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_session import GymSession

import repositories.gym_session_repository as gym_session_repository
import repositories.member_repository as member_repository

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

@gym_sessions_blueprint.route("/gym_sessions/<id>/edit", methods=['GET'])
def edit_member(id):
    gym_session = gym_session_repository.select(id)
    members = member_repository.select_all()
    return render_template('gym_sessions/edit.html', gym_session = gym_session, members = members)


@gym_sessions_blueprint.route("/gym_sessions/new",  methods=['GET'])
def new_session():
    gym_session = gym_session_repository.select_all()
    return render_template('gym_sessions/new.html', gym_session=gym_session)


@gym_sessions_blueprint.route("/gym_session/new", methods=['POST'])
def create_session():
    description = request.form['description']
    session = GymSession(description)
    gym_session_repository.save(session)
    return redirect('/gym_sessions')

