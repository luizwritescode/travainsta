from instadm import InstaDM 
from time import sleep

import wikipedia
ney = wikipedia.page("Neymar")
payload = ney.content # Content of page.

if __name__ == "__main__":
    # Auto login
	insta = InstaDM(username='luizhc_', password='', headless=False)
	
	sleep(5)
	# Send message
	insta.sendMessage(user='jamamusics', message=payload, qtd=10)
