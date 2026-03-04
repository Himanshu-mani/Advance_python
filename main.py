class JarvisMemory:
    def __init__(self, user_name):
        self.user_name = user_name
        self.tasks = [] # Ye hamara database hai

    def add_task(self, name, priority="Low"):
        self.tasks.append([name, priority])
        print(f"Added: {name}")

    def show_tasks(self):
        print(f"\n{self.user_name}'s Tasks:")
        for i in self.tasks:
            print(f"- {i[0]} [Priority: {i[1]}]")

    def update_priority(self, name, new_p):
        for i in self.tasks:
            if i[0] == name:
                i[1] = new_p
                return True
        return False

    def delete_task(self, name):
        for i in self.tasks:
            if i[0] == name:
                self.tasks.remove(i)
                return True
        return False

    def task_count(self):
        return len(self.tasks) # Sahi syntax: len(list)

# --- Usage ---
my_jarvis = JarvisMemory("Aryan")
my_jarvis.add_task("LeetCode Day 1", "High")
my_jarvis.add_task("Milk", "Low")
my_jarvis.show_tasks()
print(f"Total tasks: {my_jarvis.task_count()}")
