import os
from contextlib import contextmanager 

@contextmanager
def export_session(filename): 
    
    print(f"Starting export: {filename}") 

    directory = os.path.dirname(filename)

    if directory:
        os.makedirs(directory, exist_ok=True)
    
    file = open(filename, "w")
    
    try: 
        yield file 

    except Exception as error: 
        print(f"Export failed: {error}") 
        raise 

    finally: 
        file.close() 
        print("Export session closed")