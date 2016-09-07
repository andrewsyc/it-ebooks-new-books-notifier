# it-ebooks-new-books-notifier
Sends an email to the address of your choice indicating if new books have been posted to the site to download.

- I run this on a Raspberry Pi, low power usage an on all the time, set a cron job to run it.
- You can use a hosting provider like digital ocean, linode, or vultr to do this; I'm sure you can use Amazon or Google as well.

# How does this work?
- This program bots the home page of it-ebooks.info and then parses the html element with the books. The contents are then md5 hashed and then compared to a database where the previous bot hash is stored. 
- If the hash is new it means there are new books and an email is sent off.

# Dependencies
- SQLAlchemy
- BeautifulSoup4
- PyMySQL
- Python 2.7
- MySQL
