# Basic-Mail-Sender

A simple and lightweight Python application for sending emails with ease.

## Description

Basic-Mail-Sender is a straightforward Python project designed to facilitate email sending functionality. Whether you're looking to automate email notifications, send bulk messages, or integrate email capabilities into your application, this project provides a clean and easy-to-use interface.

## Features

- ✉️ Simple email sending functionality
- 🔧 Easy configuration
- 📧 Support for multiple recipients
- 🛡️ Secure credential management
- 🚀 Lightweight and dependency-friendly

## Requirements

- Python 3.6+
- Standard library modules (smtplib, email)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CiprianPesu/Basic-Mail-Sender.git
cd Basic-Mail-Sender
```

2. Install any required dependencies (if applicable):
```bash
pip install -r requirements.txt
```

## Usage

Basic usage example:

```python
from mail_sender import send_email

send_email(
    sender='your_email@gmail.com',
    password='your_app_password',
    recipients=['recipient@example.com'],
    subject='Hello!',
    body='This is a test email.'
)
```

## Configuration

Configure your email settings:
- **Sender Email**: Your email address
- **SMTP Server**: Gmail (smtp.gmail.com) or your email provider's SMTP server
- **Port**: Typically 587 (TLS) or 465 (SSL)

## Author

[CiprianPesu](https://github.com/CiprianPesu)

## Support

For questions or issues, please open an [Issue](https://github.com/CiprianPesu/Basic-Mail-Sender/issues) on GitHub.
