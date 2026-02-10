
import smtplib

receiver_email = input("Enter recipient email: ")
message = input("Enter your message: ")

sender_email = "client@localhost"

server = smtplib.SMTP("localhost", 1025)

server.sendmail(sender_email, receiver_email, message)

server.quit()

print("Mail transferred successfully!")

#using goggle service
'''
import smtplib

sender_email = "kudakemruganksha30@gmail.com"        
sender_password = "mibg fmug hmep twqz"   

receiver_email = input("Enter recipient email: ")
message = input("Enter your message: ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  

server.login(sender_email, sender_password)

server.sendmail(sender_email, receiver_email, message)

server.quit()

print("Email sent successfully!")
'''

