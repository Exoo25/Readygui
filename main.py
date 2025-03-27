from tkinter import *
from tkcode import *
from tkinter import filedialog, messagebox,ttk,font
import os
def CodeEditorr(title,font,langauge):
    app = Tk()
    app.title(title)
    app.geometry("800x600")
    filepath = None
    blockcursor = False
    # Initialize Code Editor
    editor = CodeEditor(app, highlighter="good", font=("Cascadia Code", 13), bg="black", undo=True, blockcursor=blockcursor, language=langauge)

    # Menu Bar
    menubar = Menu(app)
    def auto_indent(event):
        current_line = editor.get("insert linestart", "insert lineend")
        if current_line.strip().endswith(":"):
            editor.insert("insert", "\n    ")
            return "break"
    # Open File Function
    def openf(event=None):
        global filepath
        filepath = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        _, path = os.name(filepath)
        if filepath:
            with open(filepath, "r") as file:
                editor.delete(1.0, END)
                editor.insert(1.0, file.read())
        editor.config(language="python")
        if path == ".html":
            editor.config(language="html")
        

    # Save File Function
    def savef(event=None):
        global filepath
        if filepath:
            with open(filepath, "w") as file:
                file.write(editor.get(1.0, END))
        else:
            filepath = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
            if filepath:
                with open(filepath, "w") as file:
                    file.write(editor.get(1.0, END))

    # Run Function
    def run(event=None):
        global filepath
        if not filepath:
            messagebox.showerror("Error", "Please open or save a file before running it.")
        else:
            os.startfile(filepath)

    # File Menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openf)
    filemenu.add_command(label="Save", command=savef)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=lambda: app.quit())
    menubar.add_cascade(label="File", menu=filemenu)

    # Edit Menu
    editmenu = Menu(menubar, tearoff=0)
    def undo():
        try:
            # Check if there is an undo history
            if editor.index("1.0") != editor.index("insert"):  # If there's an undo history
                editor.edit_undo()
            else:
                print("Nothing to undo.")
        except TclError:
            # Handle TclError if nothing to undo
            print("Nothing to undo.")
    def redo():
        try:
            # Check if there is a redo history
            editor.edit_redo()
        except TclError:
            # Handle TclError if nothing to redo
            print("Nothing to redo.")


    editmenu.add_command(label="Undo", command=undo)
    editmenu.add_command(label="Redo", command=redo)
    editmenu.add_separator()
    editmenu.add_command(label="Copy", command=lambda: editor.event_generate("<<Copy>>"))
    editmenu.add_command(label="Cut", command=lambda: editor.event_generate("<<Cut>>"))
    editmenu.add_command(label="Paste", command=lambda: editor.event_generate("<<Paste>>"))
    menubar.add_cascade(label="Edit", menu=editmenu)
    viewmenu = Menu(menubar, tearoff=0)

    # Create the "Themes" submenu
    themes = Menu(viewmenu, tearoff=0)
    themes.add_command(label="Dracula", command=lambda:
                    editor.config(highlighter="dracula")
                    )
    themes.add_command(label="VS Code", command=lambda:
                    editor.config(highlighter="good")
                    )
    themes.add_command(label="Azure", command=lambda:
                    editor.config(highlighter="azure")
                    )
    themes.add_command(label="Monokai+", command=lambda:
                    editor.config(highlighter="monokai-plus-plus")
                    )
    themes.add_command(label="Monokai", command=lambda:
                    editor.config(highlighter="monokai")
                    )
    themes.add_command(label="Mariana", command=lambda:
                    editor.config(highlighter="mariana")
                    )
    # Add the "Themes" submenu to the "View" menu
    viewmenu.add_cascade(label="Theme", menu=themes)
    viewmenu.add_separator()
    def toggle(event=None):
        global blockcursor
        blockcursor = not blockcursor
        editor.config(blockcursor=blockcursor)

    viewmenu.add_command(label="Toggle Block Cursor", command=toggle)


    # Add the "View" menu to the main menu bar
    menubar.add_cascade(label="View", menu=viewmenu)
    # Configure Menu
    index = 0
    themess = ["dracula", "good", "azure", "monokai", "monokai-plus-plus", "mariana"]
    def toggle_theme(event=None):
        global index
        index = (index + 1) % len(themess)
        editor.config(highlighter=themess[index])
    def key_binds():
        keys = Tk()
        binds = ttk.Treeview(keys,columns=("Key", "Function"), show="headings")
        binds.heading("Key", text="Key")
        binds.heading("Function", text="Function")
        binds.insert("", END, values=("Ctrl+Z", "Undo"))
        binds.insert("", END, values=("Ctrl+Y", "Redo"))
        binds.insert("", END, values=("Ctrl+O", "Open File"))
        binds.insert("", END, values=("Ctrl+S", "Save File"))
        binds.insert("", END, values=("Ctrl+Shift+B", "Toggle Block Cursor"))
        binds.insert("", END, values=("Ctrl+Shift+T", "Toogle Theme"))
        binds.insert("", END, values=("Ctrl+C", "Copy"))
        binds.insert("", END, values=("Ctrl+X", "Cut"))
        binds.insert("", END, values=("Ctrl+V", "Paste"))
        binds.insert("", END, values=("Ctrl+Shift-R", "Run"))
        binds.pack()
        keys.mainloop()
    viewmenu.add_command(label="Key Binds", command=key_binds)
    app.config(menu=menubar)

    app.bind("<Control-o>", openf)
    app.bind("<Control-s>", savef)
    app.bind("<Control-Shift-B>", toggle)
    app.bind("<Control-Shift-T>", toggle_theme)
    app.bind("<Control-Shift-R>", run)
    app.bind("<Key>", auto_indent)
    runbtn = Button(app, text="      ▶️", command=run, width=3)
    runbtn.pack()

    editor.pack(fill=BOTH, expand=True)

    # Main Loop
    app.mainloop()
