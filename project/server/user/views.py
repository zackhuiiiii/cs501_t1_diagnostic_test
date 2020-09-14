# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

user_blueprint = Blueprint('auth', __name__)

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
    	user=db.session.query(User).all()
    	list1=[]
    	for x in user:
            y=x.email
            list1.append(y)
        return jsonify({'user':list1}),201


# define the API resources
registration_view = RegisterAPI.as_view('register_api')

# add Rules for API Endpoints
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST', 'GET']
)
