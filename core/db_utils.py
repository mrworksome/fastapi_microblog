import logging

from core.db import database


async def create_db_client():
    logging.info("Connection DB...")
    await database.connect()
    logging.info("Connected.")


async def shutdown_db_client():
    logging.info("Disconnection DB...")
    await database.disconnect()
    logging.info("Disconnected.")

