from langchain.prompts import PromptTemplate

COT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the question.

{reflections}
Relevant Context: {context} 
Question: {question}{scratchpad}"""

COT_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task. You will be given context that you should use to help you answer the question.


{reflections}

Relevant Context: {context}
{question}{scratchpad}"""

COT_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to relevant context and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, Diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  


Previous trial:
Relevant Context: {context}
Question: {question}{scratchpad}

Reflection:"""

cot_agent_prompt = PromptTemplate(
                        input_variables=["reflections", "context", "question", "scratchpad"],
                        template = COT_INSTRUCTION,
                        )

cot_reflect_agent_prompt = PromptTemplate(
                        input_variables=["reflections", "context", "question", "scratchpad"],
                        template = COT_AGENT_REFLECT_INSTRUCTION,
                        )

cot_reflect_prompt = PromptTemplate(
                        input_variables=["context", "question", "scratchpad"],
                        template = COT_REFLECT_INSTRUCTION,
                        )

COT_SIMPLE_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

{reflections}
{context}
{question}{scratchpad}"""

COT_SIMPLE_AGENT_REFLECT_INSTRUCTION = """Solve a question answering task by having a Thought, then Finish with your answer. Thought can reason about the current situation. Finish[answer] returns the answer and finishes the task.

{context}
{reflections}

{question}{scratchpad}"""

COT_SIMPLE_REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>] or there is a phrasing discrepancy with your provided answer and the answer key. In a few sentences, Diagnose a possible reason for failure or phrasing discrepancy and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.

{context}
Previous trial:
{question}{scratchpad}

Reflection:"""

cot_simple_agent_prompt = PromptTemplate(
                        input_variables=["question", "reflections", "context", "scratchpad"],
                        template = COT_SIMPLE_INSTRUCTION,
                        )

cot_simple_reflect_agent_prompt = PromptTemplate(
                        input_variables=["context", "reflections", "question", "scratchpad"],
                        template = COT_SIMPLE_AGENT_REFLECT_INSTRUCTION,
                        )

cot_simple_reflect_prompt = PromptTemplate(
                        input_variables=["question", "context", "scratchpad"],
                        template = COT_SIMPLE_REFLECT_INSTRUCTION,
                        )

# TODO(FXY)
REACT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be two types: 
(1) Search[entity], Invoke a local searcher with the chosen keywords or entities to gather relevant information. You only need to complete the thought step and output Search[Entity] in the action step, and we will return the relevant content in \"Observation\" for you. 
(2) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary.

Question: {question}{scratchpad}"""

REACT_REFLECT_INSTRUCTION = """Solve a question answering task with interleaving Thought, Action, Observation steps. Thought can reason about the current situation, and Action can be two types: 
(1) Search[entity], Invoke a local searcher with the chosen keywords or entities to gather relevant information. You only need to complete the thought step and output Search[Entity] in the action step, and we will return the relevant content in \"Observation\" for you. 
(2) Finish[answer], which returns the answer and finishes the task.
You may take as many steps as necessary. 


{reflections}

Question: {question}{scratchpad}"""

REFLECTION_HEADER = 'You have attempted to answer following question before and failed. The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'
REFLECTION_AFTER_LAST_TRIAL_HEADER = 'The following reflection(s) give a plan to avoid failing to answer the question in the same way you did previously. Use them to improve your strategy of correctly answering the given question.\n'
LAST_TRIAL_HEADER = 'You have attempted to answer the following question before and failed. Below is the last trial you attempted to answer the question.\n'

REFLECT_INSTRUCTION = """You are an advanced reasoning agent that can improve based on self refection. You will be given a previous reasoning trial in which you were given access to an local searcher environment and a question to answer. You were unsuccessful in answering the question either because you guessed the wrong answer with Finish[<answer>], or you used up your set number of reasoning steps. In a few sentences, Diagnose a possible reason for failure and devise a new, concise, high level plan that aims to mitigate the same failure. Use complete sentences.  


Previous trial:
Question: {question}{scratchpad}

Reflection:"""
react_agent_prompt = PromptTemplate(
                        input_variables=["question", "scratchpad"],
                        template = REACT_INSTRUCTION,
                        )

react_reflect_agent_prompt = PromptTemplate(
                        input_variables=["reflections", "question", "scratchpad"],
                        template = REACT_REFLECT_INSTRUCTION,
                        )

reflect_prompt = PromptTemplate(
                        input_variables=["question", "scratchpad"],
                        template = REFLECT_INSTRUCTION,
                        )
