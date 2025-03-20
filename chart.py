# import streamlit as st
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# #Load API Key
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("📌 AI-Powered Flowchart Generator")

# #User Input
# text = st.text_area("Enter a process description:", height=200)

# def generate_flowchart(description):
#     """Generates a valid MermaidJS flowchart using Gemini AI."""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that converts a process description into a valid MermaidJS flowchart.
#     Ensure the output follows correct Mermaid syntax. Example:

#     ```mermaid
#     graph TD;
#     A[Start] --> B{{Decision?}};
#     B -- Yes --> C[Process Step 1];
#     B -- No --> D[Process Step 2];
#     C --> E[End];
#     D --> E;
#     ```

#     Generate a similar flowchart for the following description:

#     {description}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             #Extract Mermaid Code
#             mermaid_start = raw_response.find("```mermaid")
#             mermaid_end = raw_response.rfind("```")
#             if mermaid_start != -1 and mermaid_end != -1:
#                 mermaid_code = raw_response[mermaid_start + 10 : mermaid_end].strip()
#                 return mermaid_code  #Only return clean Mermaid code

#         st.error("❌ API response was not in expected format.")
#         return None

#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return None

# if st.button("Generate Flowchart"):
#     if text.strip():
#         flowchart_code = generate_flowchart(text)

#         if flowchart_code:
#             st.session_state["flowchart_code"] = flowchart_code
#             st.success("✅ Flowchart generated successfully!")

# #Display Flowchart
# # if "flowchart_code" in st.session_state:
# #     st.subheader("📊 Generated Flowchart:")
# #     st.code(f"```mermaid\n{st.session_state['flowchart_code']}\n```", language="markdown")

# if "flowchart_code" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")

#     mermaid_code = f"""
#     <div class="mermaid">
#     {st.session_state['flowchart_code']}
#     </div>
#     """

#     html_code = f"""
#     <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
#     <script>
#         document.addEventListener("DOMContentLoaded", function() {{
#             if (window.mermaid) {{
#                 mermaid.initialize({{startOnLoad: true}});
#                 mermaid.init(undefined, document.querySelectorAll(".mermaid"));
#             }}
#         }});
#     </script>
#     {mermaid_code}
#     """

#     st.components.v1.html(html_code, height=500, scrolling=True)
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Streamlit App Title
# st.title("📊 AI-Powered Flowchart Generator")

# # User Input
# message = st.text_area("Enter your process description:", height=200)

# def generate_flowchart(text):
#     """Generates a flowchart using Gemini AI"""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that converts text descriptions into correct MermaidJS flowchart format.
#     Generate a flowchart in this format:
   
#     def clean_mermaid_code(code):
#         """Fix MermaidJS syntax errors by removing special characters in decision nodes."""
#     return code.replace("{Decision?}", "{Decision}")  # Remove "?" from decision nodes

#     ```mermaid
#     graph LR
#         A[Start] --> B{Decision}
#         B -- Yes --> C[Process 1]
#         B -- No --> D[Process 2]
#         C --> E[End]
#         D --> E
#     ```

#     Ensure the syntax is correct. Do NOT add extra {} brackets unless needed.

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract the Mermaid code
#             mermaid_start = raw_response.find("```mermaid")
#             mermaid_end = raw_response.rfind("```")

#             if mermaid_start != -1 and mermaid_end != -1:
#                 mermaid_code = raw_response[mermaid_start + 10 : mermaid_end].strip()
#                 return mermaid_code

#         st.error("❌ API response was not in expected format.")
#         return None

#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return None

# if st.button("Generate Flowchart"):
#     if message.strip():
#         flowchart_code = generate_flowchart(message)

#         if flowchart_code:
#             st.session_state["flowchart_code"] = flowchart_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart_code" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")

#     mermaid_code = f"""
#     <div class="mermaid">
#     {st.session_state['flowchart_code']}
#     </div>
#     """

#     html_code = f"""
#     <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
#     <script>
#         document.addEventListener("DOMContentLoaded", function() {{
#             if (window.mermaid) {{
#                 mermaid.initialize({{startOnLoad: true}});
#                 mermaid.init(undefined, document.querySelectorAll(".mermaid"));
#             }}
#         }});
#     </script>
#     {mermaid_code}
#     """

#     st.components.v1.html(html_code, height=500, scrolling=True)
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("🔄 AI-Powered Flowchart Generator")

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

#     Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code
#             start_idx = raw_response.find("```mermaid")
#             end_idx = raw_response.rfind("```")

#             if start_idx != -1 and end_idx != -1:
#                 mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                 return clean_mermaid_code(mermaid_code)  # Fix syntax errors

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         mermaid_code = generate_flowchart(user_input)

#         if mermaid_code:
#             st.session_state["flowchart"] = mermaid_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Display the Mermaid code inside Streamlit
#     st.code(f"```mermaid\n{st.session_state['flowchart']}\n```", language="mermaid")

#     # Provide a download option
#     st.download_button(
#         label="⬇️ Download Flowchart Code",
#         data=st.session_state["flowchart"],
#         file_name="flowchart.mmd",
#         type="primary",
#     )
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("🔄 AI-Powered Flowchart Generator")

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

