import string


ZERO_SHORT_COT_PROMPT = (
    "Please think through the options carefully and explain your reasoning step by step. "
    "Then select the correct answer from the options above and return the answer in the format \"Answer: X\" "
    "where X is the correct option (A, B, C, or D). You MUST return \"Answer: X\" at the end.\n"
)

def create_zero_shot_cot_prompt(doc):
    question, options = doc["question"], doc["options"]
    prompt = f"Question: {question}\n\nOptions:\n"
    option_labels = ['A', 'B', 'C', 'D']
    for label, option in zip(option_labels, options):
        prompt += f"{label}. {option.strip()}\n"
    prompt += ZERO_SHORT_COT_PROMPT
    return prompt
