from chatterbot import ChatBot #importing chatbot 
from chatterbot.trainers import ListTrainer #method to train chatbot
import os
# here we are defining bot with its various featurs
bot = ChatBot('module chatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            # thresold value is used for confidence level
            'default_response': 'I am sorry, but I do not understand.'
            # default_response will be sent is confidence level will below 70%
        }
    ],
    trainer='chatterbot.trainers.ListTrainer') # creating chatbot
bot.set_trainer(ListTrainer) #setting the trainer
# loading files from chat directory
# getting files unsing listdir() method
for _file in os.listdir('chat_data'):
	conversations= open('chat_data/'+_file,'r').readlines() 
	bot.train(conversations) #training the bot with data 