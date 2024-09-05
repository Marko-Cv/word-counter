import subprocess
import sys
import os

def create_virtualenv(env_name):
    try:
        # Create a virtual environment
        subprocess.run([sys.executable, '-m', 'venv', env_name], check=True)
        print(f"Virtual environment '{env_name}' created successfully.")
        print(f"To activate the virtual environment, run:")

        # Print the command to activate the virtual environment
        if os.name == 'nt':  # For Windows
            print(f"{env_name}\\Scripts\\activate.bat")
        else:  # For Unix or MacOS
            print(f"source {env_name}/bin/activate")

    # Handle errors
    except subprocess.CalledProcessError as e:
        print(f"Failed to create virtual environment '{env_name}': {e}")


if __name__ == "__main__":
    # Get the environment name from a command line prompt
    env_name = input('Enter desired name of your virtual environment: ')

    # Create the virtual environment
    create_virtualenv(env_name)