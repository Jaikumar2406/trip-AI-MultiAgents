from elevenlabs import ElevenLabs
import io
import pygame

# Initialize ElevenLabs client
client = ElevenLabs(api_key="37f672ce0724bc79c337ccf64c168c321dd425aa06d248b20bd7e67665c95b18")

def speak(text: str, voice="Rachel", return_audio=False):
    """
    Convert text to speech using ElevenLabs and play the audio.
    If return_audio=True, returns the raw MP3 bytes instead of playing sound.
    """
    if not text:
        return None

    try:
        # Generate audio using ElevenLabs v1 SDK
        audio_stream = client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB",  # Rachel voice
            model_id="eleven_turbo_v2",
            text=text,
            voice_settings={"stability": 0.5, "similarity_boost": 0.75},
            output_format="mp3_44100_128",
        )

        audio_bytes = b"".join(audio_stream)

        if return_audio:
            return audio_bytes  # <-- ✅ handles the backend request

        # 🎧 Play sound directly
        pygame.mixer.init()
        pygame.mixer.music.load(io.BytesIO(audio_bytes), "mp3")
        pygame.mixer.music.play()

    except Exception as e:
        print(f"❌ ElevenLabs speak() error: {e}")
        return None