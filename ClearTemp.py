import os
import shutil
import tempfile
import time

def clear_temp_folder(temp_folder_path):
    print("""
 _______  _______  __   __  _______    _______  ___      _______  _______  ______    _______  ______   
|       ||       ||  |_|  ||       |  |       ||   |    |       ||   _   ||    _ |  |       ||    _ |  
|_     _||    ___||       ||    _  |  |       ||   |    |    ___||  |_|  ||   | ||  |    ___||   | ||  
  |   |  |   |___ |       ||   |_| |  |       ||   |    |   |___ |       ||   |_||_ |   |___ |   |_||_ 
  |   |  |    ___||       ||    ___|  |      _||   |___ |    ___||       ||    __  ||    ___||    __  |
  |   |  |   |___ | ||_|| ||   |      |     |_ |       ||   |___ |   _   ||   |  | ||   |___ |   |  | |
  |___|  |_______||_|   |_||___|      |_______||_______||_______||__| |__||___|  |_||_______||___|  |_|
    """)
    
    print("Temporary folder clearer, By MomorioUHT")
    print("The process will starts within 5 seconds...")
    
    time.sleep(5)
    
    if not os.path.exists(temp_folder_path):
        print(f"The directory {temp_folder_path} does not exist.")
        return

    for item_name in os.listdir(temp_folder_path):
        item_path = os.path.join(temp_folder_path, item_name)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"File removed: {item_path}")

            # Check if it's a directory
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Directory removed: {item_path}")

        except Exception as e:
            print(f"Error while deleting {item_path}")
            
    print(""" 
 ______   _______  __    _  _______  __  
|      | |       ||  |  | ||       ||  | 
|  _    ||   _   ||   |_| ||    ___||  | 
| | |   ||  | |  ||       ||   |___ |  | 
| |_|   ||  |_|  ||  _    ||    ___||__| 
|       ||       || | |   ||   |___  __  
|______| |_______||_|  |__||_______||__| 
          """)
    print("The program will closes in 3 seconds...")
    time.sleep(3)
    print("Exiting...")

temp_folder = tempfile.gettempdir()
clear_temp_folder(temp_folder)
