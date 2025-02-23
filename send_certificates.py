import os
import pandas as pd
import smtplib
from email.message import EmailMessage

# Load the spreadsheet
recipients_file = "recipients.xlsx"
certificates_folder = "certificates"  # Folder where certificates are stored

# Read the data from Excel
data = pd.read_excel(recipients_file)

# Email credentials (Update with your credentials)
SMTP_SERVER = "smtp.gmail.com"  # For Gmail
SMTP_PORT = 587
EMAIL_ADDRESS = ""  # Your Gmail address
EMAIL_PASSWORD = ""  # Your Gmail app password

# Function to send email with certificate attachment
def send_certificate(name, email, certificate_file):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Your Certificate"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        
        # Email body
        msg.set_content(f"Dear {name},\n\nPlease find your certificate attached.\n\nBest regards,\n,\nSukhpreet Singh")
        
        # Attach the PNG certificate
        with open(certificate_file, 'rb') as cert:
            msg.add_attachment(cert.read(), maintype='image', subtype='png', filename=os.path.basename(certificate_file))
        
        # Send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {name} at {email}")
    
    except Exception as e:
        print(f"Failed to send email to {name} at {email}. Error: {e}")

# Iterate through each recipient and send their certificate
for index, row in data.iterrows():
    name = row['Name']
    email = row['Email']
    cert_file = os.path.join(certificates_folder, f"{row['Certificate File']}.png")
    
    # Check if the certificate file exists
    if os.path.exists(cert_file):
        send_certificate(name, email, cert_file)
    else:
        print(f"Certificate file for {name} not found: {cert_file}")
