import streamlit as st
from gradio_client import Client
import numpy as np
import streamlit as st
from gradio_client import Client
import numpy as np
import anthropic
import helpers.utils as utils
import os
from dotenv import load_dotenv


def main():
    st.set_page_config(layout="wide")
    st.write("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap')
    </style>
            """, unsafe_allow_html=True)

    utils.local_css('styles.css')
    utils.remote_css(
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css")
    utils.remote_css(
        "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css")
    utils.remote_css("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap")



    menu = ["Generar imagen", "Generar poema"]
    choice = st.sidebar.selectbox("Seleccione una opción", menu)

    col1, col2 = st.columns([1, 2])

        
   
    col1.title("Local stable-diffusion🌌 🎨")
    prompt = col1.text_area("Prompt:", placeholder="Escriba aquí su prompt")

    if col1.button("Generar imagen", key="primary_button", type="primary"):
        client = Client("stabilityai/stable-diffusion-3-medium")
        result = client.predict(
                    prompt=prompt,
                    negative_prompt="The image should not contain any unicorns or rainbows.",
                    seed=0,
                    randomize_seed=True,
                    width=1024,
                    height=1024,
                    guidance_scale=5,
                    num_inference_steps=28,
                    api_name="/infer"
                )
        if result:
            with col2.container():
                col1.success("Imagen generada exitosamente!")
                st.toast("Imagen generada exitosamente!")
                col2.image(result[0], use_column_width=True, caption="Generated Image")
        else:
           st.error(
            "Error al generar la imagen. Por favor, inténtelo de nuevo.")
           
    st.markdown("""
    <head>
        <title>My Website</title>
        <!-- Add Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <div class="row">
      <div class="col-sm-6 mb-3 mb-sm-0">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="https://huggingface.co/" class="btn btn-primary">
              <img src="https://huggingface.co/front/assets/huggingface_logo.svg" alt="Hugging Face" style="width: 20px; height: 20px; margin-right: 5px;">
              Hugging Face
            </a>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">Special title treatment</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="https://github.com/" class="btn btn-primary">
              <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" style="width: 20px; height: 20px; margin-right: 5px;">
              GitHub
            </a>
          </div>
        </div>
      </div>
    </div>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
