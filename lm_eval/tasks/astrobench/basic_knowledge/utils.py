import datasets
import string


def doc_to_text(doc):
    text = f"Question: {doc['question']}\n"

    for i in range(len(doc["options"])):
        text += f"{string.ascii_uppercase[i]}. {doc['options'][i]}\n"

    text += "Answer: "
    return text