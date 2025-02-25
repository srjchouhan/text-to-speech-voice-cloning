from text_extraction import extract_text_from_pdf, extract_text_from_image
from tts_voice_cloning import text_to_speech_with_cloning

def process_input(input_path, input_type, reference_audio_path, output_audio_path):
    """Process input file and generate speech with voice cloning."""
    if input_type == "pdf":
        text = extract_text_from_pdf(input_path)
    elif input_type == "image":
        text = extract_text_from_image(input_path)
    else:
        raise ValueError("Unsupported input type. Use 'pdf' or 'image'.")

    print("Extracted Text:", text)

    # Convert text to speech with voice cloning
    text_to_speech_with_cloning(text, reference_audio_path, output_audio_path)

if __name__ == "__main__":
    # Example usage
    input_path = "example.pdf"  # or "example_image.png"
    input_type = "pdf"  # or "image"
    reference_audio_path = "reference_audio.wav"
    output_audio_path = "output_speech.wav"

    process_input(input_path, input_type, reference_audio_path, output_audio_path)
