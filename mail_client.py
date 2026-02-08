import smtplib

sender_email = input("Enter your email: ")
password = input("Enter your password: ")
receiver_email = input("Enter recipient email: ")
message = input("Enter your message: ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  

server.login(sender_email, password)

server.sendmail(sender_email, receiver_email, message)

server.quit()

print("Email sent successfully!")
