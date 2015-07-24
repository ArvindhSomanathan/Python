import threading

def worker():
    """thread worker function"""
    print 'Worker'
    return

threads = []
for i in range(10):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
