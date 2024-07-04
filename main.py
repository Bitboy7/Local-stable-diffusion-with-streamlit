import streamlit as st
from gradio_client import Client
import numpy as np
import helpers.utils as utils

def main():
    st.write("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap')
    </style>
            """,unsafe_allow_html=True)

    utils.local_css('styles.css')
    utils.remote_css("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css")
    utils.remote_css("https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css")
    utils.remote_css("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap")

    MAX_SEED = np.iinfo(np.int32).max
    MAX_IMAGE_SIZE = 1344
    st.title("Local stable-diffusion🌌 🎨")
    prompt = st.text_input("Prompt:", placeholder="Escriba aquí su prompt")
    
    if st.button("Generar imagen", key="primary_button", type="primary"):
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

        with st.container():
            st.image(result[0], caption="Generated Image")


if __name__ == "__main__":
    main()

