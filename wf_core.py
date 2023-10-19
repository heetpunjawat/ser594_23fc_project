import subprocess

def execute_files():
    # List of Python files to be executed in order
    file_paths = ['wf_dataprocessing.py', 'wf_visualization.py']

    for file_path in file_paths:
        try:
            # Run the Python file using subprocess
            subprocess.run(['python3', file_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {file_path}: {e}")
            break

if __name__ == "__main__":
    execute_files()
