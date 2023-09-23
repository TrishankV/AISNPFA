# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk  # You need to install the Pillow library for image handling
# from connection import *

# name = None
# address = None
# phone_number = None

# def show_map():
#     # Create a new window
#     image_window = tk.Toplevel(root)
#     image_window.title("Image Viewer")

#     # Load and display the image
#     image = Image.open("drone.jpg")  # Replace "your_image.jpg" with the path to your image file
#     photo = ImageTk.PhotoImage(image)
#     image_label = tk.Label(image_window, image=photo)
#     image_label.image = photo  # Keep a reference to avoid garbage collection
#     image_label.pack()

# def place_order():
#     name = name_entry.get()
#     address = address_entry.get()
#     phone_number = phone_entry.get()
#     pickup = address_pick.get()
#     phoneSender = phone_sender.get()

#     check = simulate(address,pickup)
#     # Add your order processing logic here
#     if check == True:
#         order_summary = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\n Pickup Address : {pickup} \n Phone Number of Sender : {phoneSender}"
#         messagebox.showinfo("Order Placed", order_summary)
#     else:
#         order_summary = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\n Pickup Address : {pickup} \n Phone Number of Sender : {phoneSender}"
#         button = tk.Button(root, text="Show Image", command=show_map)
#         button.pack()
#         messagebox.showinfo("Address not found \n ", order_summary,"\n\n\n",button)

# if __name__ == "__main__" :
#     root = tk.Tk()
#     root.title("Order System")

#     # Create a notebook (tabbed interface)
#     notebook = ttk.Notebook(root)
#     notebook.pack(fill='both', expand=True)

#     # Home Tab
#     home_frame = tk.Frame(notebook, background='#011533')
#     notebook.add(home_frame, text="Home")

#     home_label = ttk.Label(home_frame, text="Welcome to our order system!", font=("Helvetica", 16),background='#011533',foreground='white')
#     home_label.pack(padx=20, pady=20)

#     # About Tab
#     about_frame = tk.Frame(notebook,background='#011533')
#     notebook.add(about_frame, text="About")

#     about_label = ttk.Label(about_frame, text="This is our amazing order system.", font=("Helvetica", 16),background='#011533',foreground='white')
#     about_label.pack(padx=20, pady=20)

#     # Place Order Tab
#     order_frame = tk.Frame(notebook,background='#011533')
#     notebook.add(order_frame, text="Place Order")

#     name_label = ttk.Label(order_frame, text="Name:",background='#011533',foreground='white')
#     name_label.grid(row=0, column=0, padx=10, pady=10)
#     name_entry = ttk.Entry(order_frame)
#     name_entry.grid(row=0, column=1, padx=10, pady=10)

#     address_label_pick = ttk.Label(order_frame, text="Pickup Address",background='#011533',foreground='white')
#     address_label_pick.grid(row=1, column=0, padx=10, pady=10)
#     address_pick = ttk.Entry(order_frame)
#     address_pick.grid(row=1, column=1, padx=10, pady=10)

#     address_label = ttk.Label(order_frame, text="Dropoff Address",background='#011533',foreground='white')
#     address_label.grid(row=2, column=0, padx=10, pady=10)
#     address_entry = ttk.Entry(order_frame)
#     address_entry.grid(row=2, column=1, padx=10, pady=10)

#     phone_label_sender = ttk.Label(order_frame, text="Phone Number of Sender :",background='#011533',foreground='white')
#     phone_label_sender.grid(row=3, column=0, padx=10, pady=10)
#     phone_sender = ttk.Entry(order_frame)
#     phone_sender.grid(row=3, column=1, padx=10, pady=10)

#     phone_label = ttk.Label(order_frame, text="Phone Number of receiver :",background='#011533',foreground='white')
#     phone_label.grid(row=4, column=0, padx=10, pady=10)
#     phone_entry = ttk.Entry(order_frame)
#     phone_entry.grid(row=4, column=1, padx=10, pady=10)

#     order_button = ttk.Button(order_frame, text="Place Order", command=place_order)
#     order_button.grid(row=5, columnspan=2, padx=10, pady=10)
#     # Add an image
#     image = Image.open("drone.jpg")  # Replace with your image path

#     photo = ImageTk.PhotoImage(image)
#     image_label = ttk.Label(order_frame, image=photo)
#     image_label.grid(row=6, columnspan=2, padx=10, pady=10)
#     image_label.photo = photo  # To prevent garbage collection

#     root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # You need to install the Pillow library for image handling
from connection import *
from send_mail import *

name = None
address = None
phone_number = None

