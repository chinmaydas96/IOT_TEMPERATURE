def SendMail():
    import smtplib
    sender = "chinmaydasbat@gmail.com"
    password = "chinmay123"
    receiver = "chinmaydas.etoos@gmail.com"
    content = "Subject:TEMPERTURE ALERT\n\nhello mr B4T\nyour temperature is too high.check your room please."
    mail = smtplib.SMTP_SSL("smtp.gmail.com")
    mail.login(sender, password)
    mail.sendmail(sender,
                  receiver, content)
    mail.quit()
