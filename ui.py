from tkinter import *
from PIL import ImageTk, Image
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


    def choose_file(self):
        filename = filedialog.askopenfilename(
            title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if filename:
            my_image = Image.open(filename)
            my_image.thumbnail((1000,500), Image.LANCZOS)
            img = ImageTk.PhotoImage(my_image)
            
            self.canvas.create_image(500, 250, image=img, tags="img")
            self.canvas.image = img

    def add_text(self):
        pass

root = Tk()
app = Interface(root)
root.mainloop()
