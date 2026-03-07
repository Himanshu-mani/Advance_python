"""
TOPIC: OOPs Foundations (Topic 01)
PROJECT: Jarvis Memory System
CONCEPTS: Class, Object, Constructor (__init__), Self, Methods, List Operations.
DESCRIPTION: Demonstrates basic memory management for a user assistant using OOPs.
"""

class JarvisMemory:
    """The Blueprint for storing and managing user-specific tasks."""
    
    def __init__(self, user_name):
        """
        CONSTRUCTOR: Initializes the user's name and an empty database (list).
        'self' refers to the specific instance of the memory being created.
        """
        self.user_name = user_name
        self.tasks = []  # Instance Variable: Acts as a temporary database

    def add_task(self, name, priority="Low"):
        """METHOD: Appends a new task with its priority to the list."""
        self.tasks.append([name, priority])
        print(f"[Success] Added task: {name}")

    def show_tasks(self):
        """METHOD: Iterates through the list to display all stored tasks."""
        print(f"\n--- {self.user_name.upper()}'S TASK LIST ---")
        if not self.tasks:
            print("No tasks found.")
        else:
            for i in self.tasks:
                print(f"• {i[0]} | Priority: {i[1]}")

    def update_priority(self, name, new_p):
        """METHOD: Searches for a task and updates its priority level."""
        for i in self.tasks:
            if i[0] == name:
                i[1] = new_p
                print(f"[Update] '{name}' priority changed to {new_p}")
                return True
        print(f"[Error] Task '{name}' not found.")
        return False

    def delete_task(self, name):
        """METHOD: Finds a specific task and removes it from the memory."""
        for i in self.tasks:
            if i[0] == name:
                self.tasks.remove(i)
                print(f"[Delete] Task '{name}' has been removed.")
                return True
        print(f"[Error] Could not delete. Task '{name}' not found.")
        return False

    def task_count(self):
        """METHOD: Returns the total number of tasks using len()."""
        return len(self.tasks)

# --- PROFESSIONAL USAGE BLOCK ---
if __name__ == "__main__":
    # Creating an Object (Instance) of the JarvisMemory Class
    my_jarvis = JarvisMemory("Aryan")

    # Performing Operations (CRUD)
    my_jarvis.add_task("LeetCode Day 1 Challenge", "High")
    my_jarvis.add_task("Buy Milk & Groceries", "Low")
    my_jarvis.add_task("Study OOPs Inheritance", "Critical")

    my_jarvis.show_tasks()

    # Testing Update and Delete
    my_jarvis.update_priority("Milk", "Medium") # This will fail because name is 'Buy Milk...'
    my_jarvis.delete_task("Buy Milk & Groceries")

    print(f"\nTotal Active Tasks: {my_jarvis.task_count()}")
