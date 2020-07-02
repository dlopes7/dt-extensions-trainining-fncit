import autodynatrace
import requests
import random
import time


@autodynatrace.trace
def query_ship():
    ip = f"192.168.0.{random.randint(1, 20)}"
    try:
        requests.get(f"http://{ip}")
    except:
        pass


def main():
    while True:
        time.sleep(5)
        query_ship()





if __name__ == '__main__':
    main()