import speech_recognition as sr
from gtts import gTTS
import playsound
import openai
import pygame

# Configure suas chaves de API
openai.api_key = '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'
# Configurar chaves para serviços de STT e TTS

def transcrever_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga alguma coisa:")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
        return ""
    except sr.RequestError as e:
        print("Erro na requisição ao Google Speech Recognition; {0}".format(e))
        return ""

def texto_para_fala(texto):
    tts = gTTS(text=texto, lang='pt-BR')
    tts.save("resposta.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("resposta.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def interagir_com_chatgpt(entrada):
    # Fazer chamada para a API do ChatGPT com a entrada
    resposta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=entrada,
        max_tokens=150
    )
    return resposta.choices[0].text.strip()

while True:
    entrada_usuario = transcrever_audio()

    if entrada_usuario:
        resposta_chatgpt = interagir_com_chatgpt(entrada_usuario)
        texto_para_fala(resposta_chatgpt)
