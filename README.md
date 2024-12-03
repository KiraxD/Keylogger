

# Keylogger with Webhook Integration (Educational Purpose Only)

## ⚠️ Disclaimer
This project is created for **educational purposes only**. Unauthorized use of this code for tracking or logging keystrokes without explicit user consent is **illegal** and may result in severe penalties under applicable laws.

The author does not condone or take responsibility for any misuse of this software. Use this project **ethically** and ensure compliance with the laws in your jurisdiction.

---

## About
This Python script demonstrates how to capture keystrokes and send them to a webhook URL in JSON format at regular intervals. It is designed to showcase keylogging techniques in an ethical and controlled environment, such as for educational purposes or accessibility tool development.

---

## Features
- Captures keystrokes using the `pynput` library.
- Sends captured keystrokes to a specified webhook as a JSON payload.
- Operates at user-defined intervals (default is 55 seconds).
- Stops execution when the `Esc` key is pressed.

---

## Prerequisites
1. Python 3.7 or later installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install pynput requests
   ```

---

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/keylogger-project.git
   cd keylogger-project
   ```

2. **Set Up the Script**
   - Open `keylogger.py` in a text editor.
   - Replace `'Enter Your webhook URL'` with your webhook URL.

3. **Run the Script**
   ```bash
   python keylogger.py
   ```

4. **Stopping the Script**
   - Press the `Esc` key to stop the script.

---

## Example Webhook Payload
The script sends the following JSON payload to the webhook:

```json
{
  "keystrokes": ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
}
```

---

## Warning
Improper use of this software is prohibited. Before running this code:
- Obtain explicit consent from all users.
- Ensure usage complies with all applicable laws and regulations.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

If you have any questions or need further clarification, feel free to open an issue or contact me.

---

Let me know if you'd like help with anything else!
