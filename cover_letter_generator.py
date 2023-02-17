import streamlit as st
import openai
import pdfkit
import os
import pypandoc

# Initialize OpenAI API key
import streamlit as st

# Everything is accessible via the st.secrets dict:
st.write("openai_api_key:", st.secrets["openai_api_key"])

# And the root-level secrets are also accessible as environment variables:
st.write(
    "Has environment variables been set:",
    os.environ["openai_api_key"] == st.secrets["openai_api_key"],
)


def generate_cover_letter(inputs):
    # Use the inputs dictionary to generate a prompt for the language model
    prompt = (f"Write for me a 4 parapgraph interesting, convincing, exciting, and excellent "
             f"cover letter applying for a job position as a {inputs['position']} at {inputs['company']}."
             f"My level of education is {inputs['education']}, and my qualifications are {inputs['qualifications']}."
             f"I have graduated the year {inputs['graduation_year']}. My name is {inputs['name']}."
             f"Use a formal and persuasive tone with vocabulary and grammar.")
    
    # Use the OpenAI API to generate the application letter
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text
    
    return response

def main():
    st.title("Cover Letter Generator")
    
    # Ask the user for the necessary inputs
    name = st.text_input('What is your name?')
    position = st.text_input("What is the job position you are applying for?")
    company = st.text_input("What company are you applying to?")
    education  = st.text_input("What is your level of education?")
    graduation_year = st.text_input("What year did you graduate?")
    qualifications = st.text_input("What qualifications do you have that fit the position you are applying for?")
    
    # Use the inputs to generate the application letter
    inputs = {
        "name": name,
        "position": position,
        "company": company,
        "qualifications": qualifications,
        "education": education,
        "graduation_year": graduation_year,
    }
    response = generate_cover_letter(inputs)
    
    # Submit the details
    if st.button("Submit"):

        # Show the generated letter to the user
        st.write("Here is your cover letter:")
        st.write(response)


if __name__ == "__main__":
    main()
