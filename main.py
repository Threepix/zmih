import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Вынь хуй изо рта'


def greetings():
    return "привет нищеброд"

def create_task():
    print("что добавим в список дел?")

    query = listen_command()

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    with open("todo-list.txt",'a') as file:
        file.write(f'{query}\n')

    return f'Задача {query} добавилась '


def main():
    query = listen_command()

    if query == 'привет друг':
        print(greetings())
    elif query == 'добавить задачу':
        print(create_task())
    else:
        print("прожуй потом пизди")

if __name__ == '__main__':
    main()