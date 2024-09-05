import subprocess

def install_package(env_name, package_name):
    try:
        # Install the package in the virtual environment
        subprocess.run([f'./{env_name}/bin/pip', 'install', package_name], check=True)
        print(f"Package '{package_name}' installed successfully in virtual environment '{env_name}'.")

    # Handle errors
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name} in virtual environment '{env_name}': {e}")

# List of packages to install
packages = ['python-docx', 'PyPDF2', 'pandas']


if __name__ == "__main__":
    # Get the environment name
    env_name = input('Enter the name of your virtual environment: ')

    # Install packages in the virtual environment
    for package in packages:
        install_package(env_name, package)
