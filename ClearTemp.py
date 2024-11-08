import os
import shutil
import tempfile
import time

def get_folder_size_and_count(folder_path):
    total_size = 0
    file_count = 0
    dir_count = 0

    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)
        try:
            if os.path.isfile(item_path):
                total_size += os.path.getsize(item_path)
                file_count += 1
            elif os.path.isdir(item_path):
                # Use os.walk to calculate the size of directory contents
                for dirpath, dirnames, filenames in os.walk(item_path):
                    dir_count += len(dirnames)
                    file_count += len(filenames)
                    for file in filenames:
                        file_path = os.path.join(dirpath, file)
                        total_size += os.path.getsize(file_path)
        except Exception as e:
            print(f"Error while calculating size or count for {item_path}!")

    return total_size, file_count, dir_count

def format_size(size):
    # Convert size to a human-readable format
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

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
    
    # Get the size and count of files and directories before deletion
    total_size, file_count, dir_count = get_folder_size_and_count(temp_folder_path)
    
    print(f"Folder size: {format_size(total_size)}")
    print(f"Number of files: {file_count}")
    print(f"Number of directories: {dir_count}")
    
    print("The process will start within 2 seconds...")
    time.sleep(2)

    if not os.path.exists(temp_folder_path):
        print(f"The directory {temp_folder_path} does not exist.")
        return

    for item_name in os.listdir(temp_folder_path):
        item_path = os.path.join(temp_folder_path, item_name)
        try:
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"File removed: {item_path}!")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Directory removed: {item_path}!")
        except Exception as e:
            print(f"Error while deleting {item_path}!")

    print(""" 
 ______   _______  __    _  _______  __  
|      | |       ||  |  | ||       ||  | 
|  _    ||   _   ||   |_| ||    ___||  | 
| | |   ||  | |  ||       ||   |___ |  | 
| |_|   ||  |_|  ||  _    ||    ___||__| 
|       ||       || | |   ||   |___  __  
|______| |_______||_|  |__||_______||__| 
          """)
    print("Exiting...")

temp_folder = tempfile.gettempdir()
clear_temp_folder(temp_folder)
