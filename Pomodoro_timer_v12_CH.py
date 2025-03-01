#CH_version

import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("番茄钟")
        self.root.geometry("250x130")
        
        #背景颜色
        self.root.config(bg="#FAF7F0")
        
        #倒计时
        self.timer_text = tk.StringVar()
        self.timer_label = tk.Label(
            root, 
            textvariable=self.timer_text, 
            font=("Comic Sans MS", 24, "bold"),  #字体
            fg="#4A4947", #文本颜色
            bg="#FAF7F0" #背景色
        )
        
        #下一轮按钮
        self.start_button = tk.Button(
            root, 
            text="开始下一个番茄钟", 
            command=self.start_timer, 
            font=("Comic Sans MS", 12, "bold"), #字体
            fg="#CE5A67", #文字颜色
            bg="#D8D2C2", #背景色
            activebackground="#B17457" #按钮按下时颜色
        )
        
        #计时数
        self.count_label = tk.Label(
            root, 
            text="累计次数: 0", 
            font=("Comic Sans MS", 14),
            fg="#4A4947",
            bg="#FAF7F0"
        )
        
        #初始化钟
        self.session_count = 0
        self.running = False
        self.timer_text.set("25:00")
        self.start_timer()

    def countdown(self, t):
        self.timer_label.pack(pady=30)  # 计时开始时显示时间，并向下移动
        self.start_button.pack_forget()  #隐藏按钮
        self.count_label.pack_forget()  #隐藏次数
        
        if t >= 0 and self.running:
            mins, secs = divmod(t, 60)
            self.timer_text.set(f"{mins:02d}:{secs:02d}")  # **更新文本**
            self.root.after(1000, self.countdown, t - 1)  # 1秒后继续
        elif self.running:#倒计时归零后
            self.session_count += 1
            self.count_label.config(text=f"累计次数: {self.session_count}")
            self.timer_label.pack_forget() #隐藏计时文本
            self.count_label.pack(pady=18) #显示累计次数, pady为边距离
            self.start_button.pack(pady=0) #显示按钮
            self.root.attributes("-topmost", True) #确保窗口在最前
            
            #完成四次后
            if self.session_count % 4 == 0:
                messagebox.showinfo("长休息提醒", "完成4个番茄钟，好好休息一下吧！")
                self.root.quit()
            else:
                messagebox.showinfo("番茄钟提醒", "时间到！休息一下吧！")
                self.running = False

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_button.pack_forget()
            self.countdown(25 * 60)  # 启动计时
            self.root.attributes("-topmost", False) #确保窗口不在最前

# 创建窗口
root = tk.Tk()
pomodoro = PomodoroTimer(root)
root.mainloop()
