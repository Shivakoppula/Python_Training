'''import logging

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
                 
logging.info("Logging is set up.")
logging.warning("This is a warning message.")
logging.error("This is an critical error message.")

'''

import logging
'''logging.basicConfig(level=logging.ERROR)

try:
    result=10/0
except Exception:
    logging.error("An error occurred")
    '''
    
    
logging.basicConfig(level=logging.INFO,
                    format="%(levelname)s - %(message)s")
def getBalance(balance):
    try:
        result=1000/balance
        logging.info("Balance calculation successful: %s", result)
        return result
    except Exception:
        logging.error("An error occurred during balance calculation")
        return None
    
print(getBalance(2))
print(getBalance(0))


