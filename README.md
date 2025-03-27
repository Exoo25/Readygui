# ReadyGui

ReadyGui is a Python library that provides ready-made GUI applications, including a Code Editor, Text Editor, Calculator, Image Generator, Clock, and Word Counter. It is designed for ease of use and customization.

## Features
- **Code Editor** – A simple code editor with syntax highlighting.
- **Text Editor** – A basic notepad for writing and saving text.
- **Calculator** – A functional calculator for basic arithmetic operations.
- **Image Generator** – Generate images using the Unsplash API (API key required).
- **Clock** – Displays the current time in a GUI window.
- **Word Counter** – Counts words and characters in a text input.

## Installation
### Method 1: Download ZIP
Download the ZIP from GitHub, extract it, and move the folder to your Python `Lib` directory.

### Method 2: Clone from GitHub
```sh
git clone https://github.com/Exoo25/Readygui.git
cd readygui
pip install -r requirements.txt
```

## Usage
### Importing ReadyGui
```python
import readygui
```

### Launch Applications
```python
# Open Code Editor
readygui.code_editor(language="Python", font="Courier", title="My Code Editor")

# Open Text Editor
readygui.text_editor(title="My Notepad")

# Open Calculator
readygui.calculator()

# Open Image Generator (Requires Unsplash API Key)
readygui.image_generator(api_key="your_unsplash_api_key")

# Open Clock
readygui.clock(font="Arial", title="Digital Clock")

# Open Word Counter
readygui.word_counter(font="Times New Roman", title="Word Counter")
```

## Customization
You can customize window titles, sizes, and fonts using optional parameters:
```python
readygui.code_editor(language="JavaScript", font="Consolas", title="JS Editor")
readygui.clock(font="Verdana", title="My Clock")
```

## Dependencies
- `tkinter` for UI components
- `requests` for API calls (Image Generator)

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
For any issues or suggestions, reach out via GitHub or forums.

---
Enjoy using **ReadyGui**! 🚀
