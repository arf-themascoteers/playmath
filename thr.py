import threading

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(i)

# Define the ranges
range1 = (1, 100)
range2 = (200, 300)

# Create threads for each range
thread1 = threading.Thread(target=print_numbers, args=range1)
thread2 = threading.Thread(target=print_numbers, args=range2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()