from api.validation import *


accounts = []
todo_list = []

class User():
    def add_account(sef, name, email, password):
        """
        This function creates a user account
        """
        if not is_valid_name(name) == "Valid 1":
            return is_valid_name(name)
        if not is_valid_email(email) == "Valid 2":
            return is_valid_email(email)
        if not is_valid_password(password) == "Valid 3":
            return is_valid_password(password)
        if is_existing_user(accounts, email):
            return "User with email {} already exist".format(email)

        account = {
            "name": name,
            "email": email,
            "password": password
        }
        accounts.append(account)
        return "Successfully Added an account"

    def login(self, email, password):
        """
        This function logs in the user given their email and password
        """
        if is_valid_email(email) == "valid 2":
            return is_valid_email(email)
        if is_existing_user(accounts, email) == False:
            return "You do not have an account with {}".format(email)
        if not is_valid_password(password) == "Valid 3":
            return is_valid_password(password)
        passcode = [x for x in accounts if x["email"] == email and x["password"] == password]
        if len(passcode) == 0:
            return "Invalid password. Please enter the correct password"
        return "You have successfully logged in"

class Tasks():
    def view_tasks(self):
        """
        This method Displays the All the tasks i the Todo List
        """
        if len(todo_list) == 0:
            return "It's lonely here. There are no tasks yet"
        return todo_list

    def create_task(self,task):
        """
        This function Creates todo task and appends it to the todo list
        """
        if valid_task(task) != "Valid":
            return valid_task(task)
        todo_task = [x for x in todo_list if x["task"] == task]
        if len(todo_task) != 0:
            return "Task already exist. Input a different task"
        id = len(todo_list) + 1
        todo_item ={
            "id": id,
            "task": task
        }
        # user_todo.append(todo_item)
        todo_list.append(todo_item)
        return "Successfully Created Todo task"

    def delete_task(self, id):
        """
        This function deletes the task given the task id
        """
        if not isinstance(id, int):
            return "Task id must be an integer"
        if len(todo_list) == 0:
            return "Empty Todo List. Nothing to delete"
        todo_item = [x for x in todo_list if x["id"] == id]
        if len(todo_item) == 0:
            return "{} does not exist in the todo list. Please enter an existing id".format(id)
        todo_list.remove(todo_item[0])
        i = 1
        for todo in todo_list:
            todo["id"] = i
            i += 1
        return "Task Number {} successfuly deleted".format(id)

    def mark_as_finished(self, id):
        """
        This function append the string [finished] at the end of a task if finished
        """
        if not isinstance(id, int):
            return "Task id must be an integer"
        if len(todo_list) == 0:
            return "Empty Todo List. No tasks yet"
        todo_item = [x for x in todo_list if x["id"] == id]
        if len(todo_item) == 0:
            return "{} does not exist in the todo list. Please enter an existing id".format(id)
        todo_item = [x for x in todo_list if x["id"] == id]
        if "[Finished]" in todo_item[0]["task"]:
            return "This task was already finished"
        todo_item[0]["task"] += "[Finished]"
        return "Successfully Marked task {} as Finished".format(id)

    def delete_all_tasks(self):
        """
        This function empties the Todo list
        """
        if len(todo_list) == 0:
            return "The Todo list is empty. There is no task Yet"
        
        i = len(todo_list)
        while i > 0:
            todo_list.remove(todo_list[i-1])
            i = len(todo_list)
        return "Successfully emptied Todo list"