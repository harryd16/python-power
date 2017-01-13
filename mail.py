import smtplib

gmailAddress = "compclubpythonpower@gmail.com" 
gmailPassword = "pythonsarestrong"

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(gmailAddress, gmailPassword)

msg = """Hello unclucky victim,

please be aware that your fitbit has now been comprimised.

Cheers,
CompClub
"""

server.sendmail(gmailAddress, "steve.doran@infrastream.com.au", msg)

server.quit()
