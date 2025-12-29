# CTkScrollableDropdownPP

[![PyPI Downloads](https://static.pepy.tech/badge/ctkscrollabledropdownpp)](https://pepy.tech/projects/ctkscrollabledropdownpp)

**CTkScrollableDropdownPP** is an enhanced dropdown widget for CustomTkinter featuring pagination, live search, grouping support, and multiple selection.

> Based on the original [CTkScrollableDropdown](https://github.com/Akascape/CTkScrollableDropdown) project.

## Features

* Pagination for large lists
* Real-time filtering
* Grouped items (using regex or labels)
* Autocomplete on typing
* Multiple selection support
* Fully customizable appearance

## Installation

```bash
pip install ctkscrollabledropdownpp
```

## Example

```python
import customtkinter
from PIL import Image, ImageDraw
from CTkScrollableDropdownPP import CTkScrollableDropdown
import io


def create_color_image(color, width=20, height=20):
    """Create an image of the specified color"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, width - 1, height - 1), fill=color)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return customtkinter.CTkImage(Image.open(img_bytes), size=(width, height))


def create_number_image(number, width=20, height=20):
    """Create an image with a digit"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, width - 1, height - 1), fill="#FFFFFF")
    draw.text((width // 2, height // 2), str(number), fill="#000000", anchor="mm")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return customtkinter.CTkImage(Image.open(img_bytes), size=(width, height))


# Create main window
root = customtkinter.CTk()
root.geometry("500x400")

# Create CTkComboBox
combobox = customtkinter.CTkComboBox(root, width=250)
combobox.pack(pady=50)

# Data for dropdown list
colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Orange": "#FFA500",
    "Purple": "#800080",
    "Pink": "#FFC0CB",
    "Brown": "#A52A2A",
    "Black": "#000000",
    "White": "#FFFFFF"
}

numbers = [str(i) for i in range(10)]  # Digits from 0 to 9

# Create lists of values and images
color_values = list(colors.keys())
color_images = [create_color_image(color_code) for color_code in colors.values()]

number_values = numbers
number_images = [create_number_image(num) for num in numbers]

# Combine all values and images
all_values = color_values + number_values
all_images = color_images + number_images

# Groups for sorting
groups = [
    ["Numbers", "^[0-9]$"],
    ["Colors", "__OTHERS__"]
]

# Create dropdown list
dropdown = CTkScrollableDropdown(attach=combobox, button_color="#2b2b2b", height=200, width=300, fg_color="#333333",
                                 values=all_values, command=lambda value: print(f"Selected: {value}"),
                                 image_values=all_images, text_color="#ffffff", hover_color="#3a3a3a",
                                 font=("Arial", 12), groups=groups, items_per_page=10, multiple=True)

root.mainloop()
```
