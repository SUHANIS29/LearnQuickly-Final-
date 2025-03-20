# # # # # # import streamlit as st
# # # # # # import json
# # # # # # import os
# # # # # # from dotenv import load_dotenv
# # # # # # import google.generativeai as genai  # Gemini AI SDK
# # # # # # #from google import genai
# # # # # # # Load environment variables
# # # # # # load_dotenv()
# # # # # # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # # # # # # Function to fetch MCQs using Gemini AI
# # # # # # @st.cache_data
# # # # # # def fetch_questions(text_content, quiz_level):
# # # # # #     PROMPT_TEMPLATE = f"""
# # # # # #     You are an AI that generates MCQs based on a given text. 
# # # # # #     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text:

# # # # # #     Text: {text_content}

# # # # # #     Format your response strictly as JSON:
# # # # # #     {{
# # # # # #       "mcqs": [
# # # # # #         {{
# # # # # #             "mcq": "Question 1 here?",
# # # # # #             "options": {{
# # # # # #                 "a": "Option 1",
# # # # # #                 "b": "Option 2",
# # # # # #                 "c": "Option 3",
# # # # # #                 "d": "Option 4"
# # # # # #             }},
# # # # # #             "correct": "a"
# # # # # #         }},
# # # # # #         {{
# # # # # #             "mcq": "Question 2 here?",
# # # # # #             "options": {{
# # # # # #                 "a": "Option 1",
# # # # # #                 "b": "Option 2",
# # # # # #                 "c": "Option 3",
# # # # # #                 "d": "Option 4"
# # # # # #             }},
# # # # # #             "correct": "b"
# # # # # #         }},
# # # # # #         {{
# # # # # #             "mcq": "Question 3 here?",
# # # # # #             "options": {{
# # # # # #                 "a": "Option 1",
# # # # # #                 "b": "Option 2",
# # # # # #                 "c": "Option 3",
# # # # # #                 "d": "Option 4"
# # # # # #             }},
# # # # # #             "correct": "c"
# # # # # #         }}
# # # # # #       ]
# # # # # #     }}
# # # # # #     """

# # # # # #     model = genai.GenerativeModel("gemini-1.5-pro-002")  # Ensure the correct model is used
# # # # # #     response = model.generate_content(PROMPT_TEMPLATE)

# # # # # #     try:
# # # # # #         extracted_response = response.text.strip()  # Extract text response
# # # # # #         parsed_response = json.loads(extracted_response)
# # # # # #         return parsed_response.get("mcqs", [])
# # # # # #     except json.JSONDecodeError:
# # # # # #         st.error("Failed to generate a valid quiz. Please try again.")
# # # # # #         return []

# # # # # # def main():
# # # # # #     st.title("MCQ Generator App")

# # # # # #     text_content = st.text_area("Paste the text content here:")
# # # # # #     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

# # # # # #     if st.button("Generate Quiz"):
# # # # # #         if not text_content.strip():
# # # # # #             st.error("Please enter some text before generating the quiz.")
# # # # # #             return
        
# # # # # #         questions = fetch_questions(text_content, quiz_level)

# # # # # #         if not questions:
# # # # # #             return

# # # # # #         # Store user responses
# # # # # #         selected_options = {}
# # # # # #         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

# # # # # #         st.session_state["questions"] = questions
# # # # # #         st.session_state["selected_options"] = selected_options
# # # # # #         st.session_state["correct_answers"] = correct_answers

# # # # # #     if "questions" in st.session_state:
# # # # # #         st.subheader("Quiz:")
# # # # # #         for i, question in enumerate(st.session_state["questions"]):
# # # # # #             st.write(question["mcq"])
# # # # # #             options = question["options"]
# # # # # #             selected_options[question["mcq"]] = st.radio(
# # # # # #                 f"Select an answer for: {question['mcq']}",
# # # # # #                 options=list(options.values()),
# # # # # #                 key=f"q_{i}"
# # # # # #             )

# # # # # #         if st.button("Submit"):
# # # # # #             score = sum(
# # # # # #                 1 for q in st.session_state["questions"]
# # # # # #                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
# # # # # #             )

# # # # # #             st.subheader("Quiz Result:")
# # # # # #             for question in st.session_state["questions"]:
# # # # # #                 st.write(f"**{question['mcq']}**")
# # # # # #                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
# # # # # #                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")
            
