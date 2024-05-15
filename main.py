import os
import subprocess

# This is just the entry point of the app.
# Look for examples directory and files inside it for examples.

def list_python_files(directory):
    """List all Python files in the specified directory, excluding __init__.py."""
    files = [f for f in os.listdir(directory) if f.endswith('.py') and f != '__init__.py']
    return sorted(files)

def select_and_run_file(directory, files):
    """Prompt the user to select a Python file and run it."""
    while True:
        print("\nAvailable examples:")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")

        try:
            choice = int(input("\nPlease enter the number corresponding to the example you wish to execute (or enter 0 to exit): "))
            if choice == 0:
                print("Exiting... Have a great day!")
                break
            elif 1 <= choice <= len(files):
                file_to_run = os.path.join(directory, files[choice - 1])
                print(f"\nExecuting {file_to_run}...\n")
                subprocess.run(["python", file_to_run], check=True)
            else:
                print("Invalid selection. Please choose a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    directory = 'examples'
    if os.path.isdir(directory):
        python_files = list_python_files(directory)
        if python_files:
            select_and_run_file(directory, python_files)
        else:
            print(f"No Python files found in the {directory} directory.")
    else:
        print(f"The directory {directory} does not exist.")
