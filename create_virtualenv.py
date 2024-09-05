import subprocess
import sys
import os

def create_virtualenv(env_name):
    try:
        subprocess.run([sys.executable, '-m', 'venv', env_name], check=True)
        print(f"Virtual environment '{env_name}' created successfully.")
        print(f"To activate the virtual environment, run:")
        if os.name == 'nt':  # For Windows
            print(f"{env_name}\\Scripts\\activate.bat")
        else:  # For Unix or MacOS
            print(f"source {env_name}/bin/activate")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment '{env_name}': {e}")


if __name__ == "__main__":
    # Get the environment name from the command line argument
    if len(sys.argv) < 2:
        print("Usage: python create_virtualenv.py <env_name>")
    else:
        env_name = sys.argv[1]
        create_virtualenv(env_name)