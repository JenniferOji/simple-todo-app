"""Simple TODO list application."""
import json
import os


class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_from_file()

    def add_todo(self, task):
        """Add a new todo item."""
        self.todos.append({'task': task, 'completed': False})
        self.save_to_file()

    def list_todos(self):
        """List all todos."""
        return self.todos

    def save_to_file(self):
        """Save todos to a JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=4)

    def load_from_file(self):
        """Load todos from a JSON file."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_todo("Learn about Jules")
    todo_list.save_to_file()
    print(todo_list.list_todos())
