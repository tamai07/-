import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت هزینه شخصی")

        self.expenses = []  

    
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        ttk.Label(frame, text="مبلغ:").grid(row=0, column=0)
        self.amount_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.amount_var).grid(row=0, column=1)

        ttk.Label(frame, text="دسته‌بندی:").grid(row=1, column=0)
        self.category_var = tk.StringVar()
        categories = ['خوراک', 'حمل‌ونقل', 'تفریح', 'خرید','بدهی' ,'سایر']
        ttk.Combobox(frame, textvariable=self.category_var, values=categories).grid(row=1, column=1)
        self.category_var.set(categories[0])

        ttk.Label(frame, text="توضیح:").grid(row=2, column=0)
        self.desc_var = tk.StringVar()
        ttk.Entry(frame, textvariable=self.desc_var).grid(row=2, column=1)

        ttk.Button(frame, text="اضافه کردن هزینه", command=self.add_expense).grid(row=3, column=0, columnspan=2, pady=5)

        
        self.tree = ttk.Treeview(root, columns=('Amount', 'Category', 'Description'), show='headings')
        self.tree.heading('Amount', text='مبلغ')
        self.tree.heading('Category', text='دسته‌بندی')
        self.tree.heading('Description', text='توضیح')
        self.tree.pack()

        
        self.total_label = ttk.Label(root, text="مجموع هزینه‌ها: 0")
        self.total_label.pack(pady=5)

    def add_expense(self):
        try:
            amount = float(self.amount_var.get())
        except ValueError:
            messagebox.showerror("خطا", "مبلغ باید عدد باشد!")
            return

        category = self.category_var.get()
        description = self.desc_var.get()

        self.expenses.append((amount, category, description))

        self.tree.insert('', tk.END, values=(amount, category, description))
        self.update_total()

        
        self.amount_var.set('')
        self.desc_var.set('')

    def update_total(self):
        total = sum(exp[0] for exp in self.expenses)
        self.total_label.config(text=f"مجموع هزینه‌ها: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
