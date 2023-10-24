from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog


class Interface:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Watermarking")
        self.root.config(pady=20, padx=20)
        self.root.state("zoomed")
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.canvas = Canvas(height=500, width=1000, bg="Gray")
        self.canvas.grid(column=0, columnspan=3, row=0)

        self.text_entry = Entry(self.root, font=("Arial", 24))
        self.text_entry.grid(column=1, row=1, pady=20)

        self.btn_choose = Button(
            self.root, text="Choose file", command=self.choose_file, font=("Arial", 24)
        )
        self.btn_choose.grid(column=0, row=2, pady=10)

        self.btn_add_text = Button(
            self.root,
            text="Add text to image",
            command=self.add_text,
            font=("Ariel", 24),
        )
        self.btn_add_text.grid(column=2, row=2, pady=10)

        self.photo_to_modify = None
        self.edited_photo = None

    def choose_file(self):
        filename = filedialog.askopenfilename(
            title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if filename:
            my_image = Image.open(filename)
            self.photo_to_modify = filename
            my_image.thumbnail((1000, 500), Image.LANCZOS)
            img = ImageTk.PhotoImage(my_image)

            self.canvas.create_image(500, 250, image=img, tags="img")
            self.canvas.image = img

    def add_text(self):
        img = Image.open(self.photo_to_modify)
        text_font = ImageFont.truetype("arial.ttf", 70)
        text_to_add = self.text_entry.get()

        edit_image = ImageDraw.Draw(img)
        width, height = img.size
        edit_image.text((width / 2, height / 2), text_to_add, ("red"), font=text_font)

        if img:
            filename = filedialog.asksaveasfilename(
                title="Save image as", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
            )
            if filename:
                self.edited_photo = filename
                img.save(filename)
                self.canvas.after(2000, self.show_img)

    def show_img(self):
        edited_img = Image.open(self.edited_photo)
        edited_img.thumbnail((1000, 500), Image.LANCZOS)
        img = ImageTk.PhotoImage(edited_img)
        self.canvas.create_image(500, 250, image=img, tags="img")
        self.canvas.image = img
