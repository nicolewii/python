#using the guide documentation of https://chatterbot.readthedocs.io/en/stable/ 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('MyChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english') 

while True:
    user_input = input("User: ")
    response = chatbot.get_response(user_input)
    print("ChatBot:", response)