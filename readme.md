# System Requirements
- Ubuntu 22.04 (WSL)
Always run `sudo apt-get update`
- Python 3.10.x
- pip
`sudo apt install python3-pip`
- venv
`sudo apt-get install python3-venv`
- tkinter
`sudo apt-get install python3-tk`
- requirements.txt
`pip install -r requirements.txt`

# Design choices

- Canvas for drawing(tablet)
- Buttons for operations + Keybinding
    - Save image of canvas (DONE)
    - Clear (DONE)
    - Run Latex conversion and display on Latex Display
    - Run calculation
    - Copy Latex (keybinding)
- Latex Display
- Latex input
- Dropdown box for all the functions/calculations (Lagrange, etc)
