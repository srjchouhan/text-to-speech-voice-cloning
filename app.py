from flask import Flask, request, render_template, send_file
import os
from text_extraction import extract_text_from_pdf, extract_text_from_image
from tts_voice_cloning import text_to_speech_with_cloning

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get uploaded files
        input_file = request.files["input_file"]
        reference_audio = request.files["reference_audio"]

        # Save files temporarily
        input_path = "temp_input." + input_file.filename.split(".")[-1]
        reference_audio_path = "temp_reference.wav"
        output_audio_path = "output_speech.wav"

        input_file.save(input_path)
        reference_audio.save(reference_audio_path)

        # Determine input type
        input_type = "pdf" if input_path.endswith(".pdf") else "image"

        # Process input
        if input_type == "pdf":
            text = extract_text_from_pdf(input_path)
        else:
            text = extract_text_from_image(input_path)

        # Generate speech
        text_to_speech_with_cloning(text, reference_audio_path, output_audio_path)

        # Clean up temporary files
        os.remove(input_path)
        os.remove(reference_audio_path)

        # Return the generated audio file
        return send_file(output_audio_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
