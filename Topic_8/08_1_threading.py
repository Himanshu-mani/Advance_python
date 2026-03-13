import threading
import time

# Function to simulate Diti's background listening
def diti_listener():
    print("[Diti] Background Listener started...")
    while True:
        # Simulating waiting for a voice command
        time.sleep(4)
        print("\n[Diti] Still listening in background... Speak whenever you want.")

# Main function for other tasks
def main_task():
    for i in range(1, 6):
        print(f"[System] Diti is processing your files... Step {i}")
        time.sleep(1)

if __name__ == "__main__":
    # Create the thread
    listener_thread = threading.Thread(target=diti_listener)
    
    # Daemon means it will close automatically when the main program stops
    listener_thread.daemon = True
    
    # Start the thread
    listener_thread.start()

    # Run the main task
    main_task()
    print("[System] Main tasks completed. Listener thread will stop now.")