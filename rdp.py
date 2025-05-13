import tkinter as tk
from tkinter import messagebox, Button, Tk, Label
import subprocess

class Sponsor:
    
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x200")
        self.root.title("Sponsor")
        self.setup_gui()

    def setup_gui(self):
        self.title_label = Label(self.root, text="Socials", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.patreon_button = Button(self.root, text="Join the Patreon!", command=self.open_patreon)
        self.patreon_button.pack(pady=10)

        self.github_button = Button(self.root, text="GitHub", command=self.open_github)
        self.github_button.pack(pady=10)

        self.discord_button = Button(self.root, text="Discord", command=self.open_discord)
        self.discord_button.pack(pady=10)

    def open_patreon(self):
        import webbrowser
        webbrowser.open("https://www.patreon.com/Nsfr750")

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/sponsors/Nsfr750")

    def open_discord(self):    
        import webbrowser
        webbrowser.open("https://discord.gg/q5Pcgrju")

    def run(self):
        self.root.mainloop()

class RDPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RDP 1.0")

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)
        self.root.config(menu=menubar)

    def show_about(self):
        messagebox.showinfo("About", "RDP 1.0\nBy Nsfr750\nConnect to RDP sessions easily.")

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