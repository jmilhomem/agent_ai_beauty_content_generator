#import the package dotenv, to read the .env file w/ the api-key
import streamlit as stml
from dotenv import load_dotenv
from utils.css import apply_css
from llm.llm import define_llm, generate_prompt, execute_sample_llm
from frontend.form import create_form_page, create_lables, create_execute_button, show_content_generated 

load_dotenv()

def main():
  apply_css("static/style.css")

  id_model = "llama3-70b-8192"
  llm = define_llm(id_model)

  try:
    create_form_page()
  except Exception as e:
    stml.write(f"Error: {e}")

  #define the layout of the page with 2 columns
  left_col, right_col = stml.columns([1, 2]) 
  
  with left_col:
    form_values = create_lables()
    if form_values != None:
      prompt = generate_prompt(form_values)
      model_output = create_execute_button(llm, prompt)

  with right_col:
    show_content_generated(model_output)


if __name__ == "__main__":
  main()
else: 
  main()
