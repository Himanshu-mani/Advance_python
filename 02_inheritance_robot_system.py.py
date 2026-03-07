"""
FILE: multi_robot_system.py
TOPIC: Advanced OOPs (Inheritance, Polymorphism, MRO, Magic Methods)
PROJECT: Multi-Robot Management System (Part of Diti AI Ecosystem)
"""

class Component:
    """Base Class: Essential hardware functionality."""
    def status(self):
        print("[System] Component is functional.")

class Battery:
    """Independent Class: Manages energy systems (Multiple Inheritance support)."""
    def power_info(self):
        print("[Power] Source: Lithium-ion Battery Pack.")

class Robot(Component):
    """
    Primary Class: Demonstrates Single Inheritance & Operator Overloading.
    """
    def __init__(self, version):
        self.version = version
        self.task_completed = 0

    def status(self):
        # super() ensures Parent's functionality isn't lost
        super().status()
        print(f"[Robot] Version {self.version} is online and active.")

    def __add__(self, other):
        """Operator Overloading: Adds tasks between two Robot instances."""
        if isinstance(other, Robot):
            return self.task_completed + other.task_completed
        return "Error: You can only add another Robot!"

class Drone(Robot, Battery):
    """Multiple Inheritance: Inherits from both Robot and Battery."""
    def fly(self):
        print("[Action] Drone is engaging aerial propulsion.")

class GroundBot(Robot):
    """Hierarchical Inheritance: Derived from the same Parent (Robot)."""
    def move(self):
        print("[Action] GroundBot is moving on heavy-duty wheels.")

class HybridBot(Drone, GroundBot):
    """
    Diamond Problem Case: Solved using Python's Method Resolution Order (MRO).
    """
    pass

# --- Testing Block ---
if __name__ == "__main__":
    print("--- 🤖 Robot System Initialized ---")
    
    # Testing HybridBot & MRO
    hb = HybridBot("v1.0-Alpha")
    hb.status() 
    
    print("\n--- 🔍 MRO Path (Diamond Problem Solution) ---")
    for idx, path in enumerate(HybridBot.mro()):
        print(f"Step {idx}: {path}")

    print("\n--- ➕ Testing Operator Overloading ---")
    scout = Robot("Scout-X")
    guard = Robot("Guard-Y")
    
    scout.task_completed = 15
    guard.task_completed = 25
    
    print(f"Total Team Workload: {scout + guard} tasks")