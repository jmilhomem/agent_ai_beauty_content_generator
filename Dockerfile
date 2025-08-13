FROM python:3.12-alpine

# install all libs for the app
RUN apk add --no-cache bash nano
RUN pip install -q langchain langchain-community langchain-groq 
RUN pip install streamlit
RUN pip install python-dotenv

# Copy the application code to the image
WORKDIR /usr/src/app
COPY . .

# Expose the ports for the streamlit
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py"]