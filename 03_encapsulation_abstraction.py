from abc import ABC, abstractmethod

# --- 1. ABSTRACTION (The Rule Book) ---
class SystemProtocol(ABC):
    @abstractmethod
    def verify_security(self):
        """Har system ko ye method implement karna hi padega!"""
        pass

# --- 2. ENCAPSULATION + INHERITANCE ---
class AISecurity(SystemProtocol):
    def __init__(self, admin_name, secret_key):
        self.admin = admin_name       # Public: Sab dekh sakte hain
        self.__secret_key = secret_key # Private: Ekdum secret tijori 🔐

    # Protocol follow kar rahe hain (Abstraction)
    def verify_security(self):
        print(f"[System] Authenticating {self.admin}... Access Verified.")

    # GETTER: Safe tarika key dekhne ka
    @property
    def view_key(self):
        # Hum puri key nahi dikhayenge, sirf last 3 stars dikhayenge
        return f"Key Masked: *****{self.__secret_key[-3:]}"

    # SETTER: Safe tarika key badalne ka with Validation
    @view_key.setter
    def view_key(self, new_key):
        if len(new_key) >= 8:
            self.__secret_key = new_key
            print("[Success] Secret Key updated securely.")
        else:
            print("[Error] Security Alert: Key is too weak (Min 8 chars)!")

# --- 3. EXECUTION BLOCK ---
if __name__ == "__main__":
    # Object banaya
    my_secure_ai = AISecurity("Aryan", "ALPHA_999")

    # Abstraction Check
    my_secure_ai.verify_security()

    # Encapsulation Check (Getter)
    print(my_secure_ai.view_key)

    # Validation Check (Setter)
    my_secure_ai.view_key = "BETA_777"   # Fail (Too short)
    my_secure_ai.view_key = "NEW_SECURE_123" # Pass
    
    print(f"Final Status: {my_secure_ai.view_key}")
