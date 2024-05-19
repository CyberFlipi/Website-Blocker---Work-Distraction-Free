import os
import sys

# List of websites to block
websites_to_block = [
    "www.facebook.com",
    "facebook.com"
]

# Redirect to localhost
redirect_ip = "127.0.0.1"

# Path to the hosts file on Windows 10
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

def block_websites(websites, redirect_ip, hosts_path):
    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                entry = f"{redirect_ip} {website}\n"
                if entry not in content:
                    file.write(entry)
            print("Websites have been blocked successfully.")
    except PermissionError:
        print("Permission denied: Please run this script as an administrator.")

def unblock_websites(websites, hosts_path):
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        with open(hosts_path, 'w') as file:
            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)
        print("Websites have been unblocked successfully.")
    except PermissionError:
        print("Permission denied: Please run this script as an administrator.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python website_blocker.pt <block|unblock>")
        sys.exit(1)

    action = sys.argv[1].lower()
    if action == "block":
        block_websites(websites_to_block, redirect_ip, hosts_path)
    elif action == "unblock":
        unblock_websites(websites_to_block, hosts_path)
    else:
        print("Invalid action. Use 'block' or 'unblock'.")
        sys.exit(1)