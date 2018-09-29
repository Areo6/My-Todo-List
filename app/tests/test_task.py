from app import app
from app.api.views import *
from flask import json
import unittest


class TestTask(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_if_user_successfully_creates_a_task(self):
        """
        This method tests if the user can successfully create a task
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "Planning for the upcoming bootcamp in two weeks"
        }))
        self.assertEqual(response.status_code, 201)
    
    def test_if_task_request_is_wrong(self):
        """
        This method tests if the user does not specify task in the request or too many arguments
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "tasks": "Planning for the upcoming bootcamp in two weeks"
        }))
        self.assertEqual(response.status_code, 400)
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "This is an other task",
            "tasks": "Planning for the upcoming bootcamp in two weeks"
        }))
        self.assertEqual(response.status_code, 414)
    
    def test_if_user_tries_to_add_an_already_existing_task(self):
        """
        This method tests the task already exists
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "Planning for the upcoming bootcamp in two weeks"
        }))
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "Planning for the upcoming bootcamp in two weeks"
        }))
        self.assertIn("Task already exist. Input a different task", str(response.data))
        self.assertEqual(response.status_code, 417)

    def test_if_user_can_view_all_tasks(self):
        """
        This method tests if the user views all tasks
        """
        response = self.app.get("/api/tasks")
        self.assertEqual(response.status_code, 200)

    def test_if_user_can_delete_a_specific_task(self):
        """
        This method tests if the user can successfuly delete a specif task
        """
        response = self.app.delete("/api/tasks/1")
        self.assertTrue("Task Number 1 successfuly deleted", str(response.data))
    
    def test_if_user_tries_to_delete__task_that_does_not_exist(self):
        """
        This method tests if user tries to delete an unexisting task
        """
        response = self.app.delete("/api/tasks/9")
        self.assertEqual(response.status_code, 404)

    def test_return_error_if_user_enters_invalid_task(self):
        """
        This method tests if the user tries to enter an invalid task and return an error
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "a"
        }))
        self.assertEqual(response.status_code, 417)

    def test_if_user_successfully_marked_task_as_finished(self):
        """
        This method tests if the user successfully marks a task as finished
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "This task is marked as "
        }))
        response = self.app.put('/api/tasks/1')
        self.assertEqual(response.status_code, 200)

    def test_if_user_tries_to_mark_an_already_marked_task(self):
        """
        This method tests if the user is trying to mark a marked task
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "This task 2 is marked as "
        }))
        response = self.app.post("/api/tasks", content_type = "application/json", data = json.dumps({
            "task": "This task 3 is marked as "
        }))
        response = self.app.put('/api/tasks/2')
        response = self.app.put('/api/tasks/2')
        self.assertEqual(response.status_code, 417)
        

    def test_if_user_tries_to_mark_an_non_existing_task(self):
        """
        This method tests if error is returned if user tries to mark a task that does not exist
        """
        response = self.app.post("/api/tasks", content_type = "application/json", data = {
            "task": "An other task"
        })
        response = self.app.delete("/api/tasks")
        response = self.app.put("/api/tasks/8")
        self.assertIn("Empty Todo List. No tasks yet", str(response.data))

    def test_if_user_successfully_deletes_all_tasks(self):
        """
        This method tests if user tries to delete all tasks when none exist
        """
        response = self.app.delete("/api/tasks")
        self.assertEqual(response.status_code, 202)
        response = self.app.delete("/api/tasks")
        self.assertEqual(response.status_code, 404)

    def test_if_user_tries_to_delete_all_tasks_when_none_exist(self):
        """
        This method tests if user tries to delete all tasks when none exist
        """
        response = self.app.put("/api/tasks/8")
        self.assertIn("8 does not exist in the todo list. Please enter an existing id", str(response.data))