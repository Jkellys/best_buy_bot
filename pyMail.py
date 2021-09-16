import smtplib, ssl

def send_email(item_url):

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = ""
    password = ''

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here

        sender_email = ""
        receiver_email = ""
        message =  """\
Subject: ITEM FOUND

This message is sent from Python.""" + str(item_url)


        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        # Print any error messages to stdout
        print('email not sent')
        print(e)
    finally:
        server.quit()
