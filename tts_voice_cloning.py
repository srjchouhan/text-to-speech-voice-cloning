from TTS.api import TTS

def text_to_speech_with_cloning(text, reference_audio_path, output_audio_path):
    """Convert text to speech with voice cloning."""
    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", gpu=False)
    tts.tts_to_file(
        text=text,
        speaker_wav=reference_audio_path,
        file_path=output_audio_path
    )
    print(f"Speech saved to {output_audio_path}")
