













#print(f"i_hello_0_i .")



# hello_gui.py
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("عرض نص")
    # اجعل النافذة بحجم مناسب ومركزة
    root.geometry("400x150")
    root.resizable(False, False)

    # إظهار النص في وسط النافذة بخط كبير
    label = tk.Label(root, text="i_hello_i", font=("Helvetica", 36, "bold"))
    label.pack(expand=True)

    # زر إغلاق لمن يريد إغلاق النافذة يدوياً
    btn = tk.Button(root, text="إغلاق", command=root.destroy)
    btn.pack(pady=(0,12))

    # ابدأ الحلقة الرئيسية
    root.mainloop()

if __name__ == "__main__":
    main()










