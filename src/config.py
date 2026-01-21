import logging

# log message config
logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{", 
    datefmt="%Y-%m-%d %H:%M",
    level=logging.INFO
    )