def show_map():
    # Create a new window
    image_window = tk.Toplevel(root)
    image_window.title("Image Viewer")

    # Load and display the image
    image = Image.open("drone.jpg")  # Replace "your_image.jpg" with the path to your image file
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(image_window, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.pack()

def send_message():
    name_contact = name_contact_entry.get()
    email = email_entry.get()
    phone_contact = phone_contact_entry.get()
    message = message_text.get("1.0", "end-1c")  # Get the message from the Text widget

    # Call your function here with the parameters
    send_email(name_contact,email,phone_contact,message)
    # For example, you can print the values for demonstration purposes
    print("Raising query through email")
    print("Name:", name_contact)
    print("Email:", email)
    print("Phone Number:", phone_contact)
    print("Message:", message)

def place_order():
    name = name_entry.get()
    address = address_entry.get()
    phone_number = phone_entry.get()
    pickup = address_pick.get()
    phoneSender = phone_sender.get()

    check = simulate(address,pickup,phoneSender,phone_number)
    # Add your order processing logic here
    if check == True:
        order_summary = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\n Pickup Address : {pickup} \n Phone Number of Sender : {phoneSender}"
        messagebox.showinfo("Order Placed", order_summary)
    else:
        order_summary = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}\n Pickup Address : {pickup} \n Phone Number of Sender : {phoneSender}"
        button = tk.Button(root, text="Show Image", command=show_map)
        button.pack()
        messagebox.showinfo("Address not found \n ", order_summary,"\n\n\n",button)

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("Order System")

    # Create a notebook (tabbed interface)
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Home Tab
    home_frame = tk.Frame(notebook, background='#011533')
    notebook.add(home_frame, text="Home")

    home_label = ttk.Label(home_frame, text="Welcome to our order system!", font=("Helvetica", 16),background='#011533',foreground='white')
    home_label.pack(padx=20, pady=20)

    # About Tab
    about_frame = tk.Frame(notebook,background='#011533')
    notebook.add(about_frame, text="About")

    about_label = ttk.Label(about_frame, text="This is our amazing order system.", font=("Helvetica", 16),background='#011533',foreground='white')
    about_label.pack(padx=20, pady=20)

    # Place Order Tab
    order_frame = tk.Frame(notebook,background='#011533')
    notebook.add(order_frame, text="Place Order")

    name_label = ttk.Label(order_frame, text="Name:",background='#011533',foreground='white')
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = ttk.Entry(order_frame)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    address_label_pick = ttk.Label(order_frame, text="Pickup Address",background='#011533',foreground='white')
    address_label_pick.grid(row=1, column=0, padx=10, pady=10)
    address_pick = ttk.Entry(order_frame)
    address_pick.grid(row=1, column=1, padx=10, pady=10)

    address_label = ttk.Label(order_frame, text="Dropoff Address",background='#011533',foreground='white')
    address_label.grid(row=2, column=0, padx=10, pady=10)
    address_entry = ttk.Entry(order_frame)
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    phone_label_sender = ttk.Label(order_frame, text="Phone Number of Sender :",background='#011533',foreground='white')
    phone_label_sender.grid(row=3, column=0, padx=10, pady=10)
    phone_sender = ttk.Entry(order_frame)
    phone_sender.grid(row=3, column=1, padx=10, pady=10)

    phone_label = ttk.Label(order_frame, text="Phone Number of receiver :",background='#011533',foreground='white')
    phone_label.grid(row=4, column=0, padx=10, pady=10)
    phone_entry = ttk.Entry(order_frame)
    phone_entry.grid(row=4, column=1, padx=10, pady=10)

    order_button = ttk.Button(order_frame, text="Place Order", command=place_order)
    order_button.grid(row=5, columnspan=2, padx=10, pady=10)
    # Add an image
    image = Image.open("drone.jpg")  # Replace with your image path

    photo = ImageTk.PhotoImage(image)
    image_label = ttk.Label(order_frame, image=photo)
    image_label.grid(row=6, columnspan=2, padx=10, pady=10)
    image_label.photo = photo  # To prevent garbage collection

    # ... (previous code) ...

    contact_frame = tk.Frame(notebook, background='#011533')
    notebook.add(contact_frame, text="Contact")

    name_contact_label = ttk.Label(contact_frame, text="Name:", background='#011533', foreground='white')
    name_contact_label.grid(row=0, column=0, padx=10, pady=10)
    name_contact_entry = ttk.Entry(contact_frame)
    name_contact_entry.grid(row=0, column=1, padx=10, pady=10)

    email_label = ttk.Label(contact_frame, text="Email:", background='#011533', foreground='white')
    email_label.grid(row=1, column=0, padx=10, pady=10)
    email_entry = ttk.Entry(contact_frame)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    phone_contact_label = ttk.Label(contact_frame, text="Phone Number:", background='#011533', foreground='white')
    phone_contact_label.grid(row=2, column=0, padx=10, pady=10)
    phone_contact_entry = ttk.Entry(contact_frame)
    phone_contact_entry.grid(row=2, column=1, padx=10, pady=10)

    message_label = ttk.Label(contact_frame, text="Message:", background='#011533', foreground='white')
    message_label.grid(row=3, column=0, padx=10, pady=10)
    message_text = tk.Text(contact_frame, height=5, width=30)
    message_text.grid(row=3, column=1, padx=10, pady=10)

    contact_button = ttk.Button(contact_frame, text="Send Message",command=send_message)
    contact_button.grid(row=4, columnspan=2, padx=10, pady=10)
    root.mainloop()
