from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def define_llm(id_model):
   llm = ChatGroq(
   model = id_model,
   temperature = 0.7,
   max_tokens = 5,
   timeout = None,
   max_retries = 2
   )
   return llm

def define_prompt(topic, platform, tone, audience, length, cta, hashtags, keywords):
   prompt = f"""
   Generate an SEO-optimized article on: {topic}.
   Instructions:
   1. Output only the final article, no explanations.
   2. Platform: {platform}
   3. Tone: {tone}
   4. Audience: {audience}
   5. Length: {length}
   6. {"CTA: ", cta if cta else "Exclude any call-to-action."}
   7. {"Add relevant hashtags at the end." if hashtags else "Exclude hashtags."}
   {("8. Mandatory SEO keywords: " + keywords) if keywords else ""}
   Focus on:
   - Maximizing SEO performance with natural keyword integration.
   - Clear, engaging structure tailored to the platform.
   - Concise, high-quality writing aligned with the tone and audience.
   """
   return prompt

def generate_prompt(form_values):
   lables = ("topic", "platform", "tone", "length", "audience", "cta", "hashtags", "keywords")
   kwargs = dict(zip(lables, form_values))
   return define_prompt(**kwargs)

def llm_generate (llm, prompt):
   template = ChatPromptTemplate.from_messages([
      ("system", "Você é um redator profissional"),
      ("human", "{prompt}")
      ])
   chain = template | llm | StrOutputParser()
   return chain.invoke({"prompt": prompt})

def execute_sample_llm(llm):
   prompt = define_prompt("beauty", "Instagram", "fun", "women", "short", "Enjoy the promotion", True, "elegancy, autenticity")
   return llm_generate(llm, prompt)
