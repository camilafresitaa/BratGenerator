import tkinter as tk

# Saves user's input and updates text
def update_text(event):
    user_input = entry.get()
    text_brat.config(text=f"{user_input}")

# Validates characters limit
def validate_characters(new_text):
    if len(new_text) <= 40:
        return True
    return False

window = tk.Tk()

# Window Configuration
window.title("BRAT GENERATOR")
window.geometry("700x750")
window.configure(bg="white")
window.resizable(False, False)

# Frame 1 (Text)
frame_text = tk.Frame(
        window,
        bg="#8ACE00",
        width=630,
        height=630)
frame_text.pack(fill="both", expand=True, padx=20, pady=(20,0))

# Frame 2 (Entry)
frame_entry = tk.Frame(
        window,
        bg="white",
        width=630,
        height=40)
frame_entry.pack(fill="both", expand=True, padx=20, pady=(0, 20))

# Text Widget
text_brat = tk.Label(
                frame_text,
                font=("Arial Narrow", 120),
                fg="black",
                bg="#8ACE00",
                height=5,
                wraplength=620
                )
text_brat.pack(fill="both", expand=True)

# Entry Widget with validation
text_entry = tk.StringVar()
vcmd = window.register(validate_characters)
entry = tk.Entry(
        frame_entry,
        textvariable=text_entry,
        bg="white",
        fg="black",
        font=("Arial Narrow", 15),
        relief="flat",
        width=13,
        validate="key",  # Activar validación al escribir
        validatecommand=(vcmd, "%P")  # Validar con la función definida
        )
entry.pack()


# Bind return key to save_input function
entry.bind("<KeyRelease>", update_text) 

window.mainloop()