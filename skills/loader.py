from pathlib import Path


SKILL_DIR = Path("skills")


def load_skills():

    skills={}


    for file in SKILL_DIR.glob("*.md"):

        skills[file.stem]={
            "name":file.stem,
            "content":
                file.read_text(
                    encoding="utf-8"
                )
        }


    return skills