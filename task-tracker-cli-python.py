import sys
import datetime
import json


class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __repr__(self):
        return f"Task(id={self.id}, description='{self.description}', status='{self.status}', createdAt='{self.createdAt}', updatedAt='{self.updatedAt}')"


def create_task(description):
    description = str(description)
    task = Task(1, description, "pending", datetime.datetime.now(), datetime.datetime.now())
    file = open("tasks.txt", "a")
    file.write(task.__repr__())
    


def delete_task(task_id):
    task_id = input("Enter task ID to delete: ")
    # Logic to delete the task with the given ID

def list_tasks():
    # Logic to list all tasks
    pass

def update_task(task_id, new_description):
    pass

def command_parser():
    n = len(sys.argv)
    file = open("tasks.txt", "a")
    if (sys.argv[1] == "add"):
        
        if len(sys.argv) < 3:
           print("Please provide a task description")
           return 1
        else:
           newDescription = ""
           for i in range(2, (len(sys.argv))):
               newDescription = newDescription + " " + (sys.argv[i])
           create_task(newDescription)
           return 0
        file = open("tasks.txt", "a")
        
        
        
        

n = len(sys.argv)
print(f"Number of arguments: {n}")
command_parser()