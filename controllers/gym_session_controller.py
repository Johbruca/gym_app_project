from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_session import GymSession
import repositories.gym_session_repository as gym_session_repository

gym_sessions_blueprint = Blueprint("gym_sessions", __name__)