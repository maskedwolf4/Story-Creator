from  groq import Groq
import streamlit as st
import os
import base64

from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv["GROQ_API_KEY"]

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
st.title('Turns Pictures to Story')
st.title("Upload the image  you want  to turn into story")

client = Groq(api_key=groq_api_key)
llava_model = 'llava-v1.5-7b-4096-preview'
llama31_model = 'llama-3.1-70b-versatile'

# Define image to text function
def image_to_text(client, model, base64_image, prompt):
    chat_completion = client.chat.completions.create(
         messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                         },
                    },
                ],
            }
        ],
        model=model
    )

    return chat_completion.choices[0].message.content

# Define short story generation function
def short_story_generation(client, image_description):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a author of various books and an expert in making story from images . Write a short story about the scene depicted in this image or images from every minute points.",
            },
            {
                "role": "user",
                "content": image_description,
            }
        ],
        model=llama31_model
    )
        
    return chat_completion.choices[0].message.content



def main():
    st.set_page_config("Story Generation from Image")
    st.header("Generate Your Story using Image")

    with st.sidebar:
       st.title("Upload Image")
       uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
       if st.button("Generate Story"):
        # Getting the base64 string
        base64_image = encode_image(uploaded_image)

        prompt = "Describe this image"
        image_to_text(client,llava_model, base64_image, prompt)

        prompt = '''
        Describe this image in detail.
        '''
        image_description = image_to_text(client, llava_model, base64_image, prompt)

        print(short_story_generation(client,image_description))


if __name__ == "__main__":
    main()

