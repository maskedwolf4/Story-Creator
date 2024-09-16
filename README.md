# Story-Generation-Uisng-Image

## **README: Story Generating Using Image Using Llava-v1.5-7b and Llama3.10-70b**

**Project Overview**

This repository contains the code for a Streamlit-based application that generates detailed stories for children based on user-provided images. The application leverages the Llava-v1.5-7b LLM to generate detailed descriptions of the image, which are then used as input to the Llama3.10-70b to create a captivating story.

**Key Features**

* **Image-Based Story Generation:** Users can upload an image, and the application will generate a story inspired by its content.
* **Llava and Llama LLM:** The powerful LLMs is used for describing image and generating story from it.
* **User-Friendly Interface:** The Streamlit interface offers a simple and intuitive way for users to interact with the application.

**Prerequisites**

Before running the application, ensure you have the following installed:

* Python (version 3.10 or later)
* Streamlit
* Groq API Key

**Requirements**

The required libraries are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

**Groq API Key**

To access the Groq API, you'll need an API key. Obtain one from the Groq developer portal and create a `.env` file in the project root directory with the following content:

```
GROQ_API_KEY=your_api_key
```

**Running the Application**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/maskedwolf4/Story-Creator.git
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set API Key:**
   Create the `.env` file with your Groq API key as described above.
4. **Run the Application:**
   ```bash
   streamlit run sgiapp.py
   ```

**Usage**

* **Upload Image:** Use the provided interface to upload an image.
* **Generate Story:** The application will process the image, generate a description, and create a story based on the description.

**Contributing**

We welcome contributions to this project! If you have any improvements or bug fixes, please feel free to submit a pull request.

**License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
