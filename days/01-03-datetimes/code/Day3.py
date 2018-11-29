import logging
import os
from datetime import datetime
from time import sleep
from sys import argv

seconds = int(argv[1])

# Get CWD
log_dir = os.getcwd() + '/logs/'

# Create logs folder if it doesn't exist
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set logging
logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filename=log_dir+datetime.today().strftime('%Y%m%d')+'.log',
    level=logging.INFO)


def dummy_function(seconds):
    '''
    A dummy function that creates a log entry on start.
    Sleeps z seconds.
    Then logs upon completion including the timedelta elapsed.
    '''
    # Create a start datetime object
    start_time = datetime.today()

    # Create starting log entry
    logging.info("Beginning dummy function")

    # Sleep z seconds
    sleep(seconds)

    # Create an end datetime object
    end_time = datetime.today()

    # Elapsed time
    elapsed = str(end_time - start_time)

    # Create ending log entry
    logging.info("End of processing. Time elapsed:{}".format(elapsed))


if __name__ == '__main__':
    dummy_function(seconds)
