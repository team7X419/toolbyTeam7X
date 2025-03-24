import os
import sys
import subprocess
import shutil

required_packages = [
    "requests",
    "colorama",
    "user_agent",
    "python-cfonts",
    "pycryptodome"
]

def install_packages(pip_cmd):
    for package in required_packages:
        try:
            subprocess.check_call([pip_cmd, "install", package])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package} using {pip_cmd}")

print("Installing packages for Python 3...")
install_packages("pip")

if shutil.which("pip2"):
    print("Installing packages for Python 2...")
    install_packages("pip2")
else:
    print("pip2 not found, skipping Python 2 installation.")

print("All packages installed successfully!")