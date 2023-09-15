import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # You need to install the Pillow library for image handling
name = None
address = None
phone_number = None
def place_order():
    name = name_entry.get()
    address = address_entry.get()
    phone_number = phone_entry.get()

    # Add your order processing logic here
    order_summary = f"Name: {name}\nAddress: {address}\nPhone Number: {phone_number}"
    messagebox.showinfo("Order Placed", order_summary)
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

    address_label = ttk.Label(order_frame, text="Address:",background='#011533',foreground='white')
    address_label.grid(row=1, column=0, padx=10, pady=10)
    address_entry = ttk.Entry(order_frame)
    address_entry.grid(row=1, column=1, padx=10, pady=10)

    phone_label = ttk.Label(order_frame, text="Phone Number:",background='#011533',foreground='white')
    phone_label.grid(row=2, column=0, padx=10, pady=10)
    phone_entry = ttk.Entry(order_frame)
    phone_entry.grid(row=2, column=1, padx=10, pady=10)

    order_button = ttk.Button(order_frame, text="Place Order", command=place_order)
    order_button.grid(row=3, columnspan=2, padx=10, pady=10)

    # Add an image
    image = Image.open("drone.jpg")  # Replace with your image path

    photo = ImageTk.PhotoImage(image)
    image_label = ttk.Label(order_frame, image=photo)
    image_label.grid(row=6, columnspan=2, padx=10, pady=10)
    image_label.photo = photo  # To prevent garbage collection

    root.mainloop()