# # # # # #             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# # # # # # if __name__ == "__main__":
# # # # # #     main()
# # # # # import streamlit as st
# # # # # import json
# # # # # import os
# # # # # from dotenv import load_dotenv
# # # # # import google.generativeai as genai  # Gemini AI SDK

# # # # # # Load environment variables
# # # # # load_dotenv()
# # # # # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # # # # # Function to fetch MCQs using Gemini AI
# # # # # @st.cache_data
# # # # # def fetch_questions(text_content, quiz_level):
# # # # #     PROMPT_TEMPLATE = f"""
# # # # #     You are an AI that generates MCQs based on a given text. 
# # # # #     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text:

# # # # #     Text: {text_content}

# # # # #     Format your response strictly as JSON:
# # # # #     {{
# # # # #       "mcqs": [
# # # # #         {{"mcq": "Question 1?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "a"}},
# # # # #         {{"mcq": "Question 2?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "b"}},
# # # # #         {{"mcq": "Question 3?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "c"}}
# # # # #       ]
# # # # #     }}
# # # # #     """

# # # # #     try:
# # # # #         model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model is used
# # # # #         response = model.generate_content(PROMPT_TEMPLATE)

# # # # #         # Extract response text
# # # # #         response_text = response.candidates[0].content if response.candidates else ""
# # # # #         if not response_text:
# # # # #             st.error("Gemini did not return a response.")
# # # # #             return []

# # # # #         # Find JSON part in response
# # # # #         start_idx = response_text.find("{")
# # # # #         end_idx = response_text.rfind("}") + 1
# # # # #         json_text = response_text[start_idx:end_idx]

# # # # #         # Parse JSON
# # # # #         parsed_response = json.loads(json_text)
# # # # #         return parsed_response.get("mcqs", [])

# # # # #     except json.JSONDecodeError:
# # # # #         st.error("Failed to parse Gemini's response. Try again.")
# # # # #         return []
# # # # #     except Exception as e:
# # # # #         st.error(f"Unexpected error: {str(e)}")
# # # # #         return []

# # # # # def main():
# # # # #     st.title("MCQ Generator App")

# # # # #     text_content = st.text_area("Paste the text content here:")
# # # # #     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

# # # # #     if st.button("Generate Quiz"):
# # # # #         if not text_content.strip():
# # # # #             st.error("Please enter some text before generating the quiz.")
# # # # #             return
        
# # # # #         questions = fetch_questions(text_content, quiz_level)

# # # # #         if not questions:
# # # # #             return

# # # # #         # Store user responses
# # # # #         selected_options = {}
# # # # #         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

# # # # #         st.session_state["questions"] = questions
# # # # #         st.session_state["selected_options"] = selected_options
# # # # #         st.session_state["correct_answers"] = correct_answers

# # # # #     if "questions" in st.session_state:
# # # # #         st.subheader("Quiz:")
# # # # #         for i, question in enumerate(st.session_state["questions"]):
# # # # #             st.write(question["mcq"])
# # # # #             options = question["options"]
# # # # #             selected_options[question["mcq"]] = st.radio(
# # # # #                 f"Select an answer for: {question['mcq']}",
# # # # #                 options=list(options.values()),
# # # # #                 key=f"q_{i}"
# # # # #             )

# # # # #         if st.button("Submit"):
# # # # #             score = sum(
# # # # #                 1 for q in st.session_state["questions"]
# # # # #                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
# # # # #             )

# # # # #             st.subheader("Quiz Result:")
# # # # #             for question in st.session_state["questions"]:
# # # # #                 st.write(f"**{question['mcq']}**")
# # # # #                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
# # # # #                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")

# # # # #             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# # # # # if __name__ == "__main__":
# # # # #     main()
# # # # import streamlit as st
# # # # import json
# # # # import os
# # # # from dotenv import load_dotenv
# # # # import google.generativeai as genai  # Gemini AI SDK

# # # # # Load environment variables
# # # # load_dotenv()
# # # # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # # # # Function to fetch MCQs using Gemini AI
# # # # @st.cache_data
# # # # def fetch_questions(text_content, quiz_level):
# # # #     PROMPT_TEMPLATE = f"""
# # # #     You are an AI that generates MCQs based on a given text. 
# # # #     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text:

# # # #     Text: {text_content}

