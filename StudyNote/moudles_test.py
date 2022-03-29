import os
import logging
import html.parser
from html.parser import HTMLParser


print(os.name)
logger = logging.getLogger("Main")
logger.error("Error happened in the App")
logger.info("General info")
logger.warning("Warrning ...")
logger.debug("Debug info")
logger.critical("Critical info...")

ht_parser_element = HTMLParser()
print(ht_parser_element)