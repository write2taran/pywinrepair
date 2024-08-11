import os
import subprocess
import sys

def create_batch_file(commands):
    # Define the batch file content
    batch_content = '@echo off\n'
    batch_content += 'echo Running commands with elevated privileges...\n'
    for command in commands:
        batch_content += f'{command}\n'
    batch_content += 'pause\n'  # Keep the CMD window open

    # Write the batch file
    batch_file_path = 'elevated_commands.bat'
    with open(batch_file_path, 'w') as batch_file:
        batch_file.write(batch_content)
    
    return batch_file_path

def run_batch_file(batch_file_path):
    # Run the batch file with elevated privileges
    print("Requesting admin privileges to run the batch file...")
    subprocess.run(['powershell', '-Command', f'Start-Process cmd -ArgumentList "/c {batch_file_path}" -Verb runAs'])

if __name__ == "__main__":
    # Define the commands to run
    commands = [
        "sfc /scannow",
    #    "DISM /Online /Cleanup-Image /ScanHealth",
        "DISM /Online /Cleanup-Image /RestoreHealth",
        "del /q/f/s %TEMP%\\*"
    ]

    # Create and run the batch file
    batch_file = create_batch_file(commands)
    run_batch_file(batch_file)
