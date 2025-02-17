# Keylogger
This repository contains a basic Python keylogger for Windows, built for educational purposes to demonstrate low-level system interaction using ctypes. It captures keystrokes and logs them to keys_log.txt, handling basic text input and Caps Lock. Use responsibly and ethically. This code should only be used for legal and authorized purposes.

**⚠️  WARNING: Use Responsibly and Ethically! ⚠️**

**Keylogging without explicit consent is illegal and unethical.** This code is provided solely for educational purposes to understand system programming and low-level input handling.  **Do not use this code for any malicious or illegal activities.**  You are solely responsible for using this code legally and ethically. Only use this on systems you own or have explicit permission to monitor.

**Features:**

* **Captures Keystrokes:** Records keyboard input in real-time.
* **Logs to File:** Saves captured keystrokes to a text file named `keys_log.txt`.
* **Basic Character Support:** Handles basic alphanumeric characters and Caps Lock (uppercase/lowercase).
* **Uses `ctypes`:**  Demonstrates interaction with the Windows API (`user32.dll`) for low-level system access.
* **Simple Implementation:**  Easy to understand and modify for educational exploration.

**How to Use:**

1. **Prerequisites:**
   * Python 3.x installed on a Windows machine.
   * No external libraries are required as it uses the built-in `ctypes` module.

2. **Download or Clone:**
   * Download the `keylogger.py` file from this repository or clone the entire repository.

3. **Run the Script:**
   * Open a command prompt or terminal.
   * Navigate to the directory where you saved `keylogger.py`.
   * Execute the script using: `python keylogger.py`

4. **Keystroke Logging:**
   * The keylogger will start running in the background.
   * All keystrokes will be recorded and appended to the `keys_log.txt` file in the same directory as the script.
   * To stop the keylogger, you will need to manually terminate the Python process (e.g., close the command prompt window or use Task Manager).

5. **View the Log:**
   * Open the `keys_log.txt` file to see the captured keystrokes.
