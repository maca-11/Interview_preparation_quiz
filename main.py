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

    def show_profile_screen(self):
        self.clear_main_frame()
        
        title_label = tk.Label(self.main_frame, text="プロフィール設定", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)
        
        form_frame = tk.Frame(self.main_frame)
        form_frame.pack(pady=10)
        
        name_label = tk.Label(form_frame, text="名前:")
        name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        industry_label = tk.Label(form_frame, text="業界:")
        industry_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.industry_var = tk.StringVar()
        industry_combo = ttk.Combobox(form_frame, textvariable=self.industry_var, width=27)
        industry_combo['values'] = ("IT", "金融", "製造", "小売", "その他")
        industry_combo.current(0)
        industry_combo.grid(row=1, column=1, padx=10, pady=5)
        
        difficulty_label = tk.Label(form_frame, text="難易度:")
        difficulty_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("基本")
        basic_radio = tk.Radiobutton(form_frame, text="基本", variable=self.difficulty_var, value="基本")
        basic_radio.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        advanced_radio = tk.Radiobutton(form_frame, text="応用", variable=self.difficulty_var, value="応用")
        advanced_radio.grid(row=3, column=1, sticky="w", padx=10, pady=5)
        
        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        save_button = tk.Button(button_frame, text="保存", width=15, height=2,
                              command=self.save_profile)
        save_button.grid(row=0, column=0, padx=10, pady=10)
        
        back_button = tk.Button(button_frame, text="戻る", width=15, height=2,
                             command=self.show_start_screen)
        back_button.grid(row=0, column=1, padx=10, pady=10)

    def save_profile(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("エラー", "名前を入力してください")
            return
        
        self.current_user = {
            "name": name,
            "industry": self.industry_var.get(),
            "difficulty": self.difficulty_var.get()
        }
        
        messagebox.showinfo("成功", "プロフィールを保存しました")
        self.show_start_screen()  

    def start_quiz(self):
        if not hasattr(self, 'current_user') or not self.current_user:
            self.current_user = {
                "name": "ゲスト",
                "industry": "IT",
                "difficulty": "基本"
            }
        
        filtered_quizzes = [q for q in self.quiz_data if q["industry"] == self.current_user["industry"] and
                           q["difficulty"] == self.current_user["difficulty"]]
        
        if not filtered_quizzes:
            messagebox.showerror("エラー", "条件に合うクイズがありません")
            return
        
        self.current_quiz = random.choice(filtered_quizzes)
        self.show_question_screen()
        
    def show_question_screen(self):
        self.clear_main_frame()
        
        # タイトル
        title_label = tk.Label(self.main_frame, text="問題表示画面", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        card_frame = tk.Frame(self.main_frame, bd=2, relief=tk.GROOVE, bg="white")
        card_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        question_block = tk.Frame(card_frame, bg="white")
        question_block.pack(fill=tk.X, padx=20, pady=10)
        
        question_label = tk.Label(question_block, text="面接官からの質問", bg="#F0F0F0", 
                               font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        question_label.pack(fill=tk.X)
        
        question_content = tk.Label(question_block, text=self.current_quiz["question"], 
                                 font=("Helvetica", 14), wraplength=500, bg="white", anchor="w")
        question_content.pack(fill=tk.X, pady=5)
        
        desc_block = tk.Frame(card_frame, bg="#FFE4B5")
        desc_block.pack(fill=tk.X, padx=20, pady=10)
        
        desc_label = tk.Label(desc_block, text="説明イメージ", 
                           font=("Helvetica", 12), bg="#FFE4B5", anchor="center")
        desc_label.pack(pady=5)
        
        desc_content = tk.Label(desc_block, text=self.current_quiz["description"],
                             wraplength=500, bg="#FFE4B5", fg="black")
        desc_content.pack(pady=10)
        
        keywords_block = tk.Frame(card_frame, bg="white")
        keywords_block.pack(fill=tk.X, padx=20, pady=10)
        
        keywords_label = tk.Label(keywords_block, text="記憶すべきキーワード", bg="#F0F0F0",
                               font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        keywords_label.pack(fill=tk.X)
        
        keywords_text = ", ".join(self.current_quiz["keywords"])
        keywords_display = tk.Label(keywords_block, text=keywords_text, fg="blue", 
                                 wraplength=500, bg="white")
        keywords_display.pack(pady=5, fill=tk.X)
        
        timer_block = tk.Frame(card_frame, bg="white")
        timer_block.pack(fill=tk.X, padx=20, pady=10)
        
        timer_label = tk.Label(timer_block, text="タイマー", bg="#F0F0F0",
                            font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        timer_label.pack(fill=tk.X)
        
        self.timer_label = tk.Label(timer_block, text="キーワードを記憶してください (5秒)", 
                                  fg="red", bg="white")
        self.timer_label.pack(pady=5, fill=tk.X)
        
        button_block = tk.Frame(card_frame, bg="white")
        button_block.pack(fill=tk.X, padx=20, pady=10)
        
        self.answer_button = tk.Button(button_block, text="回答する", bg="#4169E1", fg="white",
                                     font=("Helvetica", 12, "bold"), width=20, height=1,
                                     state=tk.DISABLED, command=self.show_answer_screen)
        self.answer_button.pack(pady=10)
        
        self.timer_seconds = 5
        self.update_timer()
    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_label.config(text=f"キーワードを記憶してください ({self.timer_seconds}秒)")
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="時間切れ！回答を始めてください")
            for widget in self.main_frame.winfo_children():
                if isinstance(widget, tk.Frame) and any(isinstance(child, tk.Label) and child.cget("fg") == "blue" for child in widget.winfo_children()):
                    widget.pack_forget()
            self.answer_button.config(state=tk.NORMAL)

    def show_answer_screen(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        
        self.clear_main_frame()
        
        title_label = tk.Label(self.main_frame, text="回答入力画面", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        card_frame = tk.Frame(self.main_frame, bd=2, relief=tk.GROOVE, bg="white")
        card_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        question_block = tk.Frame(card_frame, bg="white")
        question_block.pack(fill=tk.X, padx=20, pady=10)
        
        question_label = tk.Label(question_block, text="質問内容（複製用）", bg="#F0F0F0", 
                               font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        question_label.pack(fill=tk.X)
        
        question_content = tk.Label(question_block, text=self.current_quiz["question"], 
                                 font=("Helvetica", 12), wraplength=500, bg="white")
        question_content.pack(pady=5, fill=tk.X)
        
        answer_block = tk.Frame(card_frame, bg="white")
        answer_block.pack(fill=tk.X, padx=20, pady=10)
        
        answer_label = tk.Label(answer_block, text="回答入力エリア", bg="#F0F0F0",
                             font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        answer_label.pack(fill=tk.X)
        
        self.answer_text = scrolledtext.ScrolledText(answer_block, width=50, height=8)
        self.answer_text.pack(pady=10, fill=tk.BOTH, expand=True)
        
        timer_block = tk.Frame(card_frame, bg="white")
        timer_block.pack(fill=tk.X, padx=20, pady=10)
        
        timer_label = tk.Label(timer_block, text="残り時間", bg="#F0F0F0",
                            font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        timer_label.pack(fill=tk.X)
        
        self.answer_timer_label = tk.Label(timer_block, text="60秒", fg="red", bg="white")
        self.answer_timer_label.pack(pady=5)
        
        button_block = tk.Frame(card_frame, bg="white")
        button_block.pack(fill=tk.X, padx=20, pady=10)
        
        submit_button = tk.Button(button_block, text="回答を送信", bg="#4169E1", fg="white",
                               font=("Helvetica", 12, "bold"), width=20, height=1,
                               command=self.evaluate_answer)
        submit_button.pack(pady=10)
        
        self.timer_seconds = 180
        self.update_answer_timer()

    def update_answer_timer(self):
        if self.timer_seconds > 0:
            self.answer_timer_label.config(text=f"{self.timer_seconds}秒")
            self.timer_seconds -= 1
            self.timer_id = self.root.after(1000, self.update_answer_timer)
        else:
            messagebox.showinfo("時間切れ", "回答時間が終了しました")
            self.evaluate_answer()
    
    def evaluate_answer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        
        answer_text = self.answer_text.get("1.0", tk.END).strip().lower()
        
        keyword_count = 0
        used_keywords = []
        
        for keyword in self.current_quiz["keywords"]:
            if keyword.lower() in answer_text:
                keyword_count += 1
                used_keywords.append(keyword)
        
        match_rate = (keyword_count / len(self.current_quiz["keywords"])) * 100
        
        self.show_result_screen(match_rate, used_keywords)
    
    def show_result_screen(self, match_rate, used_keywords):
        self.clear_main_frame()
        
        title_label = tk.Label(self.main_frame, text="結果・フィードバック画面", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        card_frame = tk.Frame(self.main_frame, bd=2, relief=tk.GROOVE, bg="white")
        card_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        summary_block = tk.Frame(card_frame, bg="white")
        summary_block.pack(fill=tk.X, padx=20, pady=10)
        
        summary_label = tk.Label(summary_block, text="質問と回答の要約", bg="#F0F0F0", 
                              font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        summary_label.pack(fill=tk.X)
        
        question_text = f"質問: {self.current_quiz['question']}\n"
        question_content = tk.Label(summary_block, text=question_text, 
                                 wraplength=500, bg="white", justify="left", anchor="w")
        question_content.pack(fill=tk.X, pady=5, padx=5)
        
        score_feedback_row = tk.Frame(card_frame, bg="white")
        score_feedback_row.pack(fill=tk.X, padx=20, pady=10)
        score_feedback_row.grid_columnconfigure(0, weight=1)
        score_feedback_row.grid_columnconfigure(1, weight=2)
        
        score_block = tk.Frame(score_feedback_row, bg="white", bd=1, relief=tk.GROOVE)
        score_block.grid(row=0, column=0, padx=5, sticky="nsew")
        
        score_title = tk.Label(score_block, text="スコア", bg="#F0F0F0", 
                            font=("Helvetica", 12), anchor="w", padx=10, pady=5)
        score_title.pack(fill=tk.X)
        
        score_value = tk.Label(score_block, text=f"{match_rate:.1f}%", 
                            font=("Helvetica", 18, "bold"), fg="blue", bg="white")
        score_value.pack(pady=20, fill=tk.X)
        
        feedback_block = tk.Frame(score_feedback_row, bg="white", bd=1, relief=tk.GROOVE)
        feedback_block.grid(row=0, column=1, padx=5, sticky="nsew")
        
        feedback_title = tk.Label(feedback_block, text="フィードバックコメント", bg="#F0F0F0", 
                               font=("Helvetica", 12), anchor="w", padx=10, pady=5)
        feedback_title.pack(fill=tk.X)
        
        if match_rate >= 80:
            feedback_text = "素晴らしい！多くのキーワードを使用できています。"
        elif match_rate >= 60:
            feedback_text = "良い回答です。もう少しキーワードを意識しましょう。"
        elif match_rate >= 40:
            feedback_text = "まずまずの回答です。もっとキーワードを使うよう意識しましょう。"
        else:
            feedback_text = "キーワードの使用が少なめです。意識して練習しましょう。"
        
        feedback_content = tk.Label(feedback_block, text=feedback_text, 
                                 wraplength=250, bg="white", justify="left")
        feedback_content.pack(pady=10, padx=10, fill=tk.X)
        
        keywords_block = tk.Frame(card_frame, bg="white")
        keywords_block.pack(fill=tk.X, padx=20, pady=10)
        
        keywords_label = tk.Label(keywords_block, text="使用キーワードハイライト", bg="#F0F0F0", 
                               font=("Helvetica", 12), width=50, anchor="w", padx=10, pady=5)
        keywords_label.pack(fill=tk.X)
        
        keywords_content = tk.Frame(keywords_block, bg="white")
        keywords_content.pack(fill=tk.X, pady=5)
        
        used_text = "使用したキーワード: "
        if used_keywords:
            used_text += ", ".join(used_keywords)
        else:
            used_text += "なし"
        
        used_keywords_label = tk.Label(keywords_content, text=used_text, fg="blue", 
                                    wraplength=500, bg="white", justify="left", anchor="w")
        used_keywords_label.pack(fill=tk.X, pady=5, padx=5)
        
        unused_keywords = [k for k in self.current_quiz["keywords"] if k not in used_keywords]
        unused_text = "未使用キーワード: "
        if unused_keywords:
            unused_text += ", ".join(unused_keywords)
        else:
            unused_text += "なし"
        
        unused_keywords_label = tk.Label(keywords_content, text=unused_text, fg="red", 
                                     wraplength=500, bg="white", justify="left", anchor="w")
        unused_keywords_label.pack(fill=tk.X, pady=5, padx=5)
        
        button_block = tk.Frame(card_frame, bg="white")
        button_block.pack(fill=tk.X, padx=20, pady=10)
        
        next_button = tk.Button(button_block, text="次の問題へ", bg="#4169E1", fg="white",
                             font=("Helvetica", 12, "bold"), width=20, height=1,
                             command=self.start_quiz)
        next_button.pack(pady=10)
        
        menu_link = tk.Label(button_block, text="メニューに戻る", fg="blue", cursor="hand2", bg="white")
        menu_link.pack(pady=5)
        menu_link.bind("<Button-1>", lambda e: self.show_start_screen())

            
if __name__ == "__main__":
    root = tk.Tk()
    app = InterviewQuizApp(root)
    root.mainloop()