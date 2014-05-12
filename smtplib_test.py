import smtplib

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = 'ljuliom@gmail.com'
toaddrs  = 'martin@cursostotales.com'
message = "Hello, this is dog"

#Change according to your settings
smtp_server = 'email-smtp.us-west-2.amazonaws.com'
smtp_username = 'AKIAIV6T42MW6UH27T2Q'
smtp_password = 'AjPjKOpEqz4HhTcXFIwtUKoD6H1/ayYVVxGVIBVcjrfj'
smtp_port = '587'
smtp_do_tls = True

server = smtplib.SMTP(
    host = smtp_server,
    port = smtp_port,
    timeout = 10
)
server.set_debuglevel(10)
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
server.sendmail(fromaddr, toaddrs, message)
print server.quit()