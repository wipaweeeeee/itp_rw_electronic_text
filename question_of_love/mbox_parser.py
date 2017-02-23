import mailbox
import csv

def getbody(message): #getting plain text 'email body'
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body


writer = csv.writer(open("me_to_mom.csv", "wb"))
for message in mailbox.mbox('Inbox-2.mbox'):
	body = getbody(message)
	if "wipawe" in message['from'] and 'schuraiporn' in message['to']:
	    writer.writerow([message['subject'], message['from'], message['date'], body])