def word_counter(title,font):
    app = Tk()
    app.title(title)

    h1 = Label(app, text="word counter", font="arial 19 bold")
    h1.pack()

    sentence = Text(app, font="arial 13")
    sentence.pack()

    label = Label(app, text="it has ______ words ")
    label.pack()

    def click():
        text = sentence.get("1.0", "end-1c")
        length = len(text.split(" "))
        label.config(text=f'it has {length} words')
        label.pack()
        if len(text) == 0:
            messagebox.showerror("0error","the text must be 1 or 1+ characters")

    button = Button(app, text="count", command=click, font="arial 9")
    button.pack()

    app.mainloop()
def clock(title,font):
    from tkinter import ttk
    import time

    # Initialize the application
    app = Tk()

    # Create tabs
    notebook = ttk.Notebook(app)
    tab1 = Frame(app)
    tab2 = Frame(app)
    tab3 = Frame(app)

    notebook.add(tab1, text="Time")
    notebook.add(tab2, text="Date")
    notebook.add(tab3, text="Timer")

    # Time tab
    timenow = StringVar()
    timenow.set(time.strftime("%I:%M:%S %p"))

    def update_time_display():
        timenow.set(time.strftime("%I:%M:%S %p"))
        app.after(1000, update_time_display)

    timelab = Label(tab1, textvariable=timenow, font=("Digital-7", 35), fg="green", bg="black")
    timelab.pack()

    secvar = StringVar()
    secvar.set(time.time())

    def update_seconds():
        secvar.set(round(time.time(), 2))  # Display time with milliseconds
        app.after(100, update_seconds)

    Label(tab1, text="or", font=("Comic Sans MS", 14)).pack()
    seclab = Label(tab1, textvariable=secvar, font=("Consolas", 16))
    seclab.pack()

    # Date tab
    datetext = StringVar()
    datetext.set("Date: " + time.strftime("%D") + ", Day: " + time.strftime("%A"))

    datelab = Label(tab2, textvariable=datetext, font=("Comic Sans MS", 14))
    datelab.pack()

    # Timer tab
    timecc = StringVar()
    time_elapsed = 0
    is_running = False

    def format_timer(seconds):
        """Convert seconds to MM:SS format."""
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes}:{remaining_seconds:02}"

    def update_timer():
        global time_elapsed, is_running
        if is_running:
            time_elapsed += 1
            timecc.set(format_timer(time_elapsed))
            app.after(1000, update_timer)

    def start_timer():
        global is_running
        if not is_running:
            is_running = True
            update_timer()

    def reset_timer():
        global time_elapsed, is_running
        is_running = False
        time_elapsed = 0
        timecc.set(format_timer(time_elapsed))

    timecc.set(format_timer(time_elapsed))

    Button(tab3, text="Start", command=start_timer, font="Arial 12").pack()
    Label(tab3, textvariable=timecc, font=("Consolas", 19)).pack()
    Button(tab3, text="Reset", command=reset_timer, font="Arial 12").pack()

    # Pack notebook and start the main loop
    notebook.pack()
    update_time_display()
    update_seconds()

    app.maxsize(300, 150)
    app.mainloop()
