import time

def writing_msg(msg_queue):
    while True:
        time.sleep(1)
        if not msg_queue.empty():
            msg = msg_queue.get()
            with open("log.txt", "a", encoding="UTF-8") as f:
                f.write(f"Получено сообщение: {msg}\n")
        with open("log.txt", "a", encoding="UTF-8") as f:
            f.write(f"Жду ))))\n")
