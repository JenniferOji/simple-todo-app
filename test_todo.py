import unittest
import os
import json
from todo import TodoList

class TestTodoListPersistence(unittest.TestCase):

    def setUp(self):
        self.filename = "test_todos.json"
        # Ensure the file does not exist before each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def tearDown(self):
        # Clean up the file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load_file(self):
        # 1. Test saving and loading
        todo_list = TodoList(self.filename)
        todo_list.add_todo("Task 1")
        todo_list.add_todo("Task 2")

        # Manually save to ensure file is written
        todo_list.save_to_file()

        new_todo_list = TodoList(self.filename)
        self.assertEqual(len(new_todo_list.todos), 2)
        self.assertEqual(new_todo_list.todos[0]['task'], "Task 1")

    def test_load_file_not_found(self):
        # 2. Test FileNotFoundError handling
        todo_list = TodoList("non_existent_file.json")
        self.assertEqual(todo_list.todos, [])

    def test_load_invalid_json(self):
        # 3. Test invalid JSON handling
        with open(self.filename, 'w') as f:
            f.write("invalid json")

        todo_list = TodoList(self.filename)
        self.assertEqual(todo_list.todos, [])

    def test_autosave_on_add(self):
        # 4. Test autosaving on add_todo
        todo_list = TodoList(self.filename)
        todo_list.add_todo("Task 1")

        # Verify by loading into a new instance
        new_todo_list = TodoList(self.filename)
        self.assertEqual(len(new_todo_list.todos), 1)
        self.assertEqual(new_todo_list.todos[0]['task'], "Task 1")

if __name__ == '__main__':
    unittest.main()
