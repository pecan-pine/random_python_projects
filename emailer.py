import smtplib, ssl,sys

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "ebensonnn32@gmail.com"
password = '1Ohngaeze'
receiver_email = 'aquilegia.taylor2@gmail.com'

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    print(server.ehlo()) # Can be omitted
    server.starttls(context=context) # Secure the connection
    print(server.ehlo()) # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email,receiver_email,' '.join(sys.argv[1:]))
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()