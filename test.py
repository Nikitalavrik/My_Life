import multiprocessing


def test_function():
    print("Hi")


t1 = multiprocessing.Process(target=test_function)
t2 = multiprocessing.Process(target=test_function)
t1.start()
t2.start()