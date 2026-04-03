import os
import shutil
import time
import random
import sys
import platform
import subprocess
from datetime import datetime
import pyfiglet

def main():
    print("--Zerminal--")
    print("Popular commands: 'help', 'cm', 'cf', 'saf', 'exit'")

    while True:
        current_path = os.getcwd()
        
        user_input = input(f"{current_path} >> ").strip()
        
        if not user_input:
            continue
        
        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]
        
        if command == "help":
            print("cm  - create map (folder)")
            print("cf  - create file")
            print("sf  - show file (map name)0")
            print("saf - show all folders (Warning: scans whole drive)")
            print("rm  - remove [name]")
            print("update - update a zerminal0")
            print("nup - over update")
            print("si - system info")
            print("read - read text file0")
            print("exit - close terminal")
            
        elif command == "nup":
            print("Update version - 0.0.1")
            print("new command")
            print("all work")
        elif command == "rm":
            remove_item(args)

        elif command == "cm":
            create_folder(args)
            
        elif command == "cf":
            create_file(args)
            
        elif command == "sf":
            print("still working")
            
        elif command == "saf":
            show_all_file(args)
            
        elif command == "si":
            show_system_info()
            
        elif command == "read":
            read_file(args)
            
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print(f"Unknown command: '{command}'. Type 'help' for list of commands.")

def remove_item(args):
    if not args:
        print("Error: you forgette the name")
        return
    
    target = args[0]
    if os.path.isfile(target):
        os.remove(target)
        print(f"file {target} deleted.")
    elif os.path.isdir(target):
        shutil.rmtree(target)
        print(f"Map {target} succes deleted.")
    else:
        print("I dont see.")


def show_all_file(args):
    root_path = args[0] if args else "C:\\" 
    print(f"Scanning {root_path}... This may take a while! Press Ctrl+C to stop.")
    
    try:
        for root, dirs, files in os.walk(root_path):
            for name in dirs:
                print(os.path.join(root, name))
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
    except Exception as e:
        print(f"Error during scan: {e}")

def create_file(args):
    if not args:
        print("Error: cf ??? you need to print a name")
        return
    
    file_name = args[0]
    try:
        with open(file_name, 'x') as f:
            pass 
        print(f"File '{file_name}' created.")
    except FileExistsError:
        print("Error: file already exists")
    except Exception as e:
        print(f"Error: {e}")

def create_folder(args):
    if not args:
        print("Error: cm ??? you need to print a name")
        return
    
    folder_name = args[0]
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")
    except FileExistsError:
        print("Error: map (folder) already exists")
    except Exception as e:
        print(f"Error: {e}")

def show_system_info():
    """Info"""
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"{platform.processor()}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")\
    
def read_file(args):
    """Чтение текстовых файлов"""
    if not args:
        print("Error: I dont see")
        return
    try:
        with open(args[0], 'r', encoding='utf-8') as f:
            print("\n--- Open File ---")
            print(f.read())
            print("------------------------")
    except Exception as e:
        print(f"Error: what? {e}")
        

if __name__ == "__main__":
    main()