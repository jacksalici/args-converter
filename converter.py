#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title carg
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🤖
# @raycast.argument1 { "type": "text", "placeholder": "Placeholder" }
# @raycast.packageName Misc

# Documentation:
# @raycast.description Simple tool to convert Python commands to VS Code launch.json args  
# @raycast.author Jack Salici
# @raycast.authorURL https://github.com/jacksalici/args-converter

import json
import shlex
import sys
import pyperclip

def copy_to_clipboard(text):
    pyperclip.copy(text)

def command_to_launch_json(command_str):
 
    command_str = command_str.replace("\\", "")
    args = shlex.split(command_str)
    
    if args[0].lower() in ('python', 'python3'):
        args = args[1:]
    
    program = args[0]
    args = args[1:]
    
    return args


def main():
    if len(sys.argv) < 2:
        command = input("📥 Enter the Python 🐍 command string: ")
    else:
        command = " ".join(sys.argv[1:])
    
    try:
        launch_config = command_to_launch_json(command)
        print(f"\n🥫 Arguments list: {json.dumps(launch_config)}.\n")
        copy_to_clipboard(json.dumps(launch_config, indent=4))
        print(f"🧃 Parsed and copied 📋 {len(launch_config)} arguments!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
    
    