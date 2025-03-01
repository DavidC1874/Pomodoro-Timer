#EN_comment_version

import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.geometry("250x130")
        
        #background color
        self.root.config(bg="#FAF7F0")
        
        #counting down number
        self.timer_text = tk.StringVar()
        self.timer_label = tk.Label(
            root, 
            textvariable=self.timer_text, 
            font=("Comic Sans MS", 24, "bold"), # font
            fg="#4A4947", #text color
            bg="#FAF7F0" #background color
        )
        
        #button to start next round
        self.start_button = tk.Button(
            root, 
            text="Start Next Round", 
            command=self.start_timer, 
            font=("Comic Sans MS", 12, "bold"), #font
            fg="#CE5A67", #text color
            bg="#D8D2C2", #bg color
            activebackground="#B17457" #color when button is clicked
        )
        
        #How many rounds of timer u completed
        self.count_label = tk.Label(
            root, 
            text="Rounds Completed: 0", 
            font=("Comic Sans MS", 14),
            fg="#4A4947",
            bg="#FAF7F0"
        )
        
        #initialize the timer
        self.session_count = 0
        self.running = False
        self.timer_text.set("25:00")
        self.start_timer()

    def countdown(self, t):
        self.timer_label.pack(pady=30)  #show counting
        self.start_button.pack_forget()  #hide button
        self.count_label.pack_forget()  #hide rounds
        
        if t >= 0 and self.running:
            mins, secs = divmod(t, 60)
            self.timer_text.set(f"{mins:02d}:{secs:02d}")
            self.root.after(1000, self.countdown, t - 1) 
        elif self.running:  #when countdown to 0
            self.session_count += 1
            self.count_label.config(text=f"Rounds Completed: {self.session_count}")
            self.timer_label.pack_forget() #hide counting down
            self.count_label.pack(pady=18) #show rounds, pady is the margin
            self.start_button.pack(pady=0) #show button
            self.root.attributes("-topmost", True) #make sure window is at top-most
            
            #after 4 rounds
            if self.session_count % 4 == 0:
                messagebox.showinfo("Long break Reminder", "You've completed four rounds. Take a 30-minute break!")
                self.root.quit()
            else:
                messagebox.showinfo("Pomodoro Reminder", "Time's up! Take a break.")
                self.running = False

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_button.pack_forget()
            self.countdown(25 * 60)  # length of each round
            self.root.attributes("-topmost", False)

# creat window, instancing the class into the window
root = tk.Tk()
pomodoro = PomodoroTimer(root)
root.mainloop()
