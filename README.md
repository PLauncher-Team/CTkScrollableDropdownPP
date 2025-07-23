# CTkScrollableDropdownPP

**CTkScrollableDropdownPP** is an enhanced dropdown widget for CustomTkinter featuring pagination, live search, and grouping support.

> Based on the original [CTkScrollableDropdown](https://github.com/Akascape/CTkScrollableDropdown) project.

## Features

* Pagination for large lists
* Real-time filtering
* Grouped items (using regex or labels)
* Autocomplete on typing
* Fully customizable appearance

## Installation

```bash
pip install ctkscrollabledropdownpp
```

## Quick Start

```python
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
```
