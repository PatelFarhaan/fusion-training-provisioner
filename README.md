# Fusion Automation Script

Selenium-based automation script for managing Oracle Fusion and EBS training user provisioning. Automates Joomla CMS user group assignments, handles training access for 90+ Oracle courses, and generates code templates for bulk operations.

## Tech Stack

- **Language:** Python 3.6+
- **Automation:** Selenium WebDriver
- **Email:** SMTP (Gmail)
- **Data:** Google Sheets API (gspread), Pandas
- **CMS:** Joomla (automated via Selenium)

## Features

- Automated Joomla user group assignment for training modules
- Support for 90+ Oracle training courses (Fusion, EBS, Middleware)
- Single training and package provisioning workflows
- Code generation utility (`defin.py`) for bulk Selenium function creation
- Automated onboarding email delivery with training credentials
- Existing user detection and re-enrollment handling

## Prerequisites

- Python 3.6+
- Google Chrome browser
- ChromeDriver (matching Chrome version)
- Gmail account with App Password enabled

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/Fusion-Automation-Script.git
cd Fusion-Automation-Script

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your credentials
```

## Environment Variables

| Variable | Description |
|---|---|
| `JOOMLA_ADMIN_URL` | Joomla admin panel URL |
| `JOOMLA_ADMIN_USERNAME` | Joomla admin panel username |
| `JOOMLA_ADMIN_PASSWORD` | Joomla admin panel password |
| `SMTP_HOST` | SMTP server host (default: smtp.gmail.com) |
| `SMTP_PORT` | SMTP server port (default: 587) |
| `SMTP_USERNAME` | SMTP email address |
| `SMTP_PASSWORD` | SMTP email password or app password |
| `TRAINING_PASSWORDS_FILE` | Path to training passwords JSON config file |
| `GOOGLE_SERVICE_ACCOUNT_JSON` | Path to Google service account JSON key file |

## How to Run

```bash
# Activate virtual environment
source venv/bin/activate

# Copy and configure training passwords
cp training_passwords.json.example training_passwords.json
# Edit training_passwords.json with actual training passwords

# Load environment variables
source .env

# Run the automation script
python app.py
```

## Project Structure

```
Fusion-Automation-Script/
├── app.py              # Main automation script with Selenium workflows
├── defin.py            # Code generator for training function templates
├── requirements.txt                  # Python dependencies
├── training_passwords.json.example   # Training password config template
└── .env.example                      # Environment variable template
```

## License

MIT
