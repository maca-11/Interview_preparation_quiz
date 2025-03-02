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
        # クイズデータの初期化
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
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewQuizApp(root)
    root.mainloop()