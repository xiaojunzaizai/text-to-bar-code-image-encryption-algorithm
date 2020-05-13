import encryption_decryption
import random
import time

Alpha_dir = {i:chr(i) for i in range(32,127)}

def get_message():
    message = ''
    for i in range(1024):
        message += Alpha_dir[random.randint(32,126)]
    return message

def iteration(n):
    start = time.time()
    for i in range(n):
        message = get_message()
        encryption_decryption.encrytpion(message)
        if i == 0:
            stop0 = time.time()
            print('iteration ', str(i+1),'   finished','     Total message size: ',str(i+1)+'KB   ','      spend:',str(stop0 - start))
        if i == 39:
            stop1 = time.time()
            print('iteration ', str(i+1),'  finished','     Total message size: ',str(i+1)+'KB  ','      spend:',str(stop1 - start))
        if i == 74:
            stop2 = time.time()
            print('iteration ', str(i+1),'  finished','     Total message size: ',str(i+1)+'KB  ','      spend:',str(stop2 - start))
        if i == 124:
            stop3 = time.time()
            print('iteration ', str(i+1),' finished','     Total message size: ',str(i+1)+'KB ','      spend:',str(stop3 - start))
        if i ==159 :
            stop4 = time.time()
            print('iteration ', str(i+1),' finished','     Total message size: ',str(i+1)+'KB ','      spend:',str(stop4 - start))
        if i == 199:
            stop5 = time.time()
            print('iteration ', str(i+1),' finished','     Total message size: ',str(i+1)+'KB ','      spend:',str(stop5 - start))
        if i == 1023:
            stop6 = time.time()
            print('iteration ', str(i+1),'finished','     Total message size: ',str(i+1)+'KB','      spend:',str(stop6 - start))

iteration(1025)    






