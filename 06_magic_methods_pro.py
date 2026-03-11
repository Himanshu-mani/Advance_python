"""
TOPIC: Magic Methods / Dunders (Topic 06)
CONCEPTS: __str__, __len__, __call__, __getitem__, and __add__
DESCRIPTION: Making custom objects behave like built-in Python types.
"""

class AICore:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def __str__(self):
        return f"AI Entity: {self.name} | Status: Active"

    def __len__(self):
        return len(self.tasks)

    def __call__(self, cmd):
        return f"[Command Received] {self.name} is processing: {cmd}"

    def __getitem__(self, index):
        return self.tasks[index]

    # BONUS: __add__ (Adding two AI memories together)
    def __add__(self, other_tasks):
        if isinstance(other_tasks, list):
            self.tasks.extend(other_tasks)
            return f"Memory Updated. New task count: {len(self.tasks)}"

# --- Execution ---
if __name__ == "__main__":
    ai = AICore("ai", ["Coding", "Gym"])
    
    print(ai)                       # __str__
    print(f"Tasks: {len(ai)}")      # __len__
    print(ai("Run Security Scan"))  # __call__
    print(f"First Task: {ai[0]}")   # __getitem__
    
    # Adding new tasks using + operator
    print(ai + ["LeetCode", "Reading"]) # __add__