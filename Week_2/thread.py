import threading


class ClassA(threading.Thread):

    def run(self):
        th1 = threading.current_thread()
        print(th1.getName())
        pass


classa = ClassA()
classa.start()

th = threading.current_thread()
print(th.getName())
