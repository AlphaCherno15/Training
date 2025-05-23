import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def select_base_image():

    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        app.base_image_path = path
        base_image_label.config(text=f"Base Image: {path.split('/')[-1]}")

def select_logo_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        app.logo_image_path = path
        logo_image_label.config(text=f"Logo: {path.split('/')[-1]}")

def add_watermark():

    try:
        base_img = Image.open(app.base_image_path).convert("RGBA")
        logo_img = Image.open(app.logo_image_path).convert("RGBA")
        base_w, base_h = base_img.size
        logo_w = int(base_w * 0.1)
        logo_h = int(logo_img.height * (logo_w / logo_img.width))
        logo_img = logo_img.resize((logo_w, logo_h), Image.LANCZOS)

        position = (base_w - logo_w - 10, base_h - logo_h - 10)
        base_img.paste(logo_img, position, logo_img)

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg;*.jpeg")])
        if save_path:
            base_img.save(save_path)
            messagebox.showinfo("Success", f"Watermarked image saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
app = tk.Tk()
app.title("Image Watermark Tool")
app.geometry("400x250")
app.base_image_path = ""
app.logo_image_path = ""

tk.Label(app, text="Watermark Your Image", font=("Helvetica", 16, "bold")).pack(pady=10)
base_image_label = tk.Label(app, text="Base Image: None")
base_image_label.pack()
tk.Button(app, text="Select Base Image", command=select_base_image).pack(pady=5)
logo_image_label = tk.Label(app, text="Logo: None")
logo_image_label.pack()
tk.Button(app, text="Select Logo Image", command=select_logo_image).pack(pady=5)
tk.Button(app, text="Add Watermark & Save", command=add_watermark, bg="#4CAF50", fg="white").pack(pady=15)
app.mainloop()