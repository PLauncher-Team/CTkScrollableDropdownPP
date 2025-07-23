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
from ctkscrollabledropdownpp import CTkScrollableDropdown

app = ctk.CTk()
btn = ctk.CTkButton(app, text='Select')
btn.pack(pady=20)

values = [f"Item {i}" for i in range(1, 101)]

dropdown = CTkScrollableDropdown(
    attach=btn,
    values=values,
    command=lambda v: print("Selected:", v),
    items_per_page=20,
    pagination=True,
    autocomplete=True,
    groups=[('1-50', r'^Item [1-4]'), ('Others', '__OTHERS__')]
)

app.mainloop()
```
