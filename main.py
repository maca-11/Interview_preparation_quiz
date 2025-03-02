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
        
    def initialize_data_files(self):
        if not os.path.exists("quiz_data.json"):
            default_quiz_data = [
                {
                    "id": 1,
                    "question": "自己PRをお願いします",
                    "description": "自分の強みやスキルをアピールする質問です",
                    "keywords": ["経験", "スキル", "強み", "成果", "貢献"],
                    "industry": "IT",
                    "difficulty": "基本"
                },
                {
                    "id": 2,
                    "question": "あなたの長所と短所を教えてください",
                    "description": "自分を客観的に評価する質問です",
                    "keywords": ["長所", "短所", "克服", "改善", "対策"],
                    "industry": "IT",
                    "difficulty": "基本"
                },
                {
                    "id": 3,
                    "question": "志望動機を教えてください",
                    "description": "なぜこの会社を選んだのかを問う質問です",
                    "keywords": ["興味", "貢献", "成長", "ビジョン", "価値観"],
                    "industry": "IT",
                    "difficulty": "基本"
                },
                {
                    "id": 4,
                    "question": "これまでの業務経験で最も困難だった状況とその対処法を教えてください",
                    "description": "問題解決能力を問う質問です",
                    "keywords": ["課題", "分析", "解決", "協力", "結果"],
                    "industry": "IT",
                    "difficulty": "応用"
                },
                {
                    "id": 5,
                    "question": "5年後にどのようなキャリアを築いていたいですか",
                    "description": "キャリアプランを問う質問です",
                    "keywords": ["目標", "計画", "成長", "スキル", "ビジョン"],
                    "industry": "IT",
                    "difficulty": "応用"
                }
            ]
            with open("quiz_data.json", "w", encoding="utf-8") as f:
                json.dump(default_quiz_data, f, ensure_ascii=False, indent=4)
        
        with open("quiz_data.json", "r", encoding="utf-8") as f:
            self.quiz_data = json.load(f)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    def show_start_screen(self):
        self.clear_main_frame()
        
        title_label = tk.Label(self.main_frame, text="面接対策クイズ", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=20)
        
        description = """
        このアプリは面接でのコミュニケーション能力を向上させるためのものです。
        面接でよく聞かれる質問に対して、キーワードを意識しながら回答する練習ができます。
        """
        desc_label = tk.Label(self.main_frame, text=description, wraplength=400, justify="left")
        desc_label.pack(pady=10)
        
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        profile_button = tk.Button(button_frame, text="プロフィール設定", width=20, height=2,
                                  command=self.show_profile_screen)
        profile_button.grid(row=0, column=0, padx=10, pady=10)
        
        start_button = tk.Button(button_frame, text="クイズ開始", width=20, height=2,
                               command=self.start_quiz)
        start_button.grid(row=0, column=1, padx=10, pady=10)
        
        exit_button = tk.Button(button_frame, text="終了", width=20, height=2,
                              command=self.root.quit)
        exit_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)           
            
if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewQuizApp(root)
    root.mainloop()