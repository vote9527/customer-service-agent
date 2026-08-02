from skills.loader import load_skills
from skills.router import select_skill
import json


skills = load_skills()


def test_skill():

    with open(
        "evaluation/skill_test.json",
        encoding="utf-8"
    ) as f:

        cases=json.load(f)


    success=0


    for case in cases:

        skill=select_skill(
            case["input"],
            skills
        )


        result=skill["name"]


        if result == case["expected_skill"]:
            print(
                "PASS",
                case["input"],
                result
            )
            success+=1

        else:
            print(
                "FAIL",
                case["input"],
                result
            )


    print(
        f"Accuracy:{success}/{len(cases)}"
    )


if __name__=="__main__":
    test_skill()