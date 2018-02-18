import imaplib
mail = imaplib.IMAP4_SSL('mail.seasonsms.com')
mail.login('imap@seasonsms.com', '@esummit2018')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.
