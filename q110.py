#Write a script that uses the logging module to log debug, info, warning, and error messages to a file.
import logging

# Set up logging to a file
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Log messages
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")

print("Log messages have been written to app.log.")