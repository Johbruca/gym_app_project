from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.members_in_session import MemberInSession
import repositories.members_in_session_repository as member_in_session_repository
import repositories.member_respository as member_repository
import repositories.gym_session_repository as gym_session_repository

visits_blueprint = Blueprint("members_in_sessions", __name__)