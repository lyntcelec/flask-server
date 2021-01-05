from flask_restful import Resource
from flask import flash, request, jsonify
from flask_wtf import FlaskForm
from flask_login import login_required, login_user, logout_user
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    jwt_refresh_token_required,
    get_raw_jwt,
)
from app import db
from app.model import User
from app.middleware import jwt_blacklist


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    password = PasswordField(
        "Password", validators=[DataRequired(), EqualTo("confirm_password")]
    )
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            print("Email is already in use.")
            raise ValidationError("Email is already in use.")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already in use.")


class Register(Resource):
    def post(self):
        ret = {"status": 0, "msg": "success"}
        form = RegistrationForm(csrf_enabled=False)

        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                username=form.username.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                password=form.password.data,
            )

            # add user to the database
            db.session.add(user)
            db.session.commit()
            msg = "You have successfully registered! You may now login."
            flash(msg)
            ret["msg"] = msg
        else:
            ret["status"] = 1
            ret["msg"] = "error"

        return jsonify(ret)


class LoginForm(FlaskForm):
    """
    Form for users to login
    """

    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class Login(Resource):
    def post(self):
        ret = {"status": 0, "msg": "success"}
        form = LoginForm(csrf_enabled=False)
        if form.validate_on_submit():
            # check whether user exists in the database and whether
            # the password entered matches the password in the database
            user = User.query.filter_by(email=form.email.data).first()

            access_token = create_access_token(user.email)
            refresh_token = create_refresh_token(user.email)
            ret["access_token"] = access_token
            ret["refresh_token"] = refresh_token

            if user is not None and user.verify_password(form.password.data):
                # log user in
                login_user(user)

            # when login details are incorrect
            else:
                msg = "Invalid email or password."
                flash(msg)
                ret["status"] = 1
                ret["msg"] = msg

        return jsonify(ret)


class Logout(Resource):
    @jwt_required
    def get(self):
        ret = {"status": 0, "msg": "success"}
        logout_user()

        # Revoked Token
        jwt_blacklist.add(get_raw_jwt()["jti"])

        msg = "You have successfully been logged out."
        flash(msg)
        ret["msg"] = msg
        return jsonify(ret)


class Refresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {"access_token": create_access_token(identity=current_user)}
        return jsonify(ret), 200
