"""
TOPIC: File I/O (Topic 05)
CONCEPTS: 'with' statement, File Modes (w, a, r), and Line Iteration.
DESCRIPTION: Managing Diti's long-term memory and logs.
"""

def update_memory(new_data):
    # 'a' mode (Append) use kiya taaki purana data delete na ho
    with open("iti_memory.txt", "a") as memory:
        memory.write(new_data + "\n")
    print("[System] Memory logged successfully.")

def read_all_memories():
    print("\n--- 🧠 iti's Memory Bank ---")
    try:
        with open("iti_memory.txt", "r") as memory:
            # Efficiently reading line by line
            for index, line in enumerate(memory, start=1):
                print(f"Log {index}: {line.strip()}")
    except FileNotFoundError:
        print("[Alert] No memory file found. Starting fresh.")
    print("----------------------------\n")

# --- Execution ---
if __name__ == "__main__":
    # 1. User se input lekar memory mein dalna
    user_input = input("iti, aaj kya yaad rakhna hai? ")
    update_memory(user_input)

    # 2. Saari yaadein wapas padhna
    read_all_memories()