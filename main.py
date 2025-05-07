import datetime
import logging
# file = open('file.txt', mode="a")
# file.write(f"\ndate : {datetime.datetime.now()} ============= User with Create Success....")
# file.close()

with open("file.txt", mode='a') as file:
    file.write(f"\ndate : {datetime.datetime.now()} ============= User with Create Success....")