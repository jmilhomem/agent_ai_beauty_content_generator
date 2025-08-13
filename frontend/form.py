import streamlit as stml
from llm.llm import llm_generate

def create_page():
   stml.set_page_config(
      page_title = "Content Generator about Beauty", 
      page_icon = "🦋",
      layout = "wide"
      )

def create_title():
   stml.markdown(
      """
      <div class = "header-container">
         <h1>🦋 Beauty Content Generator </h1>
      </div>
      """,
      unsafe_allow_html = True
      )
   
def create_result_title():
   stml.markdown(
      """
      <div class = "header-container">
         <h5>Content Generated</h5>
      </div>
      """,
      unsafe_allow_html = True
      )

def create_lables():
   stml.markdown('<div class="form-container">', unsafe_allow_html=True)
   topic = stml.text_input("Topic: ", placeholder = "e.g. beauty, makeup, skin care, health, etc")
   platform = stml.selectbox("Platform: ", ["Instagram", "Facebook", "Blog", "E-mail"]) 
   tone = stml.selectbox("Message Tone: ", ["Informative", "Fun", "Urgent", "Inspirational"])
   length = stml.selectbox("Text Length: ", ["Short", "Medium", "Long"])
   audience = stml.selectbox("Target Audience: ", ["Young Adults", "Women", "Men", "Teenagers", "General"])
   cta = stml.text_area("CTA: ", placeholder = "e.g. enjoy the promotion ..., come to the event ..., etc")
   keywords = stml.text_area("Key Words", placeholder = "e.g. beauty, makeup, skin care, health, etc")
   hashtags = stml.checkbox("Return hashtags")
   stml.markdown('</div>', unsafe_allow_html=True)
   return (topic, platform, tone, length, audience, cta, hashtags, keywords)

def create_form_page():
   create_page()
   create_title()

def create_execute_button(llm, prompt):
   if (stml.button("Generate the content")):
      return llm_generate(llm, prompt)

def show_content_generated(model_output):
   create_result_title()
   if "result" not in stml.session_state:
      stml.session_state.result = ""
      stml.info("Please, fill the form and click on the generation button.")
   else:
      stml.session_state.result = model_output
      stml.write(stml.session_state.result)
