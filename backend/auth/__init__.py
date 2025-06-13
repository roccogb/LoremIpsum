from flask import Flask, Blueprint

auth_bp=Blueprint("auth_bp", __name__)

from . import routes
