import base64
from tkinter import *
from tkinter import ttk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

bg_color = "salmon"
fg_color = "#000080"
slight_dark = "#232287"
root = Tk()
root.geometry("900x600")
root["background"] = "salmon"
slogan = Label(root, text="Encrypt and Decrypt messages.",bg=bg_color, fg=fg_color, font=("Helvetica", 30, "bold"))
slogan.grid(row=0, column=0, padx=(50, 50), pady=(30, 60))

enter_text = StringVar()
enter_text_label = Label(root, text="Enter your message", bg=bg_color, fg=slight_dark,
                         font=("Helvetica", 20, "bold"))
enter_text_input = Entry(root, textvariable=enter_text, bg=bg_color, fg=fg_color, width=44,font=("Helvetica", 20, "bold"))

enter_text_label.grid(row=1, column=0, pady=(0, 30))
enter_text_input.grid(row=2, column=0)

encrypted_text_label = Label(root, text="Your desired output", bg=bg_color, fg=slight_dark,
                                 font=("Helvetica", 20, "bold"))
encrypted_text_label.grid(row=3, column=0, pady=(50, 30))


def encoded_output():
    user_message = base64.encodebytes(enter_text.get().encode('utf-8'))
    encrypted_text_body = Label(root, text=user_message, bg=bg_color, fg=fg_color, width=40, font=("Helvetica", 20, "bold"),
                                borderwidth=1, relief="sunken")
    encrypted_text_body.grid(row=4, column=0)
    root.clipboard_clear()
    root.clipboard_append(user_message)


def decoded_output():
    user_message = base64.decodebytes(enter_text.get().encode())
    encrypted_text_body = Label(root, text=user_message, bg=bg_color, fg=fg_color, width=40, font=("Helvetica", 20, "bold"),
                                borderwidth=1, relief="sunken")
    encrypted_text_body.grid(row=4, column=0)
    root.clipboard_clear()
    root.clipboard_append(user_message)


encode_btn = ttk.Button(root, text="Encode", command=encoded_output)
decode_btn = ttk.Button(root, text="Decode", command=decoded_output)

encode_btn.place(x=300, y=550)
decode_btn.place(x=500, y=550)

root.mainloop()
