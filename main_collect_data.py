"""
Main Collect Data.
"""
import asyncio
import logging

from humans_not_invited_problem import run_collection_process

N_ITERATIONS = 100
N_PARALLEL_TASKS = 10


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s ~ %(name)s ~ %(levelname)s ~ %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_collection_process(N_ITERATIONS, N_PARALLEL_TASKS))
    loop.close()