# # # #     Format your response strictly as JSON:
# # # #     {{
# # # #       "mcqs": [
# # # #         {{"mcq": "Question 1?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "a"}},
# # # #         {{"mcq": "Question 2?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "b"}},
# # # #         {{"mcq": "Question 3?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "c"}}
# # # #       ]
# # # #     }}
# # # #     """

# # # #     try:
# # # #         model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model is used
# # # #         response = model.generate_content(PROMPT_TEMPLATE)

# # # #         # ✅ Fix: Extract response safely
# # # #         response_text = response.text if hasattr(response, "text") else ""
# # # #         if not response_text:
# # # #             st.error("Gemini did not return a valid response.")
# # # #             return []

# # # #         # ✅ Fix: Try parsing JSON safely
# # # #         try:
# # # #             parsed_response = json.loads(response_text)
# # # #             return parsed_response.get("mcqs", [])
# # # #         except json.JSONDecodeError:
# # # #             st.error("Failed to parse Gemini's response. Try again.")
# # # #             st.text_area("Raw Response Debug:", response_text)  # Debugging info
# # # #             return []

# # # #     except Exception as e:
# # # #         st.error(f"Unexpected error: {str(e)}")
# # # #         return []

# # # # def main():
# # # #     st.title("MCQ Generator App")

# # # #     text_content = st.text_area("Paste the text content here:")
# # # #     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

# # # #     if st.button("Generate Quiz"):
# # # #         if not text_content.strip():
# # # #             st.error("Please enter some text before generating the quiz.")
# # # #             return
        
# # # #         questions = fetch_questions(text_content, quiz_level)

# # # #         if not questions:
# # # #             return

# # # #         # Store user responses
# # # #         selected_options = {}
# # # #         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

# # # #         st.session_state["questions"] = questions
# # # #         st.session_state["selected_options"] = selected_options
# # # #         st.session_state["correct_answers"] = correct_answers

# # # #     if "questions" in st.session_state:
# # # #         st.subheader("Quiz:")
# # # #         for i, question in enumerate(st.session_state["questions"]):
# # # #             st.write(question["mcq"])
# # # #             options = question["options"]
# # # #             selected_options[question["mcq"]] = st.radio(
# # # #                 f"Select an answer for: {question['mcq']}",
# # # #                 options=list(options.values()),
# # # #                 key=f"q_{i}"
# # # #             )

# # # #         if st.button("Submit"):
# # # #             score = sum(
# # # #                 1 for q in st.session_state["questions"]
# # # #                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
# # # #             )

# # # #             st.subheader("Quiz Result:")
# # # #             for question in st.session_state["questions"]:
# # # #                 st.write(f"**{question['mcq']}**")
# # # #                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
# # # #                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")

# # # #             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# # # # if __name__ == "__main__":
# # # #     main()
# # # import streamlit as st
# # # import json
# # # import os
# # # from dotenv import load_dotenv
# # # import google.generativeai as genai  # Gemini AI SDK

# # # # Load environment variables
# # # load_dotenv()
# # # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # # # Function to fetch MCQs using Gemini AI
# # # @st.cache_data
# # # def fetch_questions(text_content, quiz_level):
# # #     PROMPT_TEMPLATE = f"""
# # #     You are an AI that generates MCQs based on a given text. 
# # #     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text:

# # #     Text: {text_content}

# # #     Format your response strictly as JSON:
# # #     {{
# # #       "mcqs": [
# # #         {{"mcq": "Question 1?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "a"}},
# # #         {{"mcq": "Question 2?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "b"}},
# # #         {{"mcq": "Question 3?", "options": {{"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"}}, "correct": "c"}}
# # #       ]
# # #     }}
# # #     """

# # #     try:
# # #         model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model is used
# # #         response = model.generate_content(PROMPT_TEMPLATE)

# # #         # ✅ Debugging: Check raw AI response
# # #         response_text = response.text if hasattr(response, "text") else ""
# # #         return response_text  # Raw response return kar raha hoon

# # #     except Exception as e:
# # #         return f"ERROR: {str(e)}"

# # # def main():
# # #     st.title("MCQ Generator App")

# # #     text_content = st.text_area("Paste the text content here:")
# # #     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

# # #     if st.button("Generate Quiz"):
# # #         if not text_content.strip():
# # #             st.error("Please enter some text before generating the quiz.")
# # #             return
        
