# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # st.title("🔄 AI-Powered Flowchart Generator")
# st.title("📚 :rainbow[AI-Powered Flowchart Maker]")

# # User Input
# user_input = st.text_area("Enter your text to generate a flowchart:", height=200)

# def clean_mermaid_code(code):
#     """Fix MermaidJS syntax errors by removing invalid characters in decision nodes."""
#     return code.replace("{Decision?}", "{Decision}").replace("?", "")

# def generate_flowchart(text):
#     """Generates a flowchart using Gemini AI and ensures Mermaid compatibility."""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that generates flowcharts using MermaidJS syntax.
#     Generate a valid MermaidJS flowchart for the given text.

#     Output the flowchart in valid Mermaid syntax without any explanations or markdown.
#     Ensure there are:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code (remove markdown backticks if present)
#             if "```mermaid" in raw_response:
#                 start_idx = raw_response.find("```mermaid")
#                 end_idx = raw_response.rfind("```")
#                 if start_idx != -1 and end_idx != -1:
#                     mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                     return clean_mermaid_code(mermaid_code)
#             else:
#                 # If no markdown formatting, use the entire response
#                 return clean_mermaid_code(raw_response)

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# # Install streamlit-mermaid component using pip
# # pip install streamlit-mermaid

# # Import the mermaid component or use alternative for rendering
# try:
#     import streamlit_mermaid as st_mermaid
    
#     def render_mermaid_chart(mermaid_code):
#         """Renders mermaid chart using streamlit-mermaid component"""
#         st_mermaid.st_mermaid(mermaid_code, height=500)
        
# except ImportError:
#     # Fallback if streamlit-mermaid is not installed
#     def render_mermaid_chart(mermaid_code):
#         """Fallback method for rendering - display code and instructions"""
#         st.code(mermaid_code, language="mermaid")
#         st.info("For better visualization, install streamlit-mermaid: `pip install streamlit-mermaid`")

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         with st.spinner("Generating flowchart..."):
#             mermaid_code = generate_flowchart(user_input)

#             if mermaid_code:
#                 st.session_state["flowchart"] = mermaid_code
#                 st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Render the MermaidJS flowchart
#     render_mermaid_chart(st.session_state["flowchart"])

#     # Provide a download option for Mermaid code
#     st.download_button(
#         label="⬇️ Download Flowchart Code",
#         data=st.session_state["flowchart"],
#         file_name="flowchart.mmd",
#         type="primary",
#     )
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini AI SDK

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Title
st.title("📚 :rainbow[AI-Powered Flowchart Maker]")

# User Input
user_input = st.text_area("Enter your text to generate a flowchart:", height=200)

# Function to clean and fix Mermaid syntax
def clean_mermaid_code(code):
    return code.replace("{Decision?}", "{Decision}").replace("?", "").strip()

# Function to generate Mermaid code from text
def generate_flowchart(text):
    PROMPT_TEMPLATE = f"""
    You are an AI that generates flowcharts using MermaidJS syntax.
    Generate a valid MermaidJS flowchart for the given text.

    Output only the flowchart in valid Mermaid syntax without any explanations or markdown.
    Avoid using '?' inside any decision node.

    Text: {text}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(PROMPT_TEMPLATE)

        if response and hasattr(response, "text"):
            raw_response = response.text.strip()

            # Remove markdown code block if present
            if "```mermaid" in raw_response:
                start_idx = raw_response.find("```mermaid")
                end_idx = raw_response.rfind("```")
                mermaid_code = raw_response[start_idx + 10:end_idx].strip()
            else:
                mermaid_code = raw_response

            return clean_mermaid_code(mermaid_code)

        st.error("❌ API response was not in expected format.")
        return ""
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return ""

# Try importing streamlit-mermaid
try:
    import streamlit_mermaid as st_mermaid

    def render_mermaid_chart(mermaid_code):
        """Render Mermaid chart using streamlit-mermaid"""
        st_mermaid.st_mermaid(mermaid_code, height=500)

except ImportError:
    # Fallback method if streamlit-mermaid is not installed
    def render_mermaid_chart(mermaid_code):
        st.code(mermaid_code, language="mermaid")
        st.info("⚠️ Install streamlit-mermaid for visual rendering: `pip install streamlit-mermaid`")

# Generate button
if st.button("Generate Flowchart"):
    if user_input.strip():
        with st.spinner("Generating flowchart..."):
            mermaid_code = generate_flowchart(user_input)
            if mermaid_code:
                st.session_state["flowchart"] = mermaid_code
                st.success("✅ Flowchart generated successfully!")

# Display generated flowchart
if "flowchart" in st.session_state:
    st.subheader("📊 Generated Flowchart:")
    render_mermaid_chart(st.session_state["flowchart"])

    # Download button
    st.download_button(
        label="⬇️ Download Flowchart Code",
        data=st.session_state["flowchart"],
        file_name="flowchart.mmd",
        type="primary",
    )

# Debug test button
if st.button("🔍 Test Mermaid Render (Sample)"):
    test_code = """
    graph TD
        A[Start] --> B{Decision}
        B -->|Yes| C[Action 1]
        B -->|No| D[Action 2]
        C --> E[End]
        D --> E
    """
    st.subheader("🔧 Sample Flowchart Test:")
    render_mermaid_chart(test_code)

