import logging
logFormatter = ('TIMESTAMP:%(asctime)s LEVEL:%(levelname)s USER:%(user)s'
                ' MSG:%(message)s')

logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger(__name__)
