import os
import subprocess

def generate_requirements():
    backend_dir = 'backend'
    os.chdir(backend_dir)
    requirements_path = os.path.join(backend_dir, 'requirements.txt')
    
    if not os.path.exists(requirements_path):
        print("requirements.txt does not exist. Creating a new one.")
    
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    
    with open('requirements.txt', 'w') as f:
        f.write(result.stdout)
    
    print("requirements.txt has been updated.")

def install_requirements():
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

if __name__ == "__main__":
    generate_requirements()
    install_requirements()