# # #         raw_response = fetch_questions(text_content, quiz_level)  # Fetch raw response

# # #         # ✅ Debugging: Show raw response to user
# # #         st.text_area("Raw Gemini Response (Debugging)", raw_response, height=200)

# # #         # ✅ Try parsing JSON safely
# # #         try:
# # #             parsed_response = json.loads(raw_response)
# # #             questions = parsed_response.get("mcqs", [])
# # #         except json.JSONDecodeError:
# # #             st.error("Failed to parse Gemini's response. Try again.")
# # #             return

# # #         if not questions:
# # #             st.error("Gemini did not return valid questions.")
# # #             return

# # #         # Store user responses
# # #         selected_options = {}
# # #         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

# # #         st.session_state["questions"] = questions
# # #         st.session_state["selected_options"] = selected_options
# # #         st.session_state["correct_answers"] = correct_answers

# # #     if "questions" in st.session_state:
# # #         st.subheader("Quiz:")
# # #         for i, question in enumerate(st.session_state["questions"]):
# # #             st.write(question["mcq"])
# # #             options = question["options"]
# # #             selected_options[question["mcq"]] = st.radio(
# # #                 f"Select an answer for: {question['mcq']}",
# # #                 options=list(options.values()),
# # #                 key=f"q_{i}"
# # #             )

# # #         if st.button("Submit"):
# # #             score = sum(
# # #                 1 for q in st.session_state["questions"]
# # #                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
# # #             )

# # #             st.subheader("Quiz Result:")
# # #             for question in st.session_state["questions"]:
# # #                 st.write(f"**{question['mcq']}**")
# # #                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
# # #                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")

# # #             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# # # if __name__ == "__main__":
# # #     main()

# # import streamlit as st
# # import json
# # import os
# # from dotenv import load_dotenv
# # import google.generativeai as genai  # Gemini AI SDK

# # # Load environment variables
# # load_dotenv()
# # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # # Function to fetch MCQs using Gemini AI
# # @st.cache_data
# # def fetch_questions(text_content, quiz_level):
# #     PROMPT_TEMPLATE = f"""
# #     You are an AI that generates MCQs based on a given text. 
# #     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text.

# #     Text: {text_content}

# #     IMPORTANT:
# #     - Respond **only** in JSON format. No extra text.
# #     - If unsure, return an empty JSON.

# #     Format your response as:
# #     {{
# #       "mcqs": [
# #         {{
# #             "mcq": "Question 1?",
# #             "options": {{
# #                 "a": "Option A",
# #                 "b": "Option B",
# #                 "c": "Option C",
# #                 "d": "Option D"
# #             }},
# #             "correct": "a"
# #         }},
# #         {{
# #             "mcq": "Question 2?",
# #             "options": {{
# #                 "a": "Option A",
# #                 "b": "Option B",
# #                 "c": "Option C",
# #                 "d": "Option D"
# #             }},
# #             "correct": "b"
# #         }},
# #         {{
# #             "mcq": "Question 3?",
# #             "options": {{
# #                 "a": "Option A",
# #                 "b": "Option B",
# #                 "c": "Option C",
# #                 "d": "Option D"
# #             }},
# #             "correct": "c"
# #         }}
# #       ]
# #     }}
# #     """

# #     try:
# #         model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model
# #         response = model.generate_content(PROMPT_TEMPLATE)

# #         # ✅ Debugging: Check raw AI response
# #         response_text = response.text if hasattr(response, "text") else ""
# #         return response_text  # Raw response return kar raha hoon

# #     except Exception as e:
# #         return f"ERROR: {str(e)}"

# # def main():
# #     st.title("MCQ Generator App")

# #     text_content = st.text_area("Paste the text content here:")
# #     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

# #     if st.button("Generate Quiz"):
# #         if not text_content.strip():
# #             st.error("Please enter some text before generating the quiz.")
# #             return
        
# #         raw_response = fetch_questions(text_content, quiz_level)  # Fetch raw response

# #         # ✅ Debugging: Show raw response to user
# #         st.text_area("Raw Gemini Response (Debugging)", raw_response, height=200)

# #         # ✅ Try parsing JSON safely
# #         try:
# #             parsed_response = json.loads(raw_response)
# #             questions = parsed_response.get("mcqs", [])

