import tkinter as tk
from tkinter import ttk, messagebox

def compute_tax_new(income):
    income -= 75000
    if income <= 0:
        return 0
    tax = 0
    if income > 400000:
        tax += min(income, 800000) - 400000
    if income > 800000:
        tax += (min(income, 1200000) - 800000) * 0.05
    if income > 1200000:
        tax += (min(income, 1600000) - 1200000) * 0.10
    if income > 1600000:
        tax += (min(income, 2000000) - 1600000) * 0.15
    if income > 2000000:
        tax += (min(income, 2400000) - 2000000) * 0.20
    if income > 2400000:
        tax += (income - 2400000) * 0.25
    if income <= 1200000:
        tax = max(tax - 60000, 0)
    tax = round(tax * 1.04)
    return tax

def compute_tax_old(income):
    income -= 50000
    if income <= 0:
        return 0
    tax = 0
    if income > 250000:
        tax += (min(income, 500000) - 250000) * 0.05
    if income > 500000:
        tax += (min(income, 1000000) - 500000) * 0.20
    if income > 1000000:
        tax += (income - 1000000) * 0.30
    if income <= 500000:
        tax = max(tax - 12500, 0)
    tax = round(tax * 1.04)
    return tax

def calculate():
    try:
        income = float(entry_income.get())
        if income < 0:
            raise ValueError
        tax_new = compute_tax_new(income)
        tax_old = compute_tax_old(income)
        result_new.set(f"₹ {tax_new:,}")
        result_old.set(f"₹ {tax_old:,}")
        if tax_new < tax_old:
            recommendation.set("✅ New Tax Regime is better for you.")
        elif tax_old < tax_new:
            recommendation.set("✅ Old Tax Regime is better for you.")
        else:
            recommendation.set("Both regimes give the same tax liability.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid annual income.")
        result_new.set("")
        result_old.set("")
        recommendation.set("")

root = tk.Tk()
root.title("India Income Tax Calculator (FY 2026–27)")
root.geometry("500x320")
root.resizable(False, False)

frame = ttk.Frame(root, padding="20")
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Annual Income (₹):", font=("Arial", 12)).grid(row=0, column=0, sticky="w", pady=5)
entry_income = ttk.Entry(frame, font=("Arial", 12))
entry_income.grid(row=0, column=1, pady=5, padx=10)

ttk.Button(frame, text="Calculate Tax", command=calculate).grid(row=1, column=0, columnspan=2, pady=15)

result_new = tk.StringVar()
result_old = tk.StringVar()
recommendation = tk.StringVar()

ttk.Label(frame, text="New Regime Tax:", font=("Arial", 10)).grid(row=2, column=0, sticky="w")
ttk.Label(frame, textvariable=result_new, font=("Arial", 10, "bold"), foreground="blue").grid(row=2, column=1, sticky="w")

ttk.Label(frame, text="Old Regime Tax:", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
ttk.Label(frame, textvariable=result_old, font=("Arial", 10, "bold"), foreground="blue").grid(row=3, column=1, sticky="w")

ttk.Label(frame, textvariable=recommendation, font=("Arial", 10), foreground="green").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()