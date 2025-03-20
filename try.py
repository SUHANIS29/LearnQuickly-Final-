# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK
# import streamlit.components.v1 as components  # Required for proper HTML rendering

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("📚 :rainbow[AI-Powered Flashcard Maker]")

# # User Input
# message = st.text_area("Enter your text to generate flashcards:", height=200)

# def generate_flashcards(text):
#     """Generates flashcards using Gemini AI"""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that extracts key concepts and creates concise flashcards.
#     Generate flashcards after assessing the given content. 
#     make sure the questions are short and clear.
#     answers can be 2-3 liner and covers key term-defination pair or statements cover fill in the blanks or true-false or give reason.
#     for defintion question the question should be define -term and anser should be definition
#     generate in in JSON format:
#     {{"flashcards": [
#         {{"question":'...", "answer": "..."}} ,
        
#     ]}}

    
#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         # Ensure response is valid
#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract JSON portion only
#             json_start = raw_response.find("{")
#             json_end = raw_response.rfind("}")
#             if json_start != -1 and json_end != -1:
#                 json_data = raw_response[json_start : json_end + 1]
#                 parsed_response = json.loads(json_data)  # Parse JSON

#                 return parsed_response.get("flashcards", [])

#         st.error("❌ API response was not in expected format.")
#         return []
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return []

# if st.button("Generate Flashcards"):
#     if message.strip():
#         flashcards = generate_flashcards(message)
        
#         if flashcards:
#             st.session_state["flashcards"] = flashcards  # Store flashcards in session
#             st.success("✅ Flashcards generated successfully!")

# if "flashcards" in st.session_state:
#     st.subheader("🃏 Your AI-Generated Flashcards:")

#     # Inject custom CSS & JS for improved layout and scrolling
#     flashcard_html = """
#     <style>
#         /* Custom scrollbar */
#         ::-webkit-scrollbar {
#             width: 10px;
#         }
#         ::-webkit-scrollbar-track {
#             background: #f1f1f1;
#             border-radius: 10px;
#         }
#         ::-webkit-scrollbar-thumb {
#             background: #888;
#             border-radius: 10px;
#         }
#         ::-webkit-scrollbar-thumb:hover {
#             background: #555;
#         }

#         /* Flashcard container */
#         .flashcard-container {
#             display: flex;
#             flex-wrap: wrap;
#             justify-content: center;
#             gap: 70px;  /* Increased spacing */
#             padding: 20px;
#             overflow-y: auto;
#             max-height: 500px; /* Prevents excessive scrolling */
#         }

#         /* Flashcard styling */
#         .flashcard {
#             width: 420px; /* Slightly wider */
#             height: 220px; /* Slightly taller */
#             perspective: 1000px;
#         }

#         /* Inner card */
#         .flashcard-inner {
#             width: 100%;
#             height: 100%;
#             text-align: center;
#             position: relative;
#             transition: transform 0.6s;
#             transform-style: preserve-3d;
#         }

#         /* Flip effect */
#         .flashcard:active .flashcard-inner {
#             transform: rotateY(360deg);
#         }

#         /* Front and back design */
#         .flashcard-front, .flashcard-back {
#             position: absolute;
#             width: 100%;
#             height: 100%;
#             backface-visibility: hidden;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             border-radius: 15px;
#             font-size: 20px; /* Slightly larger text */
#             font-weight: bold;
#             padding: 20px;
#             box-shadow: 0 4px 8px rgba(0,0,0,0.2);
#         }

#         /* Front side */
#         .flashcard-front {
#             # background-color: rgba(255, 255, 255, 0.4); /* Slightly more opaque */
#             # background-color:#70C6FF;
#             # background: rgb(242,226,69);
#             # background: linear-gradient(90deg, rgba(242,226,69,1) 0%, rgba(255,173,47,1) 48%, rgba(191,46,9,1) 100%);
#             background: rgb(200,42,156);
#             background: linear-gradient(90deg, rgba(200,42,156,1) 0%, rgba(252,238,99,1) 50%, rgba(219,111,228,1) 100%);
#             color: black;
#             border: 2px solid #ddd;
#         }

#         /* Back side */
#         .flashcard-back {
#             #background-color: rgba(50, 50, 50, 0.7); /* Darker for contrast */
#             #background-color:#0093F5 ;            
#             # background: rgb(176,7,197);
#             # background: linear-gradient(90deg, rgba(176,7,197,1) 0%, rgba(255,225,98,1) 51%, rgba(196,64,7,1) 100%);
#             background: rgb(200,42,156);
#             background: linear-gradient(225deg, rgba(200,42,156,1) 0%, rgba(252,238,99,1) 50%, rgba(219,111,228,1) 100%);
#             color:black;
#             transform: rotateY(180deg);
#             border: 2px solid #555;
#         }
#     </style>

#     <div class="flashcard-container">
#     """

