from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_respository as member_repository

members_blueprint = Blueprint("members", __name__)