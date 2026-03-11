"""
TOPIC: Classes and Objects (Topic 01)
CONCEPTS: Class definition, Object instantiation, __init__ constructor, and 'self'.
DESCRIPTION: The foundation of the  AI Assistant.
"""

class AI:
    # 1. Constructor: Jab Object paida hota hai, ye tab chalta hai
    def __init__(self, owner_name, model_type):
        # 'self' ka matlab hai: "Ye wala specific object"
        self.owner = owner_name
        self.model = model_type
        self.is_active = False
        print(f"[System] {self.model} initialized for {self.owner}.")

    # 2. Instance Method: Diti ka ek action
    def activate(self):
        self.is_active = True
        print(f"[Status] {self.model} is now ONLINE. Hello {self.owner}!")

    def get_status(self):
        status = "Active" if self.is_active else "Sleep Mode"
        return f"Current Status: {status}"

# --- Execution Area ---
if __name__ == "__main__":
    # Object creation (Instantiation)
    # Yahan 'my_ai' ek object hai jo DitiBasics ki properties hold karta hai
    my_ai = AI("Himanshu", "AI_01")
    
    print(my_ai.get_status())
    my_ai.activate()
    print(my_ai.get_status())
