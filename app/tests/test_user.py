from app import app
from app.api.views import *
from flask import json
import unittest


class TestUSer(unittest.TestCase):
    def setUp(self):
        """
        This method instatiates the flask app for background operations of the no-live-server for testing purposes
        """
        self.app = app.test_client()
    
    def test_if_user_creates_account_successfully(self):
        """
        This method test if error message is returned if user tries to create an account with bad formated data
        """
        response = self.app.post("/api/register", content_type= "application/json", data = json.dumps(dict({
            "name": "Eubule",
            "email": "eubule@gmail.com",
            "password": "eubulE1."
        })))
        self.assertEqual(response.status_code, 201)
        self.assertIn("Successfully Added an account", str(response.data))

    def test_if_user_creates_account_with_invalid_data(self):
        """
        This method test if error message is returned if user tries to create an account with bad formated data
        """
        response = self.app.post("/api/register", content_type= "application/json", data = json.dumps(dict({
            "name": "",
            "email": "eubule@gmail.com",
            "password": "eubulE1."
        })))
        self.assertEqual(response.status_code, 417)
        response = self.app.post("/api/register", content_type= "application/json", data = json.dumps(dict({
            "name": "Mlaba",
            "email": 1,
            "password": "eubulE1."
        })))
        self.assertEqual(response.status_code, 417)
        response = self.app.post("/api/register", content_type= "application/json", data = json.dumps(dict({
            "name": "Rick",
            "email": "eubule@gmailcom",
            "password": "eubulE1."
        })))
        self.assertIn("Invalid email. Email should be of format john12@gmail.com", str(response.data))
    

    def test_return_error_if_try_to_create_account_with_non_dictionary_data(self):
        """
        This method tests if user puts a request with non dictionary data
        """
        response = self.app.post("/api/register", content_type = "application/json", data = "Not json data")
        self.assertEqual(response.status_code, 400)

    def test_return_error_if_one_argument_missing(self):
        """
        This method tests if user puts a request with misssing fields
        """
        response = self.app.post("/api/register", content_type = "application/json", data = json.dumps({
            "name": "Eubule",
            "email": "eubule@gmail.com"
        }))
        self.assertIn("Bad format. Please specify user Name, Email and Password", str(response.data))
    
    def test_return_error_if_user_enter_too_many_arguents(self):
        """
        This method tests if user enters too many arguements
        """
        response = self.app.post("/api/register", content_type = "application/json", data = json.dumps({
            "name": "Eubule",
            "email": "eubule@gmail.com",
            "password": "eubulE1.",
            "username": "Malaba"
        }))
        self.assertEqual(response.status_code, 414)
        self.assertIn("Too many arguments. Only Name, Email and Password are required", str(response.data))
    
    def test_return_error_if_user_enter_invalid_password(self):
        """
        This method tests if user enters invalid password
        """
        response = self.app.post("/api/register", content_type = "application/json", data = json.dumps({
            "name": "Eubule",
            "email": "eubule@gmail.com",
            "password": "eubulE1"
        }))
        self.assertEqual(response.status_code, 417)
    def test_return_error_if_user_email_already_exist(self):
        """
        This method tests if user already exists
        """
        response = self.app.post("/api/register", content_type = "application/json", data = json.dumps({
            "name": "Eubule",
            "email": "eubule@gmail.com",
            "password": "eubulE1."
        }))
        self.assertIn("User with email eubule@gmail.com already exist", str(response.data))

    def test_if_user_successfully_logs_in(self):
        """
        This method tests if user successfully logs in.
        """
        respponse = self.app.post("/api/register", content_type = "application/json", data = json.dumps({
            "name": "Eric",
            "email": "eric@gmail.com",
            "password": "ericE1."
        }))
        response = self.app.post("/api/login", content_type = "application/json", data = json.dumps({
            "email": "eric@gmail.com",
            "password": "ericE1."
        }))
        self.assertEqual(response.status_code, 200)
    
    def test_if_tries_to_log_in_with_wrong_credentials(self):
        """
        This method tests if the user fails to log in with wrong creadentials
        """
        response = self.app.post("/api/login", content_type = "application/json", data = json.dumps({
            "email": "eric@gmail.com",
            "password": "ericE1"
        }))
        self.assertEqual(response.status_code, 403)

    def test_if_user_tries_to_login_with_argument_missing(self):
        """
        This method tests if user puts a request with misssing fields
        """
        response = self.app.post("/api/login", content_type = "application/json", data = json.dumps({
            "email": "eric@gmail.com"
        }))
        self.assertIn("Bad format. Please specify user Email and Password", str(response.data))
    
    def test_if_user_tries_to_log_in_with_too_many_arguents(self):
        """
        This method tests if user enters too many arguements
        """
        response = self.app.post("/api/login", content_type = "application/json", data = json.dumps({
            "name": "Eubule",
            "email": "eubule@gmail.com",
            "password": "eubulE1."
        }))
        self.assertEqual(response.status_code, 414)
        self.assertIn("Too many arguments. Only Email and Password are required", str(response.data))

    
