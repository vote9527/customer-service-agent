import json

from tools.rag_tool import search_policy


def normalize(text):

    return (
        text
        .replace("–", "-")
        .replace("—", "-")
        .replace(" ", "")
        .lower()
    )


def load_test():

    with open(
        "evaluation/rag_test.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def evaluate():

    tests = load_test()

    total = len(tests)

    success = 0


    for test in tests:

        question = test["question"]

        expected = test["expected"]


        print(
            "\n问题:",
            question
        )


        result = search_policy.invoke(
            {
                "query": question
            }
        )


        print(
            "检索结果:",
            result
        )


        normalized_result = normalize(result)


        matched = 0


        for item in expected:

            if normalize(item) in normalized_result:

                matched += 1



        if matched == len(expected):

            print("✅ PASS")

            success += 1

        else:

            print(
                f"❌ FAIL ({matched}/{len(expected)})"
            )


    print(
        f"\nRAG测试结果:{success}/{total}"
    )

    print(
        f"Accuracy:{success/total:.2%}"
    )



if __name__ == "__main__":

    evaluate()