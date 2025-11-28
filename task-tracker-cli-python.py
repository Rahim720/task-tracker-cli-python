import sys
import datetime


class Task(self, description):
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', status='{self.status}', createdAt='{self.createdAt}', updatedAt='{self.updatedAt}')"


def create_task(description):
    description = input("Enter task description: ")
    task = newTask(description)


def delete_task(task_id):
    task_id = input("Enter task ID to delete: ")
    # Logic to delete the task with the given ID

def list_tasks():
    # Logic to list all tasks
    pass