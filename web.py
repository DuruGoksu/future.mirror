from flask import Flask, render_template, request
import os
import base64
from dotenv import load_dotenv

from text_enhancer import enhance_text
from image_generator import generate_image
# from speech_recognizer import recognize_speech  # Gelecekte kullanılmak üzere yorum satırında

# Ortam değişkenlerini yükle
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    input_text = ""
    improved_text = ""
    encoded_image = ""

    if request.method == 'POST':
        input_text = request.form.get('text', '')

        # Metni iyileştir
        improved_text = enhance_text(input_text)

        # Görsel oluştur ve base64'e çevir
        image_file_path = generate_image(improved_text)

        with open(image_file_path, "rb") as img_file:
            encoded_image = base64.b64encode(img_file.read()).decode("utf-8")

    return render_template(
        'index.html',
        original_text=input_text,
        enhanced_text=improved_text,
        image_data=encoded_image
    )

if __name__ == '__main__':
    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    app.run(debug=True, port=5001)
