import multiprocessing
import time

# A heavy CPU-bound task
def compute_heavy_data(n):
    print(f"[Core] Starting calculation for Task {n}...")
    # Simulating a heavy mathematical task
    time.sleep(2)
    return n * n

if __name__ == "__main__":
    tasks = [10, 20, 30, 40]

    print(f"[System] Utilizing {multiprocessing.cpu_count()} CPU cores...")
    
    start_time = time.time()
    
    # Use Pool to distribute tasks across CPU cores
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_heavy_data, tasks)

    end_time = time.time()
    
    print(f"\n[System] All heavy tasks finished in: {end_time - start_time:.2f} seconds")
    print(f"[System] Results: {results}")