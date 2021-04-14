import logging;
import sys

# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s  -%(process)s -%(thread)s - %(levelname)s - %(message)s ')

logger = logging.getLogger(__name__)

class action:
    def run(self):
        logger.info("exception ======")