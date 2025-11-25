# Voice-Controlled Email Service
This project enables you to interact with your email using voice commands. It includes functionalities to send emails, read inbox messages, and exit the application.
## Features
- **Send Email:** Compose and send emails by speaking recipient's email address and email body.
- **Read Inbox:** Listen to the latest emails in your inbox and hear details such as sender, subject, and body.
- **Voice Interaction:** Entirely controlled by voice commands using speech recognition and text-to-speech capabilities.
## Prerequisites
Before running the script, ensure you have the following dependencies installed:
- `speech_recognition`: For converting speech to text.
- `pyttsx3`: For text-to-speech conversion.
- `smtplib`: For sending emails using SMTP.
- `easyimap`: For accessing emails via IMAP.

Install dependencies using pip:
```bash
pip install SpeechRecognition pyttsx3 easyimap
## Setup
1. **Email Credentials:**
   - Replace `unm` (email) and `pwd` (password) variables in the script with your Gmail credentials.

2. **Voice Configuration:**
   - Adjust the voice settings (`rate` and `voice`) in the `pyttsx3.init()` section based on your preference.

3. **Email Service Configuration:**
   - Ensure your Gmail account allows access to less secure apps or generate an App Password for SMTP access.
## Usage
1. Run the script (`voice_email.py`) in your Python environment.
   ```bash
   python voice_email.py
## Notes
- The script uses Google's Speech Recognition API for speech-to-text conversion. Ensure you have a stable internet connection for accurate recognition.
- For security reasons, avoid hardcoding sensitive information directly in the script when deploying in production environments.
## Acknowledgments
- This script uses Python libraries like `speech_recognition`, `pyttsx3`, `smtplib`, and `easyimap` to integrate voice commands with email functionalities.

---

### Optional Enhancements:
- **Error Handling:** Implement robust error handling for edge cases like unrecognized speech or failed email sends.
- **Multiple Email Providers:** Extend support beyond Gmail by adapting SMTP and IMAP settings accordingly.
- **GUI Integration:** Develop a graphical user interface (GUI) for easier interaction and feedback.

