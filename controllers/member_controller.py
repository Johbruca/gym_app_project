from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_respository as member_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    gym_sessions = member_repository.gym_sessions(member)
    return render_template("members/show.html", member=member, gym_sessions=gym_sessions)