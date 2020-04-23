import telebot

"""
A simple bot for telegram.
It returns the chat id wherever the command is called.

To make it work on a channel, add the bot to the channel, then type:
    /getchannelid@bot
    where bot is the name of the bot

Remember to add the bottoken to the code as a string.
"""

bot = telebot.TeleBot(bottoken)

@bot.channel_post_handler(commands=["getchannelid"])
def chatid(message):
    bot.reply_to(message,'channel_id = {!s}'.format(message.chat.id))

bot.polling()
