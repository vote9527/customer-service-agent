from skills.router import select_skill
from utils.logger import logger


class AgentHarness:


    def __init__(
        self,
        skills
    ):

        self.skills = skills



    def prepare(
        self,
        query
    ):

        """
        Agent执行前
        """

        skill = select_skill(
            query,
            self.skills
        )


        if skill:

            logger.info(
                f"""
========== HARNESS ==========
Skill:
{skill["name"]}
=============================
"""
            )

            return {
                "skill": skill,
                "prompt": skill["content"]
            }


        logger.warning(
            f"""
========== NO SKILL ==========
Query:
{query}
=============================
"""
        )


        return {
            "skill":None,
            "prompt":""
        }



    def after(
        self,
        response
    ):

        """
        Agent执行后
        """

        return response