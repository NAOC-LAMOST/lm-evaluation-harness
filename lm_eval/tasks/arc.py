# REMINDER: this code needs to be rewritten for the new framework. Remove this comment when the code is fully converted.

from . common import HFTask

class ARCEasy(HFTask):
    DATASET_PATH = "ai2_arc"
    DATASET_NAME = "ARC-Easy"

    def has_training_docs(self):
        return True

    def has_validation_docs(self):
        return True

    def has_test_docs(self):
        return True

    def fewshot_description(self):
        # TODO: figure out description
        return ""

    def doc_to_text(self, doc):
        return "Question: " + doc['question'] + '\nAnswer:'

    def doc_to_target(self, doc):
        return " " + doc['choices']['text'][doc['choices']['label'].index(doc['answerKey'])]

    def evaluate(self, docs, lm, provide_description, num_fewshot):
        # TODO: implement
        raise NotImplementedError()

class ARCChallenge(ARCEasy):
    DATASET_PATH = "ai2_arc"
    DATASET_NAME = "ARC-Challenge"