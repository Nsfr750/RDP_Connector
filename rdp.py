import tkinter as tk
from tkinter import messagebox, Button, Tk, Label
import subprocess

class Sponsor:
    
    root = Tk()
    root.geometry("300x200")
    root.title("Sponsor")

    title_label = Label(root, text="Socials", font=("Arial", 16))
    title_label.pack(pady=10)

    def open_patreon():
        import webbrowser
        webbrowser.open("https://www.patreon.com/Nsfr750")

    def open_github():
        import webbrowser
        webbrowser.open("https://github.com/sponsors/Nsfr750")

    def open_discord():    
        import webbrowser
        webbrowser.open("https://discord.gg/q5Pcgrju")
        
    # Create and place buttons
    patreon_button = Button(root, text="Join the Patreon!", command=open_patreon)
    patreon_button.pack(pady=10)

    github_button = Button(root, text="GitHub", command=open_github)
    github_button.pack(pady=10)

    discord_button = Button(root, text="Discord", command=open_discord)
    discord_button.pack(pady=10)

    root.mainloop()

class RDPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RDP Connection App")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="RDP Connection Details").grid(row=0, column=0, columnspan=2)

        tk.Label(self.root, text="IP Address:").grid(row=1, column=0)
        self.ip_entry = tk.Entry(self.root)
        self.ip_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Username:").grid(row=2, column=0)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Password:").grid(row=3, column=0)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Connect", command=self.connect_rdp).grid(row=4, column=0, columnspan=2)

    def connect_rdp(self):
        ip = self.ip_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not ip or not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            subprocess.run(["xfreerdp", f"/v:{ip}", f"/u:{username}", f"/p:{password}"], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to connect to RDP: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = RDPApp(root)
    root.mainloop()