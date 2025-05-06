import smtplib # Simple Mail Transfer Protocol: Responsible for the communication with email services and sending emails.
import markdown as Md # Markdown necessary for compiling the generating response into markdown to have a nice format in the email

from email.mime.multipart import MIMEMultipart # MIME standard object extending the format of input a mail can have, it extends it to having a subject, text, images, videos attached or images
from email.mime.text import MIMEText # Text component of the MIME module (attach the body text from output.md)
from email.mime.image import MIMEImage # Image component of the MIME module (attach the images -> graph0.png for example)

# Documentation for Multipurpose Internet Mail Extension: https://datatracker.ietf.org/doc/html/rfc2045.html

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
    html_content = Md.markdown(body) # Converts markdown text to html format -> # Title = <h1>Title</h1>

    # Create the email message
    # Initialize as multipart
    msg = MIMEMultipart()  # <-- This is the critical line! This part creates a MIME standard mail which can handle many extensions
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Attach the PNG graph file
    for i in range(numberOfGraphImagesToAttach):
        filename = f"graph{i}.png"
        with open(filename, "rb") as f:
            img = MIMEImage(f.read(), "png") # Creates an attachable image document from the file provided.
            msg.attach(img)
            
    # Attach HTML
    msg.attach(MIMEText(html_content, 'html'))
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server: # Create a request to gmail's SMTP services via the port 587, the port responsible for client to server email transfers
        server.starttls()  # Secure the connection via an encryption protocol
        server.login(sender_email, 'qkusczydwmuzzjmi')
        server.send_message(msg)
    print("Email sent! Until next time user!")




