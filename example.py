import customtkinter as ctk
from CTkScrollableDropdownPP import CTkScrollableDropdown

app = ctk.CTk()
app.geometry("400x300")

combobox = ctk.CTkComboBox(
    master=app,
    values=[],
    width=200,
    height=30
)
combobox.pack(pady=50)

values = [f"Item {i}" for i in range(1, 101)]

dropdown = CTkScrollableDropdown(
    attach=combobox,
    values=values,
    command=lambda v: print("Selected:", v),
    autocomplete=True,
    groups=[
        ('1-50', r'^Item ([1-9]|[1-4][0-9]|50)$'),
        ('Others', '__OTHERS__')
    ],
)

app.mainloop()