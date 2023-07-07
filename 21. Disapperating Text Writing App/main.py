import time
import tkinter as tk

ALL_SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', '[', ']', '{', '}', '|',
               '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
ALL_SMALL_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
ALL_CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z']
ALL_NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

end_time = 0
is_running = ''


def delete_text():
    text_box.delete("1.0", "end")


def disappear_text(event):
    global end_time, is_running
    if event.char in ALL_SYMBOLS or event.char in ALL_SMALL_LETTERS or event.char in ALL_CAPITAL_LETTERS or event.char \
            in ALL_NUMBERS:
        end_time = time.time() + 5
        if is_running != '':
            root.after_cancel(is_running)
        is_running = root.after(5000, delete_text)


# Disappearing text writing app

# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("Disappearing Text Writing App")
root.geometry("900x650")
root.resizable(False, False)

# Title
title = tk.Label(root, text="Disappearing Text Writing App", font=("Arial", 30), bg="#E6FFFD", fg="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Text Box
text_box = tk.Text(root, width=50, height=15, font=("Arial", 15), bg="white", fg="#B799FF")
text_box.place(relx=0.5, rely=0.6, anchor="center")
text_box.bind("<Key>", disappear_text)

# Text Box Label
text_box_label = tk.Label(root, text="Write something here:", font=("Arial", 15), bg="#E6FFFD", fg="#B799FF")
text_box_label.place(relx=0.3, rely=0.3, anchor="center")

root.mainloop()
