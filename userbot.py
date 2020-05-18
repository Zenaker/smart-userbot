from pyrogram import Client
from threading import Timer
from configparser import ConfigParser
from difflib import SequenceMatcher
from db_parser import *
import random

# initialize config
config = ConfigParser()

# read config
config.read("config.ini")

app = Client(config.get("userbot", "session_name"))

mio_id = config.getint("userbot", "my_id")
mario_id = config.getint("userbot", "person_id_to_learn_from")

# changes to True when /enablechat is called
chat_mode = False

# userbot commands
commands = ["/ping", "/enablechat", "/leave", "/status", "/learn"]

def dice():
    n = [1,2,3]
    r = 1
    if random.choice(n) == r:
        return True
        
    return False

    
def send_action_message(client, message, msg, message_id):
    try:
        client.send_message(message['chat']['id'], msg, reply_to_message_id=message_id)
    except:
        pass
    client.send_chat_action(message['chat']['id'], "cancel")

@app.on_message()
def learn(client, message):
    global chat_mode
    if message['from_user']['id']  == mio_id:
        if message['text'].startswith("/learn"):
            link = message['text'].split(" ")[1]
            group_info = client.join_chat(link)
            
            # read history and get data from Mario GH best supporter
            limito = message['message_id'] - 1
            client.send_message(mio_id, "sto imparando..")
            counter = 0
            
            for messaggio in client.iter_history(group_info['id']):
                counter += 1
                
                try:
                    if "pyrogram.Voice" not in str(messaggio) and "new_chat_members" not in str(messaggio) and "empty" not in str(messaggio) and messaggio['from_user']['id'] == mario_id and "reply_to_message" in str(messaggio) and "text" in str(messaggio) and "pyrogram.Animation" not in str(messaggio) and "pyrogram.Sticker" not in str(messaggio) and "pyrogram.Photo" not in str(messaggio) and "pyrogram.Video" not in str(messaggio) and "messageMediaDocument" not in str(messaggio):
                        answer = messaggio['text']
                        question = messaggio['reply_to_message']['text']
                        
                        try:
                            if question not in get_questions():
                                try:
                                    add_value(question, answer)
                                    print("[DB ADD] " + question + " -> " + answer)
                                except:
                                    pass
                                
                            elif question in get_questions() and answer not in get_answers(question):
                                try:
                                    add_answer(question, answer)
                                    print("[ANSWER ADD] " + question + " -> " + answer)
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
                        
            client.send_message(mio_id, "fatto!, " + str(counter))
                        
        if message['text'] == "/ping":
            client.send_message(mio_id, "pong")
            
        if message['text'] == "/leave":
            client.leave_chat(message['chat']['id'])
        
        
        # call this command only when database is at least at 100kb   
        if message['text'] == "/enablechat":
            chat_mode = True
            client.send_message(message['chat']['id'], "chat mode has been enabled")
            
        if message['text'] == "/status":
            if chat_mode:
                client.send_message(message['chat']['id'], "Chat mode is enabled")
            elif not chat_mode:
                client.send_message(message['chat']['id'], "Chat mode is disabled")
            
    if chat_mode == True and message['text'] not in commands:
        if "text" in str(message) and "pyrogram.Animation" not in str(message) and "pyrogram.Sticker" not in str(message) and "pyrogram.Photo" not in str(message) and "pyrogram.Video" not in str(message) and "messageMediaDocument" not in str(message):
            # reply to messages
            question = message['text']
            message_id = message['message_id']
            questions = get_questions()
            
            if question in questions:
                answers = get_answers(question)
                answer = random.choice(answers)
                
                if str(message['chat']['id']).startswith("-100"):
                    if dice():
                        client.read_history(message['chat']['id'])
                        client.send_chat_action(message['chat']['id'], "typing")
                        Timer(random.randint(2,7), send_action_message, [client, message, answer, message_id]).start()
                        
                elif str(message['chat']['id']).startswith("-") == False:
                    client.read_history(message['chat']['id'])
                    client.send_chat_action(message['chat']['id'], "typing")
                    Timer(random.randint(2,7), send_action_message, [client, message, answer, message_id]).start()
            
            elif question not in questions:
                matches = [SequenceMatcher(None, question, str(x)).quick_ratio() for x in questions]
                closest_question = questions[matches.index(max(matches))]
                answers = get_answers(closest_question)
                final_answer = random.choice(answers)
                
                if str(message['chat']['id']).startswith("-100"):
                    if dice():
                        client.read_history(message['chat']['id'])
                        client.send_chat_action(message['chat']['id'], "typing")
                        Timer(random.randint(2,7), send_action_message, [client, message, final_answer, message_id]).start()
                        
                elif str(message['chat']['id']).startswith("-") == False:
                    client.read_history(message['chat']['id'])
                    client.send_chat_action(message['chat']['id'], "typing")
                    Timer(random.randint(2,7), send_action_message, [client, message, final_answer, message_id]).start()


app.run()
