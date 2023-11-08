import os
import pyttsx3
import speech_recognition as sr
import csv
from datetime import datetime

# Inicializa o mecanismo de síntese de voz
engine = pyttsx3.init()

# Função para registrar compromissos em um arquivo CSV
def registrar_compromisso(data, compromisso):
    with open('agenda.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data, compromisso])
    engine.say(f"Compromisso registrado para {data}: {compromisso}")
    engine.runAndWait()

# Função para listar compromissos de uma data específica
def listar_compromissos(data):
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        compromissos = [row[1] for row in reader if row[0] == data]
    if compromissos:
        engine.say(f"Compromissos para {data}: {', '.join(compromissos)}")
    else:
        engine.say(f"Não há compromissos registrados para {data}")
    engine.runAndWait()

# Função para um terceiro comando (exemplo: retornar a data e hora atual)
def terceiro_comando():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    engine.say(f"A hora atual é {current_time}")
    engine.runAndWait()

# Função principal para ouvir comandos de voz
def ouvir_comandos():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Fale um comando:")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            if "registro de compromisso" in command:
                data = input("Por favor, digite a data do compromisso (formato YYYY-MM-DD): ")
                compromisso = input("Por favor, digite o compromisso: ")
                registrar_compromisso(data, compromisso)
            elif "compromissos do dia" in command:
                data = input("Por favor, digite a data para listar os compromissos (formato YYYY-MM-DD): ")
                listar_compromissos(data)
            elif "terceiro comando" in command:
                terceiro_comando()
            else:
                engine.say("Comando não reconhecido. Por favor, tente novamente.")
                engine.runAndWait()
        except sr.UnknownValueError:
            engine.say("Não foi possível entender o comando. Por favor, tente novamente.")
            engine.runAndWait()

# Executa a função para ouvir comandos de voz
ouvir_comandos()
