from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.bookings import Bookings
import repositories.bookings_repository as bookings_repository
import repositories.member_repository as member_repository
import repositories.gym_session_repository as gym_session_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = bookings_repository.select_all() 
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_session():
    members = member_repository.select_all()
    gym_sessions = gym_session_repository.select_all()
    return render_template("bookings/new.html", members = members, gym_sessions = gym_sessions)

@bookings_blueprint.route("/bookings/new",  methods=['POST'])
def create_session():
    member_id = request.form['member_id']
    gym_session_id = request.form['gym_session_id']
    member = member_repository.select(member_id)
    gym_session = gym_session_repository.select(gym_session_id)
    booked_session = Bookings(member, gym_session)
    bookings_repository.save(booked_session)
    return redirect('/bookings')

@bookings_blueprint.route("/bookings/<id>/delete", methods=['POST'])
def delete_booking(id):
    bookings_repository.delete(id)
    return redirect('/bookings')
