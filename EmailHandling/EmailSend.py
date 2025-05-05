import smtplib
from email.message import EmailMessage
import markdown as Md

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

numberOfGraphImagesToAttach = 0

receiver_email = input(str("What is your email? \n")).lower()
caching_email = receiver_email

def emailSetupAndSend():
    # Set up email details
    sender_email = "wealthiqbot@gmail.com"
    subject = "This is your insight! - WealthIQ Team"
    
    with open("Output.md", "r") as f:
        body = f.read()

    # Convert Markdown to HTML
    html_content = Md.markdown(body)

    # Create the email message
    # Initialize as multipart
    msg = MIMEMultipart()  # <-- This is the critical line!
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Attach the PNG graph file
    for i in range(numberOfGraphImagesToAttach):
        filename = f"graph{i}.png"
        with open(filename, "rb") as f:
            img = MIMEImage(f.read(), "png")
            msg.attach(img)
            
    # Attach HTML
    msg.attach(MIMEText(html_content, 'html'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, 'qkusczydwmuzzjmi')
        server.send_message(msg)
    print("Email sent! Until next time user!")




