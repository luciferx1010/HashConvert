import hashlib
import tkinter as tk
from tkinter import filedialog

def convert_to_hash(input_text):
    sha256 = hashlib.sha256()
    sha256.update(input_text.encode())
    return sha256.hexdigest()

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as f:
            input_text = f.read()
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, convert_to_hash(input_text))

def convert_text():
    input_text = input_textbox.get(1.0, tk.END).strip()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, convert_to_hash(input_text))

root = tk.Tk()
root.title("Hash Converter")

input_frame = tk.Frame(root)
input_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

file_button = tk.Button(input_frame, text="Open File", command=open_file)
file_button.pack(side=tk.LEFT)

input_textbox = tk.Text(input_frame, height=5)
input_textbox.pack(side=tk.LEFT, padx=10)

convert_button = tk.Button(input_frame, text="Convert", command=convert_text)
convert_button.pack(side=tk.LEFT)

output_text = tk.Text(root, height=5)
output_text.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
credit = tk.Label(root, text="Created by Atharv Puranik", bg='black', fg='white')
credit.pack(side=tk.BOTTOM)

root.mainloop()
