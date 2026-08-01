import uuid
import time

from utils.logger import logger


class AgentTracer:


    def __init__(self):

        self.trace_id = str(
            uuid.uuid4()
        )

        self.start_time = None


    def start(
        self,
        node,
        input=None
    ):

        self.start_time=time.time()

        logger.info(
            f"""
========== TRACE START ==========
trace_id:
{self.trace_id}

node:
{node}

input:
{input}
"""
        )


    def end(
        self,
        output=None
    ):

        if self.start_time is None:
            return
        cost=time.time()-self.start_time


        logger.info(
            f"""
========== TRACE END ==========

trace_id:
{self.trace_id}

cost:
{cost:.3f}s

output:
{output}
"""
        )