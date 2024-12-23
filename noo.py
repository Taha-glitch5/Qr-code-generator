import tkinter as tk
from PIL import Image, ImageTk
import qrcode
import random


def random_color():
    """Generate a random color in RGB format."""
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"


def generate_qrcode():
    """Generate a colorful QR code containing user input data."""
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    age = age_entry.get().strip()
    username = username_entry.get().strip()
    email = email_entry.get().strip()
    link = link_entry.get().strip()

    if not (first_name and last_name and age and username and email and link):
        error_label.config(text="Please fill in all fields before generating the QR code.", fg="red")
        return

    user_info = (
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Age: {age}\n"
        f"Username: {username}\n"
        f"Email: {email}\n"
        f"Link: {link}"
    )

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(user_info)
    qr.make(fit=True)

    fill_color = random_color()
    back_color = random_color()
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    qr_display = ImageTk.PhotoImage(qr_img.resize((200, 200)))
    qr_label.config(image=qr_display)
    qr_label.image = qr_display
    error_label.config(text="QR Code generated successfully!", fg="green")


def change_background_color():
    """Change the background and elements' colors."""
    new_bg_color = random_color()
    new_fg_color = random_color()

    root.config(bg=new_bg_color)
    title_label.config(bg=new_bg_color, fg=new_fg_color)
    error_label.config(bg=new_bg_color, fg=new_fg_color)
    info_frame.config(bg=new_bg_color)

    # Update all entry fields and labels inside the info frame
    for widget in info_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=new_bg_color, fg=new_fg_color)
        elif isinstance(widget, tk.Entry):
            widget.config(bg=new_bg_color, fg=new_fg_color)

    qr_frame.config(bg=new_fg_color)
    qr_label.config(bg=new_bg_color)
    generate_qr_button.config(bg=new_fg_color, fg=new_bg_color)
    change_bg_button.config(bg=new_fg_color, fg=new_bg_color)
    button_frame.config(bg=new_bg_color)  # Update the button frame's background color


# Main app setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("750x800")
root.config(bg="#1e1e3e")

title_label = tk.Label(root, text="Einstein was never a programmer", bg="#1e1e3e", fg="#dcdfe4", font=("Arial", 19, "bold"))
title_label.pack(pady=20)

qr_frame = tk.Frame(root, bg="#61afef", bd=3, relief="solid")
qr_frame.pack(pady=20)

qr_label = tk.Label(qr_frame, bg="white")
qr_label.pack(padx=5, pady=5)

error_label = tk.Label(root, bg="#1e1e3e", fg="red", font=("Arial", 10))
error_label.pack(pady=5)

info_frame = tk.Frame(root, bg="#1e1e3e")
info_frame.pack(pady=10)

fields = [
    ("First Name:", "first_name_entry"),
    ("Last Name:", "last_name_entry"),
    ("Age:", "age_entry"),
    ("Username:", "username_entry"),
    ("Email:", "email_entry"),
    ("Link:", "link_entry"),
]

entries = {}
for i, (label_text, entry_var) in enumerate(fields):
    label = tk.Label(info_frame, text=label_text, bg="#1e1e3e", fg="#61afef", font=("Arial", 12))
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(info_frame, bg="#1e1e3e", fg="white", font=("Arial", 12))
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[entry_var] = entry

first_name_entry = entries["first_name_entry"]
last_name_entry = entries["last_name_entry"]
age_entry = entries["age_entry"]
username_entry = entries["username_entry"]
email_entry = entries["email_entry"]
link_entry = entries["link_entry"]

button_frame = tk.Frame(root, bg="#1e1e3e")
button_frame.pack(pady=20)

generate_qr_button = tk.Button(button_frame, text="Generate Colorful QR Code", command=generate_qrcode, bg="#61afef", fg="white", font=("Arial", 12, "bold"))
generate_qr_button.grid(row=0, column=0, padx=10)

change_bg_button = tk.Button(button_frame, text="Change Background Color", command=change_background_color, bg="#61afef", fg="white", font=("Arial", 12, "bold"))
change_bg_button.grid(row=0, column=1, padx=10)

root.mainloop()
