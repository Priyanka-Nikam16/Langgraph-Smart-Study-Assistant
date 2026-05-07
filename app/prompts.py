CLASSIFIER_PROMPT = """
You are a strict classifier.
Given a question, output ONLY one word:
- THEORY → if the question asks for an explanation or concept
- CODE → if the question asks for implementation or programming

Output exactly THEORY or CODE in uppercase. No punctuation, no extra words.
Question: {question}
Answer:
"""

THEORY_PROMPT="""
You are a theory node.Provide a detailed explaination of the following concept in simple and clear way.
Question:{question}
"""

CODE_PROMPT="""
You are a code node.Provide a code implementation and explaination for the following task.
Question: {question}
"""