#     Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code
#             start_idx = raw_response.find("```mermaid")
#             end_idx = raw_response.rfind("```")

#             if start_idx != -1 and end_idx != -1:
#                 mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                 return clean_mermaid_code(mermaid_code)  # Fix syntax errors

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# def render_mermaid_chart(mermaid_code):
#     """Embeds the MermaidJS code inside an HTML component in Streamlit."""
#     mermaid_html = f"""
#     <script type="module">
#         import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
#         mermaid.initialize({{ startOnLoad: true }});
#     </script>
#     <div class="mermaid">
#         {mermaid_code}
#     </div>
#     """
#     st.components.v1.html(mermaid_html, height=500, scrolling=True)

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         mermaid_code = generate_flowchart(user_input)

#         if mermaid_code:
#             st.session_state["flowchart"] = mermaid_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Render the MermaidJS flowchart inside Streamlit
#     render_mermaid_chart(st.session_state["flowchart"])

#     # Provide a download option for Mermaid code
#     st.download_button(
#         label="⬇️ Download Flowchart Code",
#         data=st.session_state["flowchart"],
#         file_name="flowchart.mmd",
#         type="primary",
    # )
# import streamlit as st
# import os
# import json
# import base64
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK
# import requests  # To send MermaidJS to an API for image generation

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("🔄 AI-Powered Flowchart Generator")

# # User Input
# user_input = st.text_area("Enter your text to generate a flowchart:", height=200)

# def clean_mermaid_code(code):
#     """Fix MermaidJS syntax errors and improve contrast for visibility."""
#     cleaned_code = code.replace("{Decision?}", "{Decision}").replace("?", "")
    
#     # Apply colors to improve contrast
#     style_block = """
#     classDef green fill:#2ECC71,stroke:#27AE60,stroke-width:2px;
#     classDef blue fill:#3498DB,stroke:#2980B9,stroke-width:2px;
#     classDef red fill:#E74C3C,stroke:#C0392B,stroke-width:2px;
#     classDef yellow fill:#F1C40F,stroke:#F39C12,stroke-width:2px;
#     classDef grey fill:#95A5A6,stroke:#7F8C8D,stroke-width:2px;
    
#     linkStyle default stroke:#000,stroke-width:2px,color:#000;
#     """
    
#     return cleaned_code + "\n\n" + style_block  # Append styles at the end

# def generate_flowchart(text):
#     """Generates a flowchart using Gemini AI and ensures Mermaid compatibility."""
#     PROMPT_TEMPLATE = f"""
#     You are an AI that generates flowcharts using MermaidJS syntax.
#     Generate a valid MermaidJS flowchart for the given text.

#     Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code
#             start_idx = raw_response.find("```mermaid")
#             end_idx = raw_response.rfind("```")

#             if start_idx != -1 and end_idx != -1:
#                 mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                 return clean_mermaid_code(mermaid_code)  # Fix syntax errors

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# def render_mermaid_chart(mermaid_code):
#     """Embeds the MermaidJS code inside an HTML component in Streamlit."""
#     mermaid_html = f"""
#     <script type="module">
#         import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
#         mermaid.initialize({{ startOnLoad: true }});
#     </script>
#     <div class="mermaid">
#         {mermaid_code}
#     </div>
#     """
#     st.components.v1.html(mermaid_html, height=500, scrolling=True)

# def generate_flowchart_image(mermaid_code):
#     """Send MermaidJS to an API (Kroki) to generate an image."""
#     kroki_url = "https://kroki.io/mermaid/png"  # MermaidJS to PNG API

#     try:
#         response = requests.post(kroki_url, json={"diagram_source": mermaid_code})
#         if response.status_code == 200:
#             return response.content  # Return the image data
#     except Exception as e:
#         st.error(f"❌ Error converting Mermaid to image: {str(e)}")
#         return None

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         mermaid_code = generate_flowchart(user_input)

#         if mermaid_code:
#             st.session_state["flowchart"] = mermaid_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Render the MermaidJS flowchart inside Streamlit
#     render_mermaid_chart(st.session_state["flowchart"])

#     # Convert and display as image
#     image_data = generate_flowchart_image(st.session_state["flowchart"])
#     if image_data:
#         st.image(image_data, caption="Flowchart", use_column_width=True)

#         # Enable image download as PNG
#         b64 = base64.b64encode(image_data).decode()
#         href = f'<a href="data:image/png;base64,{b64}" download="flowchart.png">⬇️ Download Flowchart as PNG</a>'
#         st.markdown(href, unsafe_allow_html=True)
# import streamlit as st
# import os
# import json
# from dotenv import load_dotenv
# import google.generativeai as genai  # Gemini AI SDK

# # Load environment variables
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("🔄 AI-Powered Flowchart Generator")

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

#     Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code
#             start_idx = raw_response.find("```mermaid")
#             end_idx = raw_response.rfind("```")