def notepad(title):
    from tkinter.filedialog import asksaveasfile, askopenfile
    from tkinter.messagebox import showinfo
    from tkinter.colorchooser import askcolor
    app = Tk()
    app.title(title)

    def save():
        file = asksaveasfile(mode="w", defaultextension=".txt", filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt")
        ], initialfile="untitled")
        app.title(f"{title} - {file.name}")
        file.write(text.get(1.0, END))

    def openfile():
        file = askopenfile(mode="r", defaultextension=".txt", filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ])
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        app.title(f"{title} - {file.name}")
        
    def new():
        app.title(f"{title} - untitled")
        text.delete(1.0, END)

    def copytext():
        text.event_generate("<<Copy>>")

    def cut():
        text.event_generate("<<Cut>>")

    def paste():
        text.event_generate("<<Paste>>")

    def font_change(*args):
        text.config(font=(Font_name.get(), font_size.get()))

    def color_change():
        colorr = askcolor()
        text.config(fg=colorr[1])

    def undot():
        text.edit_undo()

    def redot():
        text.edit_redo()

    Font_name = StringVar()
    Font_name.set("Arial")
    font_size = StringVar()
    font_size.set("25")

    frame = Frame(app)
    fontsoption = OptionMenu(frame, Font_name, *font.families(), command=font_change)
    fontsoption.grid(row=0, column=1)
    font_size_op = Spinbox(frame, textvariable=font_size, command=font_change, from_=1, to=100)
    font_size_op.grid(row=0, column=2)
    color = Button(frame, command=color_change, text="Color").grid(row=0, column=3)
    frame.pack()

    menubar = Menu(app)
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu, font=23)
    file_menu.add_command(label="Save", command=save)
    file_menu.add_command(label="Open", command=openfile)
    file_menu.add_command(label="New", command=new)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=quit)

    edit_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edit", menu=edit_menu, font=23)
    edit_menu.add_command(label="Copy", command=copytext)
    edit_menu.add_command(label="Cut", command=cut)
    edit_menu.add_command(label="Paste", command=paste)
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo", command=undot)
    edit_menu.add_command(label="Redo", command=redot)

    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu, font=23)
    help_menu.add_command(label="About", command=lambda: showinfo("About", "NotePady: A program made by Mahdi Ali, the youngest multi-language developer in the world."))
    help_menu.add_separator()
    help_menu.add_command(label="How", command=lambda: showinfo("How to Use", "In NotePady, you can type text, format it, save files, open files, create new files, and more!"))

    # Format Menu
    format_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Format", menu=format_menu, font=23)

    def toggle_bold():
        if text.tag_ranges("sel"):
            current_tags = text.tag_names("sel.first")
            if 'bold' in current_tags:
                text.tag_remove('bold', "sel.first", "sel.last")
            else:
                text.tag_add('bold', "sel.first", "sel.last")
            text.tag_config('bold', font=(Font_name.get(), font_size.get(), "bold"))

    def toggle_italic():
        if text.tag_ranges("sel"):
            current_tags = text.tag_names("sel.first")
            if 'italic' in current_tags:
                text.tag_remove('italic', "sel.first", "sel.last")
            else:
                text.tag_add('italic', "sel.first", "sel.last")
            text.tag_config('italic', font=(Font_name.get(), font_size.get(), "italic"))

    def toggle_underline():
        if text.tag_ranges("sel"):
            current_tags = text.tag_names("sel.first")
            if 'underline' in current_tags:
                text.tag_remove('underline', "sel.first", "sel.last")
            else:
                text.tag_add('underline', "sel.first", "sel.last")
            text.tag_config('underline', font=(Font_name.get(), font_size.get(), "underline"))

    format_menu.add_command(label="Bold", command=toggle_bold)
    format_menu.add_command(label="Italic", command=toggle_italic)
    format_menu.add_command(label="Underline", command=toggle_underline)

    app.config(menu=menubar)

    text = Text(app, font=(Font_name.get(), font_size.get()), undo=True)
    scorll = Scrollbar(app)
    text.config(yscrollcommand=scorll.set)
    text.pack()
    scorll.pack()

    Label1 = Label(frame, text="0 Words", font=("Comic Sans MS", 10))
    Label1.grid(row=1, column=0)
    Label2 = Label(frame, text="0 Chars", font=("Comic Sans MS", 10))
    Label2.grid(row=1, column=1)

    def count():
        words = len(text.get(1.0, END).split(" "))
        Label1.config(text=f"{words} Words")
        Label2.config(text=f"{len(text.get(1.0, END))} Chars")
        app.after(1, count)

    count()

    app.mainloop()
