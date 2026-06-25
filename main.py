import tkinter as tk
from tkinter import messagebox
from levels import levels

class FindTheBug:
    def __init__(self, root):
        self.root = root
        self.root.title("FindTheBug")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")

        self.current_level = 0
        self.score = 0
        self.app_widgets = []

        self.show_start_screen()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.app_widgets = []

    def show_start_screen(self):
        self.clear()

        tk.Label(self.root, text="FindTheBug", font=("Arial", 32, "bold"),
                 bg="#1a1a2e", fg="#e94560").pack(pady=60)
        
        tk.Label(self.root, text="Find the bug in each fake app.\n10 levels. Good luck.",
                 font=("Arial", 13), bg="#1a1a2e", fg="#a8a8b3").pack(pady=10)
        
        tk.Button(self.root, text="Start", font=("Arial", 14, "bold"),
                  bg="#e94560", fg="white", relief="flat", padx=30, pady=10,
                  cursor="hand2", command=self.start_game).pack(pady=40)
        
    def start_game(self):
        self.current_level = 0
        self.score = 0
        self.show_level()

    def show_level(self):
        if self.current_level >= len(levels):
            self.show_result_screen()
            return
        
        self.clear()
        level = levels[self.current_level]

        header = tk.Frame(self.root, bg="#16213e", pady=8)
        header.pack(fill="x")

        tk.Label(header, text=f"Level {level['id']}/10",
                 font=("Arial", 11, "bold"), bg="#16213e", fg="white").pack(side="left", padx=15)
        
        colors = {"easy": "#6bcb77", "medium": "#ffd93d", "hard": "#ff6b6b"}
        tk.Label(header, text=level["difficulty"].upper(),
                 font=("Arial", 11, "bold"), bg="#16213e",
                 fg=colors[level["difficulty"]]).pack(side="right", padx=15)
        
        tk.Label(self.root, text=level["description"],
                 font=("Arial", 12), bg="#1a1a2e", fg="#a8a8b3",
                 wraplength=500).pack(pady=15)
        
        app_frame = tk.Frame(self.root, bg="#16213e", relief="ridge", bd=2)
        app_frame.pack(padx=30, fill="both", expand=True, pady=5)

        self.render_app(app_frame, level)

        if level["type"] == "type":
            input_frame = tk.Frame(self.root, bg="#1a1a2e")
            input_frame.pack(pady=10)

            self.answer_input = tk.Entry(input_frame, font=("Arial", 12),
                                         width=30, bg="#16213e", fg="white",
                                         insertbackground="white", relief="flat")
            self.answer_input.pack(side="left", padx=5, ipady=6)

            tk.Button(input_frame, text="Submit", font=("Arial", 11, "bold"),
                      bg="#e94560", fg="white", relief="flat", padx=15,
                      cursor="hand2", command=self.submit_type_answer).pack(side="left")
    
    def render_app(self, frame, level):
        app = level["app"]

        if app == "login":
            self.render_login(frame, level)
        elif app == "calculator":
            self.render_calculator(frame, level)
        elif app == "signup":
            self.render_signup(frame, level)
        elif app == "timer":
            self.render_timer(frame, level)
        elif app == "cart":
            self.render_cart(frame, level)
        elif app == "signup2":
            self.render_signup2(frame, level)
        elif app == "progress":
            self.render_progress(frame, level)
        elif app == "login2":
            self.render_login2(frame, level)
        elif app == "volume":
            self.render_volume(frame, level)
        elif app == "darkmode":
            self.render_darkmode(frame, level)

    def correct(self):
        self.score += 1
        messagebox.showinfo("Correct!", f"Good find!\n\nBug: {levels[self.current_level]['bug_text']}")
        self.current_level += 1
        self.show_level()

    def wrong(self):
        messagebox.showerror("Wrong!", "Thats not the bug. Look more carefully!")

    def skip(self):
        messagebox.showinfo("Skipped", f"The bug was:\n{levels[self.current_level]['bug_text']}")
        self.current_level += 1
        self.show_level()

    def submit_type_answer(self):
        answer = self.answer_input.get().lower()
        level = levels[self.current_level]
        if any(keyword in answer for keyword in level["keywords"]):
            self.correct()
        else:
            self.wrong()

    def render_login(self, frame, level):
        tk.Label(frame, text="Login", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=15)
        tk.Label(frame, text="Username", bg="#16213e", fg="#a8a8b3").pack()
        tk.Entry(frame, font=("Arial", 11), bg="#1a1a2e", fg="white",
                 insertbackground="white", relief="flat").pack(pady=5, ipady=5)
        tk.Label(frame, text="Password", bg="#16213e", fg="#a8a8b3").pack()
        tk.Entry(frame, font=("Arial", 11), bg="#1a1a2e", fg="white",
                 insertbackground="white", relief="flat", show="*").pack(pady=5, ipady=5)
        
        btn = tk.Button(frame, text="Logout", font=("Arial", 12, "bold"),
                        bg="#e94560", fg="white", relief="flat", padx=20, pady=6,
                        cursor="hand2",
                        command=lambda: self.check_click("login_btn", level))
        btn.pack(pady=15)

        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    
    def render_calculator(self, frame, level):
        tk.Label(frame, text="Calculator", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        tk.Label(frame, text="2 + 2 = 5", font=("Arial", 28, "bold"),
                 bg="#16213e", fg="#e94560").pack(pady=20)
        tk.Label(frame, text="Type whats wrong below",
                 bg="#16213e", fg="#a8a8b3").pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack(pady=10)
        
    def render_signup(self, frame, level):
        tk.Label(frame, text="Shop", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        tk.Label(frame, text="Premium Plan", font=("Arial", 13),
                 bg="#16213e", fg="white").pack()
        price = tk.Label(frame, text="Price: -$9.99", font=("Arial", 10, "bold"),
                         bg="#16213e", fg="#6bcb77", cursor="hand2")
        price.pack(pady=10)
        price.bind("<Button-1>", lambda e: self.check_click("price_label", level))
        tk.Button(frame, text="Buy Now", font=("Arial", 12),
                  bg="#e94560", fg="white", relief="flat", padx=20,
                  command=lambda: self.check_click("buy_btn", level)).pack(pady=10)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    def render_timer(self, frame, level):
        tk.Label(frame, text="Countdown Timer", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        self.timer_val = 0
        self.timer_label = tk.Label(frame, text="0", font=("Arial", 40, "bold"),
                                    bg="#16213e", fg="white")
        self.timer_label.pack(pady=10)
        tk.Button(frame, text="Start Timer", font=("Arial", 12),
                  bg="#e94560", fg="white", relief="flat", padx=20,
                  command=self.run_timer).pack(pady=5)
        tk.Label(frame, text="Type whats wrong below",
                 bg="#16213e", fg="#a8a8b3").pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    def run_timer(self):
        if not hasattr(self, 'timer_label') or not self.timer_label.winfo_exists():
            return
        self.timer_val += 1
        self.timer_label.config(text=str(self.timer_val))
        self.root.after(1000, self.run_timer)

    def render_cart(self, frame, level):
        tk.Label(frame, text="Shopping Cart", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        tk.Label(frame, text="Item 1 - $10.00", bg="#16213e", fg="white",
                 font=("Arial", 12)).pack()
        tk.Label(frame, text="Item 2 - $5.00", bg="#16213e", fg="white",
                 font=("Arial", 12)).pack(pady=5)
        total = tk.Label(frame, text="Total: $9.00", font=("Arial", 16, "bold"),
                         bg="#16213e", fg="#e94560", cursor="hand2")
        total.pack(pady=5)
        total.bind("<Button-1>", lambda e: self.check_click("total_label", level))
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack(pady=5)
        
    def render_signup2(self, frame, level):
        tk.Label(frame, text="Sign Up", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        tk.Label(frame, text="Password", bg="#16213e", fg="#a8a8b3").pack()
        self.pass_entry = tk.Entry(frame, font=("Arial", 11), bg="#1a1a2e",
                                   fg="white", insertbackground="white",
                                   relief="flat", show="*")
        self.pass_entry.pack(pady=5, ipady=5)
        tk.Button(frame, text="Sign Up", font=("Arial", 12),
                  bg="#e94560", fg="white", relief="flat", padx=20,
                  command=self.check_signup2).pack(pady=10)
        tk.Label(frame, text="Type whats wrong below",
                    bg="#16213e", fg="#a8a8b3").pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
        
    def check_signup2(self):
        password = self.pass_entry.get()
        messagebox.showinfo("Signed up!", "Account created successfully!")

    def render_progress(self, frame, level):
        tk.Label(frame, text="Uploading...", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        self.progress_val = 100
        self.progress_label = tk.Label(frame, text="100%", font=("Arial", 20),
                                       bg="#16213e", fg="white")
        self.progress_label.pack()
        self.progress_bar_frame = tk.Frame(frame, bg="#1a1a2e", width=400, height=20)
        self.progress_bar_frame.pack(pady=5)
        self.progress_bar_frame.pack_propagate(False)
        self.progress_bar_fill = tk.Frame(self.progress_bar_frame, bg="#e94560",
                                          width=400, height=20)
        self.progress_bar_fill.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        tk.Button(frame, text="Start", font=("Arial", 12),
                  bg="#e94560", fg="white", relief="flat", padx=20,
                  command=self.run_progress).pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9), 
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    def run_progress(self):
        if self.progress_val > 0:
            self.progress_val -= 1
            self.progress_label.config(text=f"{100 - self.progress_val}%")
            self.progress_bar_fill.place(relwidth=self.progress_val / 100)
            self.root.after(50, self.run_progress)

    def render_login2(self, frame, level):
        tk.Label(frame, text="Login", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=15)
        tk.Label(frame, text="Password", bg="#16213e", fg="#a8a8b3").pack()
        tk.Entry(frame, font=("Arial", 11), bg="#1a1a2e", fg="white",
                 insertbackground="white", relief="flat").pack(pady=5, ipady=5)
        tk.Label(frame, text="Type whats wrong below",
                 bg="#16213e", fg="#a8a8b3").pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    def render_volume(self, frame, level):
        tk.Label(frame, text="Volume", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        self.vol_label = tk.Label(frame, text="Volume: 0", font=("Arial", 14),
                                  bg="#16213e", fg="white", cursor="hand2")
        self.vol_label.pack(pady=5)
        self.vol_label.bind("<Button-1>", lambda e: self.check_click("volume_label", level))
        slider = tk.Scale(frame, from_=0, to=10, orient="horizontal",
                          bg="#16213e", fg="white", highlightthickness=0,
                          troughcolor="#1a1a2e", length=300,
                          command=self.update_volume)
        slider.pack(pady=10)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    
    def update_volume(self, val):
        display_val = int(val) * 10
        self.vol_label.config(text=f"Volume: {display_val}")

    def render_darkmode(self, frame, level):
        self.dark_on = False
        self.dm_frame = frame
        tk.Label(frame, text="Settings", font=("Arial", 16, "bold"),
                 bg="#16213e", fg="white").pack(pady=10)
        self.dm_label = tk.Label(frame, text="Dark Mode: OFF", font=("Arial", 13),
                                 bg="#16213e", fg="white")
        self.dm_label.pack(pady=5)
        tk.Button(frame, text="Toggle Dark Mode", font=("Arial", 12),
                  bg="#e94560", fg="white", relief="flat", padx=20,
                  command=self.toggle_dark).pack(pady=10)
        tk.Label(frame, text="Type whats wrong below",
                 bg="#16213e", fg="#a8a8b3").pack(pady=5)
        tk.Button(frame, text="Skip", font=("Arial", 9),
                  bg="#16213e", fg="#a8a8b3", relief="flat",
                  cursor="hand2", command=self.skip).pack()
        
    def toggle_dark(self):
        self.dark_on = not self.dark_on
        if self.dark_on:
            self.dm_frame.configure(bg="#ffffff")
            self.dm_label.configure(text="Dark Mode: ON", bg="#ffffff", fg="#000000")
        else:
            self.dm_frame.configure(bg="#16213e")
            self.dm_label.configure(text="Dark Mode: OFF", bg="#16213e", fg="white")

    
    def check_click(self, element, level):
        if element == level["bug_element"]:
            self.correct()
        else:
            self.wrong()

    def show_result_screen(self):
        self.clear()
        tk.Label(self.root, text="Done!", font=("Arial", 32, "bold"),
                 bg="#1a1a2e", fg="#e94560").pack(pady=40)
        tk.Label(self.root, text=f"You found {self.score}/10 bugs",
                 font=("Arial", 16), bg="#1a1a2e", fg="white").pack(pady=10)
        
        if self.score >= 8:
            comment = "You are basically a QA engineer."
        elif self.score >= 5:
            comment = "Not bad. Some bugs slipped past you though."
        else:
            comment = "The bugs found you instead."

        tk.Label(self.root, text=comment, font=("Arial", 13),
                 bg="#1a1a2e", fg="#a8a8b3").pack(pady=10)
        tk.Button(self.root, text="Play Again", font=("Arial", 14, "bold"),
                  bg="#e94560", fg="white", relief="flat", padx=30, pady=10,
                  cursor="hand2", command=self.show_start_screen).pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = FindTheBug(root)
    root.mainloop()