import logging


# class logger
logging.basicConfig(filename="C://Users//nagababu.endla//pythonProject1//log//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M')
logger = logging.getLogger();

logger.setLevel(logging.INFO);


logger.debug("debug");
logger.info("info_level");
logger.warning("empty");
logger.error("errors");
logger.critical("high")

# def logger(self):