def calcualtor(title):

    def press(num):
        current = calc_text.get()
        calc_text.set(current + str(num))

    def equal():
        try:
            result = str(eval(calc_text.get()))
            calc_text.set(result)
        except:
            calc_text.set("Error")

    def clear():
        calc_text.set("")

    app = Tk()
    app.title(title)
    app.geometry("250x250")  # Adjusted size for better fit

    calc_text = StringVar()
    Label1 = Label(app, textvariable=calc_text, font="Consolas 15", bg="white", width=15)
    Label1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    Button(app, text=7, width=5, command=lambda: press(7)).grid(row=1, column=0)
    Button(app, text=8, width=5, command=lambda: press(8)).grid(row=1, column=1)
    Button(app, text=9, width=5, command=lambda: press(9)).grid(row=1, column=2)
    Button(app, text='/', width=5, command=lambda: press('/')).grid(row=1, column=3)

    Button(app, text=4, width=5, command=lambda: press(4)).grid(row=2, column=0)
    Button(app, text=5, width=5, command=lambda: press(5)).grid(row=2, column=1)
    Button(app, text=6, width=5, command=lambda: press(6)).grid(row=2, column=2)
    Button(app, text='*', width=5, command=lambda: press('*')).grid(row=2, column=3)

    Button(app, text=1, width=5, command=lambda: press(1)).grid(row=3, column=0)
    Button(app, text=2, width=5, command=lambda: press(2)).grid(row=3, column=1)
    Button(app, text=3, width=5, command=lambda: press(3)).grid(row=3, column=2)
    Button(app, text='-', width=5, command=lambda: press('-')).grid(row=3, column=3)

    Button(app, text=0, width=5, command=lambda: press(0)).grid(row=4, column=0)
    Button(app, text='.', width=5, command=lambda: press('.')).grid(row=4, column=1)
    Button(app, text='=', width=5, command=equal).grid(row=4, column=2)
    Button(app, text='+', width=5, command=lambda: press('+')).grid(row=4, column=3)

    Button(app, text='C', width=5, command=clear).grid(row=5, column=0, columnspan=4)

    app.mainloop()
