# Agent AI to generate content about Beauty for Social Media
> This application is responsible for:
> 1. Create a form with defined parameters for the content generator, based on the business needs in order to support any type of business necessity.  
> 2. Generate the prompt using the parameters inputed in the form.
> 3. Execute the LLM (Large Language Model) to generate the customized content for the Beauty company based on the prompt informed.

![alt text](/static/images/Beauty_Content_Generator.png)

## Business Use Case:
A Beauty has many responsibilities in the Marketing area, however, the team is lean. 

Although it demands a long period of effort, one of the responsibilities is to generate daily content in different social medias.

Thus, it's important for the Marketing team to automate the generation of the content task to reduce effort from the professionals to evaluate the content generated and publish it with as much as intelligence as possible. Then, save time to focus on more strategic activities.

## Technical details:
- __Front End__: Created with Streamlit lib from Python and CSS for format.
- __Backend and LLM__: The application is created in Python, and the model used in this project is the _llama_, consumed via API from the provider Groq.

## Dependencies:
To execute the whole pipeline (dbt seed, dbt run and dbt test):
* [Docker Installation](https://www.docker.com/)
* [Groq API Key](https://console.groq.com/keys) creation and input in the __.env file__ of the repository
* Have the Docker up and running.
  * If you are using the Docker Desktop, you just need to open it. 

## Run
  1. Go to the path where you cloned the project
  2. Run: ```docker build -t beauty_content_generator .``` to create the environment
  3. Run: ```docker run -it -p 8501:8501 beauty_content_generator``` to create the environment
