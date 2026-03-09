    # Topic 04: Exception Handling

class SecurityError(Exception): pass # Apna chota sa custom error

def run_system():
    try:
        level = int(input("Power Level (1-100): "))
        
        if level < 0 or level > 100:
            raise SecurityError("Invalid Level!") # Apna niyam lagaya
            
        res = 1000 / level
        
    except (ValueError, ZeroDivisionError) as e:
        print(f"[Error] Math ya Input galat hai: {e}")
        
    except SecurityError as e:
        print(f"[Alert] {e}")
        
    else:
        print(f"[Success] System running at {level}%")
        
    finally:
        print("[System] Task Finished.") # Hamesha chalega


run_system()
