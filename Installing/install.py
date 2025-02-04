import subprocess
import sys
import os

def install_requirements():
    try:
        # Ensure pip is installed
        subprocess.check_call([sys.executable, "-m", "ensurepip"])

        # Check if 'requirements.txt' exists in the current directory
        if not os.path.isfile('requirements.txt'):
            print("'requirements.txt' not found. Please make sure it is present.")
            return

        # Install packages from 'requirements.txt'
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

        print("All packages have been installed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing the packages: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
