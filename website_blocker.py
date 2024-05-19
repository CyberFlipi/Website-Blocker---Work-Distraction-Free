#!/usr/bin/env python

import os
import argparse

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
    except Exception as e:
        print(f"An error occurred: {e}")

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
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Block or unblock websites.",
        epilog="Example commands:\n"
               "  website_blocker.py --block www.facebook.com www.twitter.com\n"
               "  website_blocker.py --unblock www.facebook.com www.twitter.com",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("--block", nargs='+', metavar='WEBSITE', help="Block the specified websites.")
    parser.add_argument("--unblock", nargs='+', metavar='WEBSITE', help="Unblock the specified websites.")

    args = parser.parse_args()

    if args.block:
        block_websites(args.block, redirect_ip, hosts_path)
    elif args.unblock:
        unblock_websites(args.unblock, hosts_path)
    else:
        parser.print_help()
