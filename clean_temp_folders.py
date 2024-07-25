import os
import shutil
import time

def delete_contents(folder_path, retries=3, delay=1):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            for attempt in range(retries):
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)  # Remove the file or link
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # Remove the directory and its contents
                    break
                except (OSError, PermissionError) as e:
                    if "being used by another process" in str(e) or "Access is denied" in str(e):
                        print(f"File '{item_path}' is currently in use and will be skipped.")
                        break
                    if attempt < retries - 1:
                        print(f"Error: {e}. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        print(f"Failed to delete '{item_path}' after {retries} attempts.")
                        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred while deleting contents of '{folder_path}': {e}")

if __name__ == "__main__":
    temp_folders = [
        r"C:\Users\MY\AppData\Local\Temp",
        r"C:\Windows\Temp"
    ]
    
    for folder_path in temp_folders:
        if not os.path.exists(folder_path):
            print(f"Error: The specified folder '{folder_path}' does not exist.")
        else:
            delete_contents(folder_path)
