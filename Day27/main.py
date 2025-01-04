import tkinter as tk

result = 0
convert = "metric to imp"
def calculate():
    global result
    if convert == "metric to imp":
        x = user_input.get()
        formula = float(x) * 1.60934
        result = round(formula, 2)
        show_result = tk.Label(text=result)
        show_result.grid(row=2, column=2)
        show_unit = tk.Label(text=result)
        show_unit.grid(row=2, column=2)
    elif convert == "imp to metric":
        x = user_input.get()
        formula = float(x) * 0.621371
        result = round(formula, 2)
        show_result = tk.Label(text=result)
        show_result.grid(row=2, column=2)
def switch():
    global convert
    if convert == "metric to imp":
        kg_label = tk.Label(text="Km")
        kg_label.grid(row=0, column=3)
        mi_label = tk.Label(text="Mi")
        mi_label.grid(row=2, column=3)
        convert = "imp to metric"
    elif convert == "imp to metric":
        kg_label = tk.Label(text="Km")
        kg_label.grid(row=2, column=3)
        mi_label = tk.Label(text="Mi")
        mi_label.grid(row=0, column=3)
        convert = "metric to imp"

root = tk.Tk()
root.title("Gui Program")
root.minsize(200, 100)
root.config(padx= 20, pady=20)
button_calculate = tk.Button(text="calculate", command=calculate)
button_calculate.grid(row=1, column= 2)
button_switch = tk.Button(text="Switch", command=switch)
button_switch.grid(row=1, column=3)
user_input = tk.Entry(width=10)
user_input.grid(row=0, column=2)
kg_label = tk.Label(text="Km")
kg_label.grid(row=0, column=3)
mi_label = tk.Label(text="Mi")
mi_label.grid(row=2, column=3)


root.mainloop()
# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     print(total)
# add(4,6,5,5)
#
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2, add=3, multiply=5)