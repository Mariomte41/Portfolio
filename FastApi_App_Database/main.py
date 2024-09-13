import logging
import logging.config


from fastapi import FastAPI, HTTPException

logging.config.fileConfig("logging.conf",disable_existing_loggers=False)
logger = logging.getLogger(__name__)
app = FastAPI()


