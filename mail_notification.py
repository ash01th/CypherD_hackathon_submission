
import smtplib
import ssl
from email.message import EmailMessage

def send_email(receiver_email: str, subject: str, body: str, sender_email: str, sender_password: str) -> bool:
    """
    Sends an email using Gmail's SMTP server.

    Args:
        receiver_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The plain text body of the email.
        sender_email (str): The Gmail address of the sender.
        sender_password (str): The app password for the sender's Gmail account.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

   
    context = ssl.create_default_context()

    try:
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        print("Email sent successfully!")
        return True

    except Exception as e:
        print(f"Error: Failed to send email. {e}")
        return False


if __name__ == "__main__":
    SENDER_EMAIL = 'boredman665@gmail.com'
    SENDER_PASSWORD = '#######'
    RECEIVER_EMAIL = "boredman665@gmail.com"  

    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: Make sure you have set GMAIL_USER and GMAIL_APP_PASSWORD in your .env file.")
    else:
        email_subject = "te3st mail 1 Hello from a  Python Function!"
        email_body = """
This email was sent using a reusable Python function.
This is much cleaner and safer!
"""
        success = send_email(
            receiver_email=RECEIVER_EMAIL,
            subject=email_subject,
            body=email_body,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD
        )

        if success:
            print("Function executed correctly.")
        else:
            print("Function encountered an error.")