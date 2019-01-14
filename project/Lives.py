import time

def funkcija(q,q1,q2):
    while True:
        time.sleep(0.1)
        if(not q1.empty() and not q2.empty()):
            x1 = q1.get()
            x2 = q2.get()
            q.put(1)