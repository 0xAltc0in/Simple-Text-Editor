#!/usr/bin/env python3

import argparse
import os
import tempfile
import subprocess
import sys
from datetime import datetime

def get_editor():
    """Get the user's preferred text editor"""
    # Try environment variables in order
    for var in ['VISUAL', 'EDITOR']:
        editor = os.environ.get(var)
        if editor:
            return editor
    
    # Default editors based on platform
    if sys.platform.startswith('win'):
        return 'notepad'
    elif sys.platform.startswith('darwin'):
        return 'open -t'
    else:
        # Try common editors on Unix-like systems
        for editor in ['nano', 'vim', 'vi', 'emacs']:
            if subprocess.run(['which', editor], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
                return editor
    
    return 'nano'  # Final fallback

def create_file(file_path, template=None):
    """Create a new text file"""
    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    
    # Check if file already exists
    if os.path.exists(file_path):
        overwrite = input(f"File '{file_path}' already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            print("Operation cancelled.")
            return False
    
    with open(file_path, 'w') as f:
        if template:
            if template == 'blank':
                pass  # Leave file empty
            elif template == 'note':
                f.write(f"# Note created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            elif template == 'todo':
                f.write("# To-Do List\n\n- [ ] Task 1\n- [ ] Task 2\n- [ ] Task 3\n")
            elif template == 'memo':
                f.write(f"MEMO\nDate: {datetime.now().strftime('%Y-%m-%d')}\nSubject: \n\n")
    
    print(f"File created: {file_path}")
    return True

def edit_file(file_path):
    """Open a file in the user's preferred text editor"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        create_new = input("Would you like to create it? (y/n): ")
        if create_new.lower() != 'y':
            return False
        create_file(file_path)
    
    editor = get_editor()
    try:
        subprocess.run(f'{editor} "{file_path}"', shell=True)
        print(f"File edited: {file_path}")
        return True
    except Exception as e:
        print(f"Error opening editor: {e}")
        return False

def view_file(file_path, line_numbers=False):
    """Display the contents of a file"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False
    
    try:
        with open(file_path, 'r') as f:
            content = f.readlines()
        
        print(f"\n--- {file_path} ---\n")
        for i, line in enumerate(content):
            if line_numbers:
                print(f"{i+1:4d} | {line}", end='')
            else:
                print(line, end='')
        print("\n")
        print(f"--- End of file ({len(content)} lines) ---\n")
        return True
    except Exception as e:
        print(f"Error reading file: {e}")
        return False

def get_file_info(file_path):
    """Get information about a file"""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return False
    
    try:
        stats = os.stat(file_path)
        created = datetime.fromtimestamp(stats.st_ctime)
        modified = datetime.fromtimestamp(stats.st_mtime)
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Count lines, words, and characters
        lines = content.count('\n') + (1 if content and not content.endswith('\n') else 0)
        words = len(content.split())
        chars = len(content)
        
        print(f"\nFile Information for: {file_path}")
        print(f"Size: {stats.st_size} bytes")
        print(f"Created: {created.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Modified: {modified.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Characters: {chars}\n")
        return True
    except Exception as e:
        print(f"Error getting file info: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Simple Text Editor")
    
    # Main commands
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Create command
    create_parser = subparsers.add_parser("create", help="Create a new text file")
    create_parser.add_argument("file", help="File path")
    create_parser.add_argument("-t", "--template", choices=["blank", "note", "todo", "memo"],
                              default="blank", help="Template to use")
    
    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit a text file")
    edit_parser.add_argument("file", help="File path")
    
    # View command
    view_parser = subparsers.add_parser("view", help="View a text file")
    view_parser.add_argument("file", help="File path")
    view_parser.add_argument("-n", "--line-numbers", action="store_true", help="Show line numbers")
    
    # Info command
    info_parser = subparsers.add_parser("info", help="Get information about a text file")
    info_parser.add_argument("file", help="File path")
    
    args = parser.parse_args()
    
    if args.command == "create":
        create_file(args.file, args.template)
    
    elif args.command == "edit":
        edit_file(args.file)
    
    elif args.command == "view":
        view_file(args.file, args.line_numbers)
    
    elif args.command == "info":
        get_file_info(args.file)
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