def image_generator(unsplash_access_key, font, theme, colortheme="blue"):
    import requests
    import io
    import customtkinter as ctk
    from PIL import Image
    from tkinter import filedialog

    # Initialize CustomTkinter settings
    ctk.set_appearance_mode(theme)
    ctk.set_default_color_theme(colortheme)  # Light theme

    # Create main window
    root = ctk.CTk()
    ctk.CTkFont(font)
    root.title("Image Generator")
    root.geometry("700x500")
    root.resizable(False, False)

    # Replace with your working Unsplash API key
    UNSPLASH_ACCESS_KEY = unsplash_access_key

    # Global variable to store the last downloaded image
    current_image = None

    # Function to download and save the image
    def download_image():
        global current_image
        if current_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                    filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])
            if file_path:
                current_image.save(file_path)
                print(f"Image saved as {file_path}")

    # Function to retrieve and display an image
    def display_image(category):
        global current_image
        if category == "Choose Category":
            return
        
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        try:
            
            response = requests.get(url)
            response.raise_for_status()
            download_button.grid_forget()
            data = response.json()
            
            
            img_url = data.get("urls", {}).get("regular")
            if not img_url:
                label.configure(text="No image found", image=None)
                download_button.grid_forget()
                return

            img_data = requests.get(img_url).content
            current_image = Image.open(io.BytesIO(img_data)).resize((600, 400), Image.LANCZOS)
            
            # Convert to CTkImage to avoid warning
            ctk_image = ctk.CTkImage(light_image=current_image, size=(600, 400))

            label.configure(image=ctk_image, text="")
            label.image = ctk_image

            # Show download button after an image is loaded
            download_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        except requests.exceptions.RequestException as e:
            label.configure(text="Error fetching image", image=None)
            download_button.grid_forget()
            print(f"Error: {e}")

    # Function to enable/disable the "Generate Image" button
    def enable_button(*args):
        generate_button.configure(state="normal" if category_var.get() != "Choose Category" else "disabled")

    # Create GUI elements
    def create_gui():
        global category_var, generate_button, label, download_button

        # Category dropdown menu
        category_var = ctk.StringVar(value="random")
        
        category_dropdown = ctk.CTkEntry(root, textvariable=category_var)
        category_dropdown.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        # Generate Image button
        generate_button = ctk.CTkButton(root, text="Generate Image", state="disabled", 
                                        command=lambda: display_image(category_var.get()), 
                                        font=("Arial", 14, "bold"), corner_radius=8, 
                                        fg_color="#8ecae6",
                                        hover_color="#219ebc", text_color="white")
        generate_button.grid(row=0, column=1, padx=10, pady=20, sticky="ew")

        # Label to display images
        label = ctk.CTkLabel(root, text="Select a category to generate an image", width=600, height=400, corner_radius=8, 
                            fg_color="#f0f8ff", anchor="center")
        label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Download Image button (initially hidden)
        download_button = ctk.CTkButton(root, text="Download Image", command=download_image,
                                        font=("Arial", 12), corner_radius=8, fg_color="#4CAF50", 
                                        hover_color="#388E3C", text_color="white")
        download_button.grid(row=2, column=0, columnspan=2, pady=10)
        download_button.grid_forget()  # Hide initially

        # Configure grid to make columns/rows expandable
        root.grid_columnconfigure([0, 1], weight=1)
        root.grid_rowconfigure(1, weight=1)
        
        enable_button()
        root.mainloop()

    if __name__ == '__main__':
        create_gui()
image_generator("obfif3lGZRvpY27y2ouZKzag5I_P222JSZxgrCDjXug","arial", "dark", "blue")
