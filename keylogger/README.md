# Input Monitoring & Control (Python + pynput)

## Overview
This project demonstrates the use of the `pynput` library to automate and monitor user input devices.  
It includes examples of:

- Mouse control  
- Keyboard control  
- Keyboard event logging  
- Mouse movement tracking  

> **Note:** This project is intended strictly for educational and personal-use testing on your own system.

---

## Files Included
- **Control.py** – Automates mouse movement and keyboard typing  
- **main.py** – Listens for and logs keyboard input  
- **mouseListener.py** – Listens for and prints mouse movement coordinates  
- **log.txt** – Automatically generated file storing logged keys  

---

## Features

### 1. Mouse and Keyboard Automation (`Control.py`)
- Moves the mouse cursor to a specific screen position **(500, 200)**
- Types the text **"Hello"** automatically
- Uses:
  - `MouseController`
  - `KeyboardController`

---

### 2. Keyboard Logging (`main.py`)
- Listens for keyboard key presses in real time  
- Logs:
  - Alphanumeric characters directly  
  - Special keys with readable tags such as:
    - `[ENTER]`
    - `[SPACE]`
    - `[BACKSPACE]`
    - `[SHIFT]`
    - `[CTRL]`
    - Arrow keys  
- Saves all inputs to **log.txt**  
- Includes error handling for unexpected events  

---

### 3. Mouse Movement Tracking (`mouseListener.py`)
- Monitors mouse movement events  
- Prints the current cursor coordinates **(x, y)** whenever the cursor moves  

---

## Usage

Run any script individually:

```bash
python Control.py
python main.py
python mouseListener.py
```
---

## How It Works

This project uses several components from the `pynput` library:

- **MouseController** — programmatically moves the mouse  
- **KeyboardController** — types text automatically  
- **Listener** — captures keyboard or mouse events  

Each script focuses on a different type of input interaction to keep the implementation simple and easy to understand.

---

## Important Notice

This project is intended for **educational and personal use only**.  
Do **not** run input-monitoring code on devices you do not own or without explicit permission.

