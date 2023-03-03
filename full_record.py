import speech_recognition as speech_r
import recorder


class STT:
    # init a recognition class
    recognition = speech_r.Recognizer()

    def decode(self):
        # prepare audio file for sending
        recorder.Recorder.record_file()
        sample_audio = speech_r.AudioFile("file.wav")
        with sample_audio as audio_source:
            audio_content = self.recognition.record(audio_source)

        # send an audio file
        answer_dict = self.recognition.recognize_google(
            audio_content, language="ru-RU")
        return answer_dict

        # get an output string
        # speech_r.pprint(answer_dict, indent=4)
