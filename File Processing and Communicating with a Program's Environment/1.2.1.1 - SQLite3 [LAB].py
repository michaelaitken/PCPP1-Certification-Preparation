"""
Objectives

    improving the student's skills in interacting with the SQLite database;
    using known methods of the Cursor object.

Scenario

Our TODO application requires you to add a little security and display the data saved in the database. Your task is to implement the following functionalities:

    Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
    Block the ability to enter an empty task (the name cannot be an empty string).
    Block the ability to enter a task priority less than 1.
    Use the find_task method to block the ability to enter a task with the same name.
    Create a method called show_tasks, responsible for displaying all tasks saved in the database.
"""

import sqlite3


class Todo:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("todo.db")
        self.c = self.conn.cursor()
        self.__create_task_table()
        
    def __create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL
        );''')
    
    def __get_task_name(self, displayed_message: str) -> str:
        """Get name from user and validate. Return valid name."""
        while True:
            valid_name = input(displayed_message).strip()
            
            name_exists = False
            for row in self.c.execute('SELECT * FROM tasks'):
                if row[1] == valid_name:
                    name_exists = True
            
            if valid_name == '':
                print("Task name cannot be blank.")
            elif name_exists:
                print("Task already exists.")
            else:
                break
            
        return valid_name
    
    def __get_task_priority(self, displayed_message: str) -> int:
        """Get priority from user and validate. Return valid priority."""
        while True:
            try:
                valid_priority = int(input(displayed_message).strip())
                if valid_priority < 1 or valid_priority > 5:
                    print("Priority must be between 1 and 5.")
                else:
                    break
            except ValueError:
                print("Priority must be a number.")
        
        return valid_priority
            
    
    def add_task(self):
        """Add a new task to the database"""
        name = self.__get_task_name('Enter task name: ')
        priority = self.__get_task_priority('Enter task priority: ')

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
        
    def show_tasks(self):
        """Display all the tasks in the database"""
        for row in self.c.execute('SELECT * FROM tasks'):
            print("[{}] : {}".format(row[2], row[1]))
    
    def find_task(self, task_name: str) -> tuple | None:
        for row in self.c.execute('SELECT * FROM tasks'):
            if row[1] == task_name:
                return row
        return None


# === TESTING ===

app = Todo()
app.show_tasks()
app.add_task()
app.show_tasks()
    