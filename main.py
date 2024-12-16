import imaplib
import email
from email.header import decode_header
import sys
def connect_to_email(username, password, imap_server="imap.gmail.com"):
    try:
        print("connecting to gmail")
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        return mail

    except Exception as e:
        print(f"Error connecting to main:{e}")
        return None


def delete_emails_by_keyword(main,keyword):
    try:
        mail.select("inbox")

        status, messages = mail.search(None, f'(BODY "{keyword}")')

        if status == "OK":
            email_ids = messages[0].split()
            print(f"Found {len(email_ids)} emails of keyword '{keyword}'")
            
            for email_id in email_ids:

                mail.store(email_id,"+FLAGS","\\Deleted")

            mail.expunge()
            print(f"Deleted{len(email_ids)} emails of keyword '{keyword}'")
        else:
            print("no emails found of that word")
    except Exception as e:
        print("error while deleting")
if __name__ == "__main__":   
   
    email = input("your mail: ")
    password = input("your password: ")

    mail=connect_to_email(email,password)

    if mail:
        keyword=input("enter your keyword: ")

        confirm = input("are you sure?(y/n)")
        if confirm == "y":
            print(f"proceding to delete email with '{keyword}'")
            
        else:
            sys.exit("terminating program")
        delete_emails_by_keyword(mail,keyword)

        mail.logout()
        print("logged out")



           
