import os
import shutil
import time
import random
import sys
import platform
import subprocess
from datetime import datetime
import vlc
import pyfiglet
from tkinter import *
from tkinter.ttk import Combobox, Checkbutton, Radiobutton
from tqdm import tqdm

def main():
    print(pyfiglet.figlet_format("Zerminal"))
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
            print("cm     - create folder")
            print("cf     - create file")
            print("sf     - show file (folder name)")
            print("saf    - show all folders (Warning: scans whole drive)")
            print("rm     - remove [name]")
            print("update - update zerminal")
            print("nup    - version info")
            print("si     - system info")
            print("read   - read text file")
            print("exit   - close terminal")
            print("vlc    - launch vlc (video name)")
            print("tf     - test file (py)")
            print("rf     - redact file")
            print("mos    - MiniOS")
            print("ps     - password info")

        elif command == "vlc":
            vlc_launcher(args)

        elif command == "ps":
            print("Zerminal Password System")

        elif command == "nup":
            print("Update version - 0.0.3")
            print("New commands - MOS, rf, tf")
            print("No bug fixes in this version")

        elif command == "rm":
            remove_item(args)

        elif command == "cm":
            create_folder(args)
            
        elif command == "cf":
            create_file(args)
            
        elif command == "sf":
            print("Feature still in development")
            
        elif command == "saf":
            show_all_files(args)
            
        elif command == "si":
            show_system_info()
            
        elif command == "read":
            read_file(args)
            
        elif command == "exit":
            print("Goodbye!")
            break

        elif command == "mos":
            MiniOS(args)

        else:
            print(f"Unknown command: '{command}'. Type 'help' for list of commands.")

def MiniOS(args):
    if not args:
        print("Error: Usage 'mos [name]'")
        return
    
    target = args[0]
    print(f"Initializing {target}...") 
    
    for i in tqdm(range(100), desc="Loading Kernel", unit="%", ascii=True):
        time.sleep(0.02)
        
    window = Tk()
    window.title(f"Zerminal OS - {target}")
    window.geometry("400x250")

    def check_password():
        entered = txt.get()
        if entered == "Zerminal": 
            for widget in window.winfo_children():
                widget.destroy()
            
            window.geometry("600x400")
            Label(window, text=f"Welcome to {target}", font=("Arial", 20)).pack(pady=20)
            Button(window, text="Open Files", command=lambda: print("Files opened")).pack()
            Button(window, text="Shutdown", command=window.destroy).pack(pady=10)
        else:
            lbl_error.config(text="Wrong Password!", fg="red")

    Label(window, text=f"System: {target}", font=("Arial Bold", 14)).pack(pady=10)
    Label(window, text="Enter Password:").pack()
    
    txt = Entry(window, show="*", width=20) 
    txt.pack(pady=5)

    btn = Button(window, text="Login", command=check_password)
    btn.pack(pady=10)

    lbl_error = Label(window, text="")
    lbl_error.pack()

    window.mainloop()

def vlc_launcher(args):
    if not args:
        print("Usage: vlc [filename]")
        return

    video_name = args[0]
    extensions = ['.mp4', '.mkv', '.avi', '.mov', '.flv']
    has_extension = any(video_name.lower().endswith(ext) for ext in extensions)

    print(f"Searching for '{video_name}'...")
    search_root = os.path.expanduser("~")
    found_path = None

    try:
        with tqdm(desc="Scanning directories", unit=" folders", leave=False, ascii=True) as pbar:
            for root, dirs, files in os.walk(search_root):
                pbar.update(1)
                for f in files:
                    if has_extension:
                        if f.lower() == video_name.lower():
                            found_path = os.path.join(root, f)
                            break
                    else:
                        for ext in extensions:
                            if f.lower() == (video_name + ext).lower():
                                found_path = os.path.join(root, f)
                                break
                    if found_path: break
                if found_path: break
                
    except KeyboardInterrupt:
        print("\nSearch stopped by user.")
        return

    if found_path:
        print(f"\nFound: {found_path}")
        if shutil.which("vlc"):
            print("Launching VLC player...")
            subprocess.Popen(["vlc", found_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            print("Error: VLC is not installed. Use 'sudo apt install vlc'")
    else:
        print(f"\nFile '{video_name}' not found in {search_root}")
        
def remove_item(args):
    if not args:
        print("Error: Name required for removal")
        return
    
    target = args[0]
    if os.path.isfile(target):
        os.remove(target)
        print(f"File {target} deleted.")
    elif os.path.isdir(target):
        shutil.rmtree(target)
        print(f"Folder {target} successfully deleted.")
    else:
        print("Item not found.")

def show_all_files(args):
    default_path = "/" if platform.system() != "Windows" else "C:\\"
    root_path = args[0] if args else default_path
    
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
        print("Error: Filename required")
        return
    
    file_name = args[0]
    try:
        with open(file_name, 'x') as f:
            pass 
        print(f"File '{file_name}' created.")
    except FileExistsError:
        print("Error: File already exists")
    except Exception as e:
        print(f"Error: {e}")

def create_folder(args):
    if not args:
        print("Error: Folder name required")
        return
    
    folder_name = args[0]
    try:
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")
    except FileExistsError:
        print("Error: Folder already exists")
    except Exception as e:
        print(f"Error: {e}")

def show_system_info():
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
    
def read_file(args):
    if not args:
        print("Error: No file specified")
        return
    try:
        with open(args[0], 'r', encoding='utf-8') as f:
            print("\n--- File Content ---")
            print(f.read())
            print("--------------------")
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    main()
