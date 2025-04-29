import multiprocessing

def task(name):
    print(f"Process {name}: starting")
    # Simulate work
    print(f"Process {name}: finishing")

if __name__ == "__main__":
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=task, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print("All processes completed.")


import threading

def task(name):
    print(f"Thread {name}: starting")
    # Simulate work
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    threads = []
    for i in range(3):
        thread = threading.Thread(target=task, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("All threads completed.")
