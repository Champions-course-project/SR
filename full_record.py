import speech_recognition as speech_r
import recorder
import os
import wave


class STT:
    # init a recognition class
    __recognition = speech_r.Recognizer()

    @staticmethod
    def decode():
        """
        Record data and decode it.
        """
        try:
            recorder.Recorder.record_file()
            return STT.decode_file("file.wav")
        finally:
            os.remove("file.wav")

    @staticmethod
    def decode_bytestream(bytestream: bytes, framerate: int):
        """
        Decode a bytestream using known framerate.\n
        bytestream - simply raw data as a bytes class\n
        framerate - also known as frequency (in Hz)\n
        Returns dictionary, containing words and final result.
        """
        try:
            wb = wave.open("file.wav", "wb")
            wb.setnchannels(1)
            wb.setsampwidth(2)
            wb.setframerate(framerate)
            wb.writeframes(bytestream)
            wb.close()
            return STT.decode_file("file.wav")
        finally:
            os.remove("file.wav")

    @staticmethod
    def decode_file(filename: str):
        """
        Decode data written in .wav file.\n
        filename - name of .wav file (with extencion)\n
        Returns dictionary, containing words and final result.
        """
        # prepare audio file for sending
        sample_audio = speech_r.AudioFile(filename)
        with sample_audio as audio_source:
            audio_content = STT.__recognition.record(audio_source)
        # send an audio file
        answer_dict = STT.__recognition.recognize_google(
            audio_content, language="ru-RU")
        return answer_dict
