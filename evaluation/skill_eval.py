import json

from skills.loader import load_skills
from skills.router import select_skill


skills = load_skills()


def run_skill_eval():

    with open(
        "evaluation/test_cases.json",
        encoding="utf-8"
    ) as f:

        cases=json.load(f)


    total=0
    passed=0


    print(
        "\n========== Skill Evaluation =========="
    )


    for case in cases:

        if case["type"]!="skill":
            continue


        total+=1


        result=select_skill(
            case["input"],
            skills
        )


        actual=result["name"]


        if actual == case["expected"]:

            print(
                "PASS",
                case["input"],
                actual
            )

            passed+=1


        else:

            print(
                "FAIL",
                case["input"],
                "expected:",
                case["expected"],
                "actual:",
                actual
            )


    accuracy = passed / total


    print(
        f"""
        
Skill Accuracy:
{passed}/{total}

{accuracy:.2%}

"""
    )


if __name__=="__main__":

    run_skill_eval()