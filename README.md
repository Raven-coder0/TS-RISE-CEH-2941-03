# Educational Keylogger (Python + Tkinter)

A GUI-based keylogging application built with Python, intended **strictly for educational and authorized research use**. It allows users to log keystrokes in real-time, view captured logs through the interface, and manage logging operations safely and ethically.

> ⚠️ This software is for **ethical use only**. It must not be used without explicit permission from the device owner or within unauthorized systems.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Overview

This application demonstrates how a keylogger functions in a controlled and ethical environment. It provides a basic but functional keylogging system where users can:

- Start or stop keystroke logging  
- View captured logs in a readable format  
- Use a safe GUI that avoids stealth or malicious design  

---

## Features

- Keyboard input logging using `pynput`  
- GUI built with Tkinter  
- Log viewer with scrollable display  
- Start/Stop control for real-time logging  
- Ethical use disclaimer on startup  
- Local file-based storage (no data is transmitted externally)  

---

## Technologies Used

| Technology | Purpose                         |
|------------|---------------------------------|
| Python     | Core programming language       |
| Tkinter    | GUI interface                   |
| pynput     | Capturing keyboard events       |
| threading  | Keeps GUI responsive            |
| os         | File operations and path checks |

---

## How It Works

1. **User Interface**  
   - Shows an ethical use disclaimer on startup  
   - Buttons to start or stop the logger  

2. **Key Capture**  
   - Logs stored in `keylog.txt`  
   - Special keys (e.g. Enter, Backspace) are enclosed in brackets  

3. **Log Viewer**  
   - Scrollable popup displays all captured keystrokes  

4. **Threading**  
   - Listener runs in background thread to keep GUI responsive  

---

## Usage

### Prerequisites

- Python 3.x  
- Required package:

```bash
pip install pynput
```

### Running the Application

```bash
python keylogger.py
```

### Output File

- Logs are saved locally in `keylog.txt`  
- File is created in the same directory as the script  

---

## Important Notes

- This tool does **not** run in the background or start automatically  
- Logs are **not** transmitted over any network  
- Use **only** with explicit permission in a controlled environment  

---



## Future Enhancements

| Feature           | Description                              |
|------------------|------------------------------------------|
| Timestamp Logging| Add date/time stamps to each keystroke   |
| Log Encryption   | Secure logs with password-based encryption |
| Export Format    | Enable export to CSV or PDF              |
| Auto-Clear Logs  | Option to clear logs on exit/view        |
| Real-Time Stats  | Show most-typed keys or count live data  |

---

## Disclaimer

This application is built for:  
- Educational demonstrations  
- Cybersecurity awareness training  
- Ethical research and testing  

**⚠️ The developer is not liable for any misuse. Always gain consent before use. Unauthorized deployment is strictly discouraged.**

---

## License

This project is licensed for **educational and ethical use only**. Redistribution or use for malicious intent is prohibited.
