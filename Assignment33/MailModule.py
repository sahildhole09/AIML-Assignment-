import smtplib
import os

from email.message import EmailMessage

###############################################################
# Function : SendMail
# Description : Sends log file through Gmail
###############################################################

def SendMail(SenderEmail,AppPassword,ReceiverEmail,LogFile,StartTime,EndTime,Directory,Result):
    try:
        msg = EmailMessage()
        msg["From"] = SenderEmail
        msg["To"] = ReceiverEmail
        msg["Subject"] = "Duplicate File Removal Report"
        Body = (f"""
Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics

Starting Time           : {StartTime}
Completion Time         : {EndTime}

Directory Scanned       : {Directory}

Total Files Scanned     : {Result['TotalFiles']}
Duplicate Files Found   : {Result['DuplicateFiles']}
Duplicate Files Deleted : {len(Result['DeletedFiles'])}

Please find the attached log file.

Regards,
Marvellous Automation System
""")
        msg.set_content(Body)

        f = open(LogFile, "rb")

        FileData = f.read()

        FileName = os.path.basename(LogFile)

        msg.add_attachment(FileData,maintype="application",subtype="octet-stream",filename=FileName)

        smtp = smtplib.SMTP("smtp.gmail.com", 587)

        smtp.starttls()

        smtp.login(SenderEmail, AppPassword)

        smtp.send_message(msg)

        smtp.quit()

        return "Success"

    except Exception as e:
        return "Failed : " + str(e)