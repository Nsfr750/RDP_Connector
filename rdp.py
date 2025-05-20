import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import subprocess
import json
import os
import re
from pathlib import Path
import webbrowser
import threading
from datetime import datetime
from about import About
from sponsor import Sponsor
from version import get_version



class RDPApp:
    CONFIG_FILE = 'rdp_config.json'
    HISTORY_LIMIT = 10

    def __init__(self, root):
        self.root = root
        self.root.title("RDP Connector 2.0")
        self.root.geometry("600x400")
        
        self.config = self.load_config()
        self.history = self.config.get('history', [])
        
        self.create_menu()
        self.create_widgets()
        self.setup_styles()

    def setup_styles(self):
        style = ttk.Style()
        style.configure('RDP.TFrame', padding='10')
        style.configure('RDP.TLabel', padding='5')
        style.configure('RDP.TButton', padding='5')
        style.configure('RDP.TEntry', padding='5')
        style.configure('RDP.TLabelframe', padding='10')

    def load_config(self):
        config_path = Path(self.CONFIG_FILE)
        if config_path.exists():
            try:
                return json.loads(config_path.read_text())
            except json.JSONDecodeError:
                return {}
        return {}

    def save_config(self):
        with open(self.CONFIG_FILE, 'w') as f:
            json.dump(self.config, f, indent=4)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save Connection", command=self.save_connection)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Help menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_about)
        helpmenu.add_command(label="Support", command=self.show_support)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.root.config(menu=menubar)

    def show_support(self):
        sponsor = Sponsor(self.root)
        sponsor.show_sponsor()

    def show_about(self):
        About.show_about(self.root)

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style='RDP.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Connection Details Frame
        details_frame = ttk.LabelFrame(main_frame, text="Connection Details", style='RDP.TLabelframe')
        details_frame.pack(fill='x', pady=(0, 10))

        # Grid layout for connection details
        ttk.Label(details_frame, text="IP Address:", style='RDP.TLabel').grid(row=0, column=0, sticky='e')
        self.ip_entry = ttk.Entry(details_frame, style='RDP.TEntry')
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Username:", style='RDP.TLabel').grid(row=1, column=0, sticky='e')
        self.username_entry = ttk.Entry(details_frame, style='RDP.TEntry')
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(details_frame, text="Password:", style='RDP.TLabel').grid(row=2, column=0, sticky='e')
        self.password_entry = ttk.Entry(details_frame, show="*", style='RDP.TEntry')
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        # Show password button
        self.show_pass_var = tk.BooleanVar()
        show_pass_btn = ttk.Checkbutton(details_frame, text="Show Password",
                                      variable=self.show_pass_var,
                                      command=self.toggle_password_visibility)
        show_pass_btn.grid(row=2, column=2, padx=5, pady=5)

        # Connection History Frame
        history_frame = ttk.LabelFrame(main_frame, text="Connection History", style='RDP.TLabelframe')
        history_frame.pack(fill='both', expand=True, pady=(0, 10))

        self.history_list = tk.Listbox(history_frame, height=5)
        self.history_list.pack(fill='both', expand=True, padx=5, pady=5)
        self.update_history_list()

        # Connect Button
        self.connect_button = ttk.Button(main_frame, text="Connect", 
                                       command=self.connect_rdp,
                                       style='RDP.TButton')
        self.connect_button.pack(pady=10)

        # Status Label
        self.status_label = ttk.Label(main_frame, text="", style='RDP.TLabel')
        self.status_label.pack(pady=5)

    def toggle_password_visibility(self):
        if self.show_pass_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def validate_ip(self, ip):
        pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return bool(re.match(pattern, ip))

    def update_history_list(self):
        self.history_list.delete(0, tk.END)
        for item in self.history[-self.HISTORY_LIMIT:]:
            self.history_list.insert(tk.END, f"{item['ip']} - {item['username']}")

    def save_connection(self):
        ip = self.ip_entry.get()
        username = self.username_entry.get()
        if not ip or not username:
            messagebox.showerror("Error", "IP and Username are required to save")
            return

        if not self.validate_ip(ip):
            messagebox.showerror("Error", "Invalid IP address format")
            return

        self.config['saved_connections'] = self.config.get('saved_connections', [])
        self.config['saved_connections'].append({
            'ip': ip,
            'username': username,
            'last_used': datetime.now().isoformat()
        })
        self.save_config()
        messagebox.showinfo("Success", "Connection saved successfully!")

    def connect_rdp(self):
        ip = self.ip_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not all([ip, username, password]):
            messagebox.showerror("Error", "All fields are required")
            return

        if not self.validate_ip(ip):
            messagebox.showerror("Error", "Invalid IP address format")
            return

        self.status_label.config(text="Connecting...")
        self.connect_button.config(state='disabled')

        # Add to history
        self.history.append({
            'ip': ip,
            'username': username,
            'timestamp': datetime.now().isoformat()
        })
        self.history = self.history[-self.HISTORY_LIMIT:]
        self.config['history'] = self.history
        self.save_config()
        self.update_history_list()

        def rdp_thread():
            try:
                cmd = [
                    "xfreerdp",
                    f"/v:{ip}",
                    f"/u:{username}",
                    f"/p:{password}",
                    "/cert-ignore",  # Ignore certificate errors
                    "/t:RDP Connection"  # Title for the RDP window
                ]
                subprocess.run(cmd, check=True)
                self.status_label.config(text="Connection successful!")
            except subprocess.CalledProcessError as e:
                self.status_label.config(text=f"Error: {str(e)}")
                messagebox.showerror("Connection Error", f"Failed to connect: {str(e)}")
            except Exception as e:
                self.status_label.config(text=f"Error: {str(e)}")
                messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            finally:
                self.connect_button.config(state='normal')

        threading.Thread(target=rdp_thread, daemon=True).start()



if __name__ == "__main__":
    root = tk.Tk()
    app = RDPApp(root)
    root.mainloop()