# #             if not questions:
# #                 st.error("Gemini did not return valid questions.")
# #                 return
# #         except json.JSONDecodeError:
# #             st.error("Failed to parse Gemini's response. Try again.")
# #             return

# #         # Store user responses
# #         selected_options = {}
# #         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

# #         st.session_state["questions"] = questions
# #         st.session_state["selected_options"] = selected_options
# #         st.session_state["correct_answers"] = correct_answers

# #     if "questions" in st.session_state:
# #         st.subheader("Quiz:")
# #         for i, question in enumerate(st.session_state["questions"]):
# #             st.write(question["mcq"])
# #             options = question["options"]
# #             selected_options[question["mcq"]] = st.radio(
# #                 f"Select an answer for: {question['mcq']}",
# #                 options=list(options.values()),
# #                 key=f"q_{i}"
# #             )

# #         if st.button("Submit"):
# #             score = sum(
# #                 1 for q in st.session_state["questions"]
# #                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
# #             )

# #             st.subheader("Quiz Result:")
# #             for question in st.session_state["questions"]:
# #                 st.write(f"**{question['mcq']}**")
# #                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
# #                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")

# #             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# # if __name__ == "__main__":
# #     main()
# import streamlit as st
# import json
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key

# # Function to fetch MCQs using Gemini AI
# @st.cache_data
# def fetch_questions(text_content, quiz_level):
#     PROMPT_TEMPLATE = f"""
#     You are an AI that generates MCQs based on a given text. 
#     Please create 3 multiple-choice questions (MCQs) at a {quiz_level} level based on the following text.

#     Text: {text_content}

#     IMPORTANT:
#     - Respond **only** in JSON format. No extra text.
#     - Do **not** add explanations.
#     - JSON should be inside triple backticks (```) to avoid parsing issues.

#     Format your response:
#     ```
#     {{
#       "mcqs": [
#         {{
#             "mcq": "Question 1?",
#             "options": {{
#                 "a": "Option A",
#                 "b": "Option B",
#                 "c": "Option C",
#                 "d": "Option D"
#             }},
#             "correct": "a"
#         }},
#         {{
#             "mcq": "Question 2?",
#             "options": {{
#                 "a": "Option A",
#                 "b": "Option B",
#                 "c": "Option C",
#                 "d": "Option D"
#             }},
#             "correct": "b"
#         }},
#         {{
#             "mcq": "Question 3?",
#             "options": {{
#                 "a": "Option A",
#                 "b": "Option B",
#                 "c": "Option C",
#                 "d": "Option D"
#             }},
#             "correct": "c"
#         }}
#       ]
#     }}
#     ```
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model
#         response = model.generate_content(PROMPT_TEMPLATE)

#         # ✅ Debugging: Check raw AI response
#         response_text = response.text if hasattr(response, "text") else ""
        
#         # ✅ Extract JSON from triple backticks
#         start_idx = response_text.find("```") + 3
#         end_idx = response_text.rfind("```")
#         json_text = response_text[start_idx:end_idx].strip() if start_idx > 2 and end_idx > start_idx else response_text

#         # ✅ Try parsing JSON safely
#         parsed_response = json.loads(json_text)
#         return parsed_response.get("mcqs", [])

#     except json.JSONDecodeError:
#         st.error("Failed to parse Gemini's response. Try again.")
#         return []
#     except Exception as e:
#         st.error(f"Unexpected error: {str(e)}")
#         return []

# def main():
#     st.title("MCQ Generator App")

#     text_content = st.text_area("Paste the text content here:")
#     quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

#     if st.button("Generate Quiz"):
#         if not text_content.strip():
#             st.error("Please enter some text before generating the quiz.")
#             return
        
#         questions = fetch_questions(text_content, quiz_level)

#         if not questions:
#             return

#         # Store user responses
#         selected_options = {}
#         correct_answers = {q["mcq"]: q["options"][q["correct"]] for q in questions}

#         st.session_state["questions"] = questions
#         st.session_state["selected_options"] = selected_options
#         st.session_state["correct_answers"] = correct_answers

#     if "questions" in st.session_state:
#         st.subheader("Quiz:")
#         for i, question in enumerate(st.session_state["questions"]):
#             st.write(question["mcq"])
#             options = question["options"]
#             selected_options[question["mcq"]] = st.radio(
#                 f"Select an answer for: {question['mcq']}",
#                 options=list(options.values()),
#                 key=f"q_{i}"
#             )

