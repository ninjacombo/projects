import os
import tkinter as tk
from tkinter import filedialog

from PyPDF2 import PdfReader
from gtts import gTTS

filenames = []


def select_files():
    global filenames

    f_types = [('PDF files', '*.pdf')]

    filenames = list(filedialog.askopenfilenames(filetypes=f_types))

    if len(filenames) == 0:
        print("No files selected yet!")
        error_message.config(text="No files selected yet!", fg="red")
    else:
        error_message.config(text="Files selected successfully!", fg="green")


def add_files():
    global filenames
    temp_filenames = []

    f_types = [('PDF files', '*.pdf')]
    temp_filenames = filedialog.askopenfilenames(filetypes=f_types)
    filenames.extend(temp_filenames)

    if len(temp_filenames) == 0:
        print("No files selected yet!")
        error_message.config(text="No files selected yet!", fg="red")
    else:
        error_message.config(text="Files added successfully!", fg="green")


def convert_pdf_to_tts():
    global filenames

    if len(filenames) == 0:
        print("No files selected yet!")
        error_message.config(text="No files selected yet!", fg="red")
        return

    for filename in filenames:
        # Open the PDF file in read-binary mode
        # Open the PDF file in read-binary mode
        with open(filename, 'rb') as file:

            # Create a PdfReader object
            reader = PdfReader(file)

            # Iterate through each page
            for page in reader.pages:
                # Extract the text from the page
                text = page.extract_text()
                print(text)

        temp1 = filename.split('/')[-1].split('.')[-2]
        try:
            open('/'.join(filename.split("/")[:-1]) + "/tts_pdf/", 'r')
        except FileNotFoundError:
            os.mkdir('/'.join(filename.split("/")[:-1]) + "/tts_pdf/")
        except PermissionError:
            pass

        save_filename = '/'.join(
            filename.split("/")[:-1]) + "/tts_pdf/" + temp1 + "tts.mp3"
        print(save_filename)

        tts = gTTS(text=text)
        tts.save(save_filename)

        error_message.config(text="Files converted successfully!\n"
                                  f"{save_filename}", fg="green")

        filenames = []


# PDF to TTS

# Main Window
root = tk.Tk()
root.config(bg='#E6FFFD')
root.title("PDF to TTS")
root.geometry("900x650")
root.resizable(False, False)

# Title
title = tk.Label(root, text="PDF to TTS", font=("Arial", 30), bg="#E6FFFD", fg="#B799FF")
title.place(relx=0.5, rely=0.1, anchor="center")

# Description
description = tk.Label(root, text="Convert PDF files to TTS", font=("Arial", 15), bg="#E6FFFD", fg="#B799FF")
description.place(relx=0.5, rely=0.2, anchor="center")

# Instructions
instructions = tk.Label(root, text="Instructions:\n1. Select the PDF files you want to convert to TTS.\n2. Click on "
                                   "'Add Files' to add more files.\n3. Click on 'Convert' to convert the PDF files to "
                                   "TTS.\n4. The converted files will be saved in the same folder as the PDF files "
                                   "with the name 'tts_pdf'.", font=("Arial", 15), bg="#E6FFFD", fg="#B799FF")
instructions.place(relx=0.5, rely=0.4, anchor="center")

# Select Files Button
select_files_button = tk.Button(root, text="Select Files", font=("Arial", 15), bg="#B799FF", fg="#E6FFFD", width=15,
                                command=select_files)
select_files_button.place(relx=0.2, rely=0.6, anchor="center")

# Add Files Button
add_files_button = tk.Button(root, text="Add Files", font=("Arial", 15), bg="#B799FF", fg="#E6FFFD", width=15,
                             command=add_files)
add_files_button.place(relx=0.5, rely=0.6, anchor="center")

# Convert Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 15), bg="#B799FF", fg="#E6FFFD", width=15,
                           command=convert_pdf_to_tts)
convert_button.place(relx=0.8, rely=0.6, anchor="center")

# Error Message
error_message = tk.Label(root, text="", font=("Arial", 15), bg="#E6FFFD", fg="#B799FF")
error_message.place(relx=0.5, rely=0.8, anchor="center")

# Main Loop
root.mainloop()
