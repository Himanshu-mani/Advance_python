"""
TOPIC: Advanced Functions (Topic 07)
CONCEPTS: Decorators (*args/**kwargs) and Generators (yield).
DESCRIPTION: Performance and logging system for Diti AI.
"""

import time

# --- DECORATOR: Performance Timer ---
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[Timer] {func.__name__} took {end-start:.4f} seconds.")
        return result
    return wrapper

# --- GENERATOR: Log Streamer ---
def log_generator(logs_list):
    for log in logs_list:
        yield f"Processing: {log}"
        time.sleep(0.5) # Thoda delay real feel ke liye

@timer_decorator
def process_data(data):
    print(f"Diti is analyzing: {data}")

# --- Execution ---
if __name__ == "__main__":
    # 1. Testing Decorator
    process_data("Secret Server Files")

    # 2. Testing Generator
    my_logs = ["Log A", "Log B", "Log C"]
    print("\n--- Streaming Logs ---")
    for l in log_generator(my_logs):
        print(l)