#         if st.button("Submit"):
#             score = sum(
#                 1 for q in st.session_state["questions"]
#                 if st.session_state["selected_options"][q["mcq"]] == st.session_state["correct_answers"][q["mcq"]]
#             )

#             st.subheader("Quiz Result:")
#             for question in st.session_state["questions"]:
#                 st.write(f"**{question['mcq']}**")
#                 st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
#                 st.write(f"📝 Your answer: {st.session_state['selected_options'][question['mcq']]}")

#             st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

# if __name__ == "__main__":
#     main()
import streamlit as st
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini AI SDK

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Use Gemini API key
st.markdown("""
<style>
                 .title {
            font-size: 2.5rem;
            font-weight: 600;
            background: linear-gradient(90deg, #D13F77, #F68D2E);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }
</style>
""", unsafe_allow_html=True)
# Function to fetch MCQs using Gemini AI
@st.cache_data
def fetch_questions(text_content, quiz_level):
    PROMPT_TEMPLATE = f"""
    You are an AI that generates MCQs based on a given text. 
    Please create multiple-choice questions baserd on your analysis (MCQs) at a {quiz_level} level based on the following text.

    Text: {text_content}

    IMPORTANT:
    - Respond **only** in JSON format. No extra text.
    - Do **not** add explanations.
    - JSON should be inside triple backticks (```) to avoid parsing issues.

    Format your response:
    ```
    {{
      "mcqs": [
        {{
            "mcq": "Question 1?",
            "options": {{
                "a": "Option A",
                "b": "Option B",
                "c": "Option C",
                "d": "Option D"
            }},
            "correct": "a"
        }},
       
      ]
    }}
    ```
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model
        response = model.generate_content(PROMPT_TEMPLATE)

        # ✅ Debugging: Check raw AI response
        response_text = response.text if hasattr(response, "text") else ""
        
        # ✅ Extract JSON from triple backticks
        start_idx = response_text.find("```") + 3
        end_idx = response_text.rfind("```")
        json_text = response_text[start_idx:end_idx].strip() if start_idx > 2 and end_idx > start_idx else response_text

        # ✅ Try parsing JSON safely
        parsed_response = json.loads(json_text)
        return parsed_response.get("mcqs", [])

    except json.JSONDecodeError:
        st.error("Failed to parse Gemini's response. Try again.")
        return []
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return []

def main():
    # st.title("MCQ Generator App")
    st.markdown("<h1 class='title'>✨ MCQ Generator ✨</h1>", unsafe_allow_html=True)

    text_content = st.text_area("Paste the text content here:")
    quiz_level = st.selectbox("Select quiz level:", ["Easy", "Medium", "Hard"]).lower()

    if st.button("Generate Quiz"):
        if not text_content.strip():
            st.error("Please enter some text before generating the quiz.")
            return
        
        questions = fetch_questions(text_content, quiz_level)

        if not questions:
            return

        # ✅ Initialize selected_options properly
        st.session_state["selected_options"] = {}

        # ✅ Store correct answers
        st.session_state["correct_answers"] = {q["mcq"]: q["options"][q["correct"]] for q in questions}

        # ✅ Store questions in session state
        st.session_state["questions"] = questions

    if "questions" in st.session_state:
        st.subheader("Quiz:")
        
        for i, question in enumerate(st.session_state["questions"]):
            st.write(question["mcq"])
            options = question["options"]

            # ✅ Prevents default selection by setting `index=None`
            st.session_state["selected_options"][question["mcq"]] = st.radio(
                f"Select an answer for:",
                options=list(options.values()),
                key=f"q_{i}",
                index=None
            )

        if st.button("Submit"):
            score = sum(
                1 for q in st.session_state["questions"]
                if st.session_state["selected_options"].get(q["mcq"], "") == st.session_state["correct_answers"][q["mcq"]]
            )

            st.subheader("Quiz Result:")
            for question in st.session_state["questions"]:
                st.write(f"**{question['mcq']}**")
                st.write(f"✅ Correct answer: {st.session_state['correct_answers'][question['mcq']]}")
                st.write(f"📝 Your answer: {st.session_state['selected_options'].get(question['mcq'], 'No answer selected')}")

            st.subheader(f"Final Score: {score} / {len(st.session_state['questions'])}")

if __name__ == "__main__":
    main()
