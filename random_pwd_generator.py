import tkinter as tk
from tkinter import font
import random
import string

root = tk.Tk()
root.geometry("650x675")
root.title("Random Password Generator")
root.iconbitmap(r'icon.ico')
root.configure(bg="#252222")
root.resizable(False, False)

S_font = font.Font(size=16)
M_font = font.Font(size=18)
L_font = font.Font(size=20)
XL_font = font.Font(size=26)

heading = tk.Label(root, text="Random Password Generator 🔐", font=XL_font, bg="#252222", fg="white")
heading.pack(pady=35)

Select_Pwd_Length = tk.Label(root, text="Select Password Length", bg="#252222", font=L_font, fg="white")
Select_Pwd_Length.pack(pady=(50,0))

pwd_length = tk.StringVar(value="8")

options_frame = tk.Frame(root, bg="#252222")
options_frame.pack(fill="x", padx=10)

options = ["8", "12", "16", "20"]

for i in range(len(options)):
    options_frame.columnconfigure(i, weight=1)

for i, text in enumerate(options):
    rb = tk.Radiobutton(
        options_frame, text=text, font=L_font, bg="#252222", fg="white",
        variable=pwd_length, value=text, indicatoron=True, selectcolor="#252222",
        activebackground="#252222", activeforeground="white"
    )
    rb.grid(row=0, column=i, pady=10)

check_box_options = tk.Frame(root, bg = "#252222")
check_box_options.pack(fill="x", padx=25, pady=(50,0))

symbol_var = tk.BooleanVar()
number_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

symbol = tk.Checkbutton(check_box_options, text="Include Symbols", font=M_font, bg="#252222", fg="white", indicatoron=True, 
                        selectcolor="#252222", activebackground="#252222", activeforeground="white", variable=symbol_var)
symbol.grid(column=0, row=1, pady=4, sticky="w")

number = tk.Checkbutton(check_box_options, text="Include Numbers", font=M_font, bg="#252222", fg="white", indicatoron=True, 
                        selectcolor="#252222", activebackground="#252222", activeforeground="white", variable=number_var)
number.grid(column=0, row=2, pady=4, sticky="w")

uppercase = tk.Checkbutton(check_box_options, text="Include Uppercase", font=M_font, bg="#252222", fg="white", indicatoron=True, 
                        selectcolor="#252222", activebackground="#252222", activeforeground="white", variable=uppercase_var)
uppercase.grid(column=0, row=3, pady=4, sticky="w")

password_frame = tk.Frame(root, bg="#252222")
password_frame.pack(fill="x", padx=25, pady=(30,0))

password_frame.columnconfigure(0, weight=1)
password_frame.columnconfigure(1, weight=0)
password_frame.columnconfigure(2, weight=1)

pwd_label = tk.Label(password_frame, text="Your Password", fg="white", bg="#252222", font=M_font)
pwd_label.grid(row=0, column=0, sticky="e", padx=(0,10))

password = tk.StringVar(value="")
pwd_entry = tk.Entry(password_frame, font=M_font, bg="#252222", fg="white", 
                     state="readonly", textvariable=password, justify="center", readonlybackground="#252222")
pwd_entry.grid(row=0, column=1, sticky="ew")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password.get())
    root.update()

copy_btn = tk.Button(password_frame, text="Copy", fg="white", bg="#252222", font=S_font, relief="flat", cursor="hand2", command=copy_to_clipboard)
copy_btn.grid(row=0, column=2, sticky="w", padx=(10,0))

generate_frame = tk.Frame(root, bg = "#252222")
generate_frame.pack(fill="x", padx=25, pady=(30,0))

def generate():
    length = int(pwd_length.get())
    characters = string.ascii_lowercase
    
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if number_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if not characters:
        password.set("Select an option!")
        return

    generated_pwd = "".join(random.choice(characters) for _ in range(length))
    password.set(generated_pwd)


generate_btn = tk.Button(generate_frame, text="Generate Password", fg="#252222", bg="white", font=M_font, relief="flat", cursor="hand2", command=generate, activebackground="#252222", activeforeground="white")
generate_btn.pack(pady=(35,0))

root.mainloop()