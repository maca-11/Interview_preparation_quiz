import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
import os
import random
import time

class InterviewQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("面接対策クイズ")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        self.current_user = {}
        self.quiz_data = []
        self.current_quiz = None
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_id = None
        
        self.initialize_data_files()
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_start_screen()