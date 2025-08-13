from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as stml

def define_llm(id_model):
   llm = ChatGroq(
   model = id_model,
   temperature = 0.7,
   max_tokens = None,
   timeout = None,
   max_retries = 2
   )
   return llm

def define_prompt(topic, platform, tone, audience, length, cta, hashtags, keywords):
   theme = topic if topic else "beauty"
   prompt = f"""
   Generate an SEO-optimized article on: {theme}.
   Instructions:
   1. Output only the final article, no explanations.
   2. Platform: {platform}
   3. Tone: {tone}
   4. Audience: {audience}
   5. Length: {length}
   {(f"6. Mandatory SEO keywords: {theme}, {keywords}") if keywords else (f"6. Mandatory SEO keywords: {theme}")}
   {(f"7. Add call-to-action: {cta}") if cta else (f"7. Exclude any call-to-action.")}
   {("8. Add relevant hashtags at the end.") if hashtags else "8. Exclude hashtags."}
   Focus on:
   - Maximizing SEO performance with natural keywords integration.
   - Clear, engaging structure tailored to the platform and appropriate length of text.
   - Concise, high-quality writing aligned with the tone and audience, closing with the call-to-action.
   """
   return prompt

def generate_prompt(form_values):
   lables = ("topic", "platform", "tone", "length", "audience", "cta", "hashtags", "keywords")
   kwargs = dict(zip(lables, form_values))
   return define_prompt(**kwargs)

def llm_generate (llm, prompt):
   template = ChatPromptTemplate.from_messages([
      ("system", "You're a professional writer"),
      ("human", "{prompt}")
      ])
   chain = template | llm | StrOutputParser()
   return chain.invoke({"prompt": prompt})

def execute_sample_llm(llm):
   prompt = define_prompt("beauty", "Instagram", "fun", "women", "short", "Enjoy the promotion", True, "elegancy, autenticity")
   return llm_generate(llm, prompt)
