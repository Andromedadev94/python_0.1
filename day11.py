def tests(x):
    if x < 12:
        raise Exception("argument can not be less than 12")
    y = 3 + x
    assert y < 20   #it says y must be less than 20 or crash
    print(y)
try:
    tests(12)
except Exception as e:
    print("Brother, fuk off", e)
# tests(22)

import logging
logging.disable(logging.CRITICAL)  #to disable the loging after finishing the dubuging
logging.basicConfig(filename="debuglog.txt", level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug("start of program")
for i in range(12):
    logging.debug("value of i = " + str(i))
logging.debug('end of debuging')