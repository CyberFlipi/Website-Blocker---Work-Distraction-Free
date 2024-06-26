#!/usr/bin/env python

import tkinter as tk
from tkinter import messagebox

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
            messagebox.showinfo("Success", "Websites have been blocked successfully.")
    except PermissionError:
        messagebox.showerror("Permission Denied", "Please run this application as an administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def unblock_websites(websites, hosts_path):
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
        with open(hosts_path, 'w') as file:
            for line in lines:
                if not any(website in line for website in websites):
                    file.write(line)
        messagebox.showinfo("Success", "Websites have been unblocked successfully.")
    except PermissionError:
        messagebox.showerror("Permission Denied", "Please run this application as an administrator.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def get_blocked_websites(redirect_ip, hosts_path):
    blocked_websites = []
    try:
        with open(hosts_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(redirect_ip):
                    website = line.split()[1]
                    blocked_websites.append(website)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return blocked_websites

def update_blocked_websites_list():
    blocked_websites = get_blocked_websites(redirect_ip, hosts_path)
    blocked_websites_text.delete(1.0, tk.END)
    if blocked_websites:
        for website in blocked_websites:
            blocked_websites_text.insert(tk.END, website + "\n")
    else:
        blocked_websites_text.insert(tk.END, "No websites are currently blocked.")

def on_block():
    websites = entry_websites.get().split()
    if websites:
        block_websites(websites, redirect_ip, hosts_path)
        update_blocked_websites_list()
    else:
        messagebox.showwarning("Input Error", "Please enter at least one website.")

def on_unblock():
    websites = entry_websites.get().split()
    if websites:
        unblock_websites(websites, hosts_path)
        update_blocked_websites_list()
    else:
        messagebox.showwarning("Input Error", "Please enter at least one website.")

# Dark theme colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
btn_bg_color = "#444444"
btn_fg_color = "#ffffff"
entry_bg_color = "#3e3e3e"
entry_fg_color = "#ffffff"
text_bg_color = "#2e2e2e"
text_fg_color = "#ffffff"

# Create the main window
root = tk.Tk()
root.title("Website Blocker")
root.configure(bg=bg_color)

# Create and place the widgets
frame = tk.Frame(root, padx=10, pady=10, bg=bg_color)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Enter websites (separated by space):", bg=bg_color, fg=fg_color)
label.pack(pady=5)

entry_websites = tk.Entry(frame, width=50, bg=entry_bg_color, fg=entry_fg_color, insertbackground=fg_color)
entry_websites.pack(pady=5)

block_button = tk.Button(frame, text="Block Websites", command=on_block, bg=btn_bg_color, fg=btn_fg_color)
block_button.pack(pady=5)

unblock_button = tk.Button(frame, text="Unblock Websites", command=on_unblock, bg=btn_bg_color, fg=btn_fg_color)
unblock_button.pack(pady=5)

blocked_websites_label = tk.Label(frame, text="Currently Blocked Websites:", bg=bg_color, fg=fg_color)
blocked_websites_label.pack(pady=5)

blocked_websites_text = tk.Text(frame, width=50, height=10, bg=text_bg_color, fg=text_fg_color, state=tk.NORMAL, insertbackground=fg_color)
blocked_websites_text.pack(pady=5)

refresh_button = tk.Button(frame, text="Refresh List", command=update_blocked_websites_list, bg=btn_bg_color, fg=btn_fg_color)
refresh_button.pack(pady=5)

# Initialize the list of blocked websites
update_blocked_websites_list()

# Run the application
root.mainloop()