#             if start_idx != -1 and end_idx != -1:
#                 mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                 return clean_mermaid_code(mermaid_code)  # Fix syntax errors

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# def render_mermaid_chart(mermaid_code):
#     """Embeds the MermaidJS code inside an HTML component in Streamlit."""
#     mermaid_html = f"""
#     <script type="module">
#         import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
#         mermaid.initialize({{ startOnLoad: true }});
#     </script>
#     <div class="mermaid">
#         {mermaid_code}
#     </div>
#     """
#     st.components.v1.html(mermaid_html, height=500, scrolling=True)

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         mermaid_code = generate_flowchart(user_input)

#         if mermaid_code:
#             st.session_state["flowchart"] = mermaid_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Render the MermaidJS flowchart inside Streamlit
#     render_mermaid_chart(st.session_state["flowchart"])

#     # Provide a download option for Mermaid code
#     st.download_button(
#         label="⬇️ Download Flowchart Code",
#         data=st.session_state["flowchart"],
#         file_name="flowchart.mmd",
#         type="primary",
#     )
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
#     Generate a valid MermaidJS flowchart for the given text.give output in json format

#     Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
#     - No syntax errors
#     - No special characters inside decision nodes (e.g., '?' is not allowed)

#     Text: {text}
#     """

#     try:
#         model = genai.GenerativeModel("gemini-1.5-pro")
#         response = model.generate_content(PROMPT_TEMPLATE)

#         if response and hasattr(response, "text"):
#             raw_response = response.text.strip()

#             # Extract only the Mermaid code
#             start_idx = raw_response.find("```mermaid")
#             end_idx = raw_response.rfind("```")

#             if start_idx != -1 and end_idx != -1:
#                 mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
#                 return clean_mermaid_code(mermaid_code)  # Fix syntax errors

#         st.error("❌ API response was not in expected format.")
#         return ""
    
#     except Exception as e:
#         st.error(f"❌ Error: {str(e)}")
#         return ""

# def render_mermaid_chart(mermaid_code):
#     """Embeds the MermaidJS code inside an HTML component in Streamlit."""
#     mermaid_html = f"""
#     <script type="module">
#         import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
#         mermaid.initialize({{ startOnLoad: true }});
#     </script>
#     <div class="mermaid">
#         {mermaid_code}
#     </div>
#     """
#     st.components.v1.html(mermaid_html, height=500, scrolling=True)

# if st.button("Generate Flowchart"):
#     if user_input.strip():
#         mermaid_code = generate_flowchart(user_input)

#         if mermaid_code:
#             st.session_state["flowchart"] = mermaid_code
#             st.success("✅ Flowchart generated successfully!")

# if "flowchart" in st.session_state:
#     st.subheader("📊 Generated Flowchart:")
    
#     # Render the MermaidJS flowchart inside Streamlit
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
import json
from dotenv import load_dotenv
import google.generativeai as genai  # Gemini AI SDK

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# st.title("🔄 AI-Powered Flowchart Generator")
st.title("📚 :rainbow[AI-Powered Flowchart Maker]")

# User Input
user_input = st.text_area("Enter your text to generate a flowchart:", height=200)

def clean_mermaid_code(code):
    """Fix MermaidJS syntax errors by removing invalid characters in decision nodes."""
    return code.replace("{Decision?}", "{Decision}").replace("?", "")

def generate_flowchart(text):
    """Generates a flowchart using Gemini AI and ensures Mermaid compatibility."""
    PROMPT_TEMPLATE = f"""
    You are an AI that generates flowcharts using MermaidJS syntax.
    Generate a valid MermaidJS flowchart for the given text.give output in json format

    Output the flowchart **inside triple backticks** (```mermaid ... ```), ensuring:
    - No syntax errors
    - No special characters inside decision nodes (e.g., '?' is not allowed)

    Text: {text}
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(PROMPT_TEMPLATE)

        if response and hasattr(response, "text"):
            raw_response = response.text.strip()

            # Extract only the Mermaid code
            start_idx = raw_response.find("```mermaid")
            end_idx = raw_response.rfind("```")

            if start_idx != -1 and end_idx != -1:
                mermaid_code = raw_response[start_idx + 10 : end_idx].strip()
                return clean_mermaid_code(mermaid_code)  # Fix syntax errors

        st.error("❌ API response was not in expected format.")
        return ""
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        return ""

def render_mermaid_chart(mermaid_code):
    """Embeds the MermaidJS code inside an HTML component in Streamlit."""
    mermaid_html = f"""
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true }});
    </script>
    <div class="mermaid">
        {mermaid_code}
    </div>
    """
    st.components.v1.html(mermaid_html, height=500, scrolling=True)

if st.button("Generate Flowchart"):
    if user_input.strip():
        mermaid_code = generate_flowchart(user_input)

        if mermaid_code:
            st.session_state["flowchart"] = mermaid_code
            st.success("✅ Flowchart generated successfully!")

if "flowchart" in st.session_state:
    st.subheader("📊 Generated Flowchart:")
    
    # Render the MermaidJS flowchart inside Streamlit
    render_mermaid_chart(st.session_state["flowchart"])

    # Provide a download option for Mermaid code
    st.download_button(
        label="⬇️ Download Flowchart Code",
        data=st.session_state["flowchart"],
        file_name="flowchart.mmd",
        type="primary",
    )
