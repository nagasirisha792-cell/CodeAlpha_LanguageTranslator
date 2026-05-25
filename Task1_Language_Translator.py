from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", END)

    lang = language_var.get()

    language_codes = {
        "Telugu": "te",
        "Hindi": "hi",
        "Tamil": "ta",
        "English": "en"
    }

    translated = GoogleTranslator(
        source='auto',
        target=language_codes[lang]
    ).translate(text)

    output_text.delete("1.0", END)
    output_text.insert(END, translated)

root = Tk()
root.title("Language Translation Tool")
root.geometry("600x500")

title = Label(root,
text="Language Translation Tool",
font=("Arial",18))
title.pack(pady=10)

Label(root, text="Enter Text").pack()

input_text = Text(root, height=6, width=60)
input_text.pack()

Label(root, text="Select Language").pack()

language_var = StringVar()

language_dropdown = ttk.Combobox(
    root,
    textvariable=language_var
)

language_dropdown["values"] = (
    "Telugu",
    "Hindi",
    "Tamil",
    "English"
)

language_dropdown.current(0)
language_dropdown.pack()

Button(
    root,
    text="Translate",
    command=translate_text
).pack(pady=10)

Label(root, text="Translated Text").pack()

output_text = Text(root,
height=6,
width=60)
output_text.pack()

root.mainloop()