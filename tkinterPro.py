import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import PostTest

# 함수 정의
def submit_action():
    prompt_text = prompt_entry.get()
    date_text = date_entry.get()
    title_text = title_entry.get()

    try:
        # 날짜 유효성 검사
        date_obj = datetime.strptime(date_text, '%Y-%m-%d')
        date_text = date_obj.strftime('%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
        return

    # 입력값 출력
    print(f"Prompt Text: {prompt_text}")
    print(f"Date: {date_text}")
    print(f"Title Text: {title_text}")

    PostTest.generatePostFile(prompt_text, date_text, title_text)

    # 메시지 박스 띄우기
    messagebox.showinfo("Submitted", f"Prompt: {prompt_text}\nDate: {date_text}\nTitle: {title_text}")

# 윈도우 생성
root = tk.Tk()
root.title("Input Form")

# 레이블과 입력 필드 생성
prompt_label = ttk.Label(root, text="Prompt Text:")
prompt_label.grid(column=0, row=0, padx=10, pady=5)

prompt_entry = ttk.Entry(root, width=30)
prompt_entry.grid(column=1, row=0, padx=10, pady=5)

date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(column=0, row=1, padx=10, pady=5)

date_entry = ttk.Entry(root, width=30)
date_entry.grid(column=1, row=1, padx=10, pady=5)

title_label = ttk.Label(root, text="Title Text:")
title_label.grid(column=0, row=2, padx=10, pady=5)

title_entry = ttk.Entry(root, width=30)
title_entry.grid(column=1, row=2, padx=10, pady=5)

# 제출 버튼 생성
submit_button = ttk.Button(root, text="Submit", command=submit_action)
submit_button.grid(column=0, row=3, columnspan=2, pady=10)

# 메인 루프 실행
root.mainloop()