#     for flashcard in st.session_state["flashcards"]:
#         flashcard_html += f"""
#         <div class="flashcard">
#             <div class="flashcard-inner">
#                 <div class="flashcard-front">
#                     {flashcard['question']}
#                 </div>
#                 <div class="flashcard-back">
#                     {flashcard['answer']}
#                 </div>
#             </div>
#         </div>
#         """

#     flashcard_html += "</div>"

#     # Render flashcards properly
#     components.html(flashcard_html, height=600, scrolling=True)

#     # Download flashcards as text file
#     flashcards_text = "\n\n".join(
#         f"Q : {fc['question']}\nA : {fc['answer']}" for fc in st.session_state["flashcards"]
#     )

#     st.download_button(
#         label="⬇️ Download Flashcards",
#         data=flashcards_text,
#         file_name="flashcards.txt",
#         type="primary",
#     )
import streamlit as st
import os
import json
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini AI SDK
import streamlit.components.v1 as components  # Required for proper HTML rendering

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.title("📚 :rainbow[AI-Powered Flashcard Maker]")

# User Input
message = st.text_area("Enter your text to generate flashcards:", height=200)

def generate_flashcards(text):
    """Generates flashcards using Gemini AI"""
    PROMPT_TEMPLATE = f"""
    You are an AI that extracts key concepts and creates concise flashcards.
    Generate flashcards after assessing the given content. 
    Make sure the questions are short and clear.
    Answers can be 2-3 liners and cover key term-definition pairs, fill-in-the-blanks, true/false, or 'give reason' type questions.
    For definition questions, the question should be "Define -term", and the answer should be the definition.
    Generate the output in JSON format:
    {{"flashcards": [
        {{"question": "...", "answer": "..."}}
    ]}}
    
    Text: {text}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(PROMPT_TEMPLATE)

        # Ensure response is valid
        if response and hasattr(response, "text"):
            raw_response = response.text.strip()

            # Extract JSON portion only
            json_start = raw_response.find("{")
            json_end = raw_response.rfind("}")
            if json_start != -1 and json_end != -1:
                json_data = raw_response[json_start : json_end + 1]
                parsed_response = json.loads(json_data)  # Parse JSON

                return parsed_response.get("flashcards", [])

        st.error("❌ API response was not in expected format.")
        return []
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return []

if st.button("Generate Flashcards"):
    if message.strip():
        flashcards = generate_flashcards(message)
        
        if flashcards:
            st.session_state["flashcards"] = flashcards  # Store flashcards in session
            st.success("✅ Flashcards generated successfully!")

if "flashcards" in st.session_state:
    st.subheader("🃏 Your AI-Generated Flashcards:")

    # Inject custom CSS & JS for flipping effect
    flashcard_html = """
    <style>
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        /* Flashcard container */
        .flashcard-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 90px;
            padding: 20px;
            overflow-y: auto;
            max-height: 500px;
        }

        /* Flashcard styling */
        .flashcard {
            width: 420px;
            height: 220px;
            perspective: 1000px;
            cursor: pointer;
        }

        /* Inner card */
        .flashcard-inner {
            width: 100%;
            height: 100%;
            text-align: center;
            position: relative;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }

        /* Flip effect */
        .flashcard.flipped .flashcard-inner {
            transform: rotateY(180deg);
        }

        /* Front and back design */
        .flashcard-front, .flashcard-back {
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px;
            font-size: 20px;
            font-weight: bold;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        /* Front side */
        .flashcard-front {
            background: linear-gradient(90deg, rgba(200,42,156,1) 0%, rgba(252,238,99,1) 50%, rgba(219,111,228,1) 100%);
            color: black;
            border: 2px solid #ddd;
        }

        /* Back side */
        .flashcard-back {
            background: linear-gradient(225deg, rgba(200,42,156,1) 0%, rgba(252,238,99,1) 50%, rgba(219,111,228,1) 100%);
            color: black;
            transform: rotateY(180deg);
            border: 2px solid #555;
        }
    </style>

    <div class="flashcard-container">
    """

    for flashcard in st.session_state["flashcards"]:
        flashcard_html += f"""
        <div class="flashcard">
            <div class="flashcard-inner">
                <div class="flashcard-front">
                    {flashcard['question']}
                </div>
                <div class="flashcard-back">
                    {flashcard['answer']}
                </div>
            </div>
        </div>
        """

    flashcard_html += """
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            document.querySelectorAll(".flashcard").forEach(card => {
                card.addEventListener("click", () => {
                    card.classList.toggle("flipped");
                });
            });
        });
    </script>
    """

    # Render flashcards properly
    components.html(flashcard_html, height=600, scrolling=True)

    # Download flashcards as a text file
    flashcards_text = "\n\n".join(
        f"Q: {fc['question']}\nA: {fc['answer']}" for fc in st.session_state["flashcards"]
    )

    st.download_button(
        label="⬇️ Download Flashcards",
        data=flashcards_text,
        file_name="flashcards.txt",
        type="primary",
    )
