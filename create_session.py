from pyrogram import Client

session_name = input("give me a name for the session: ")
app = Client(session_name)

app.start()

warning_message = """
##########################################################################################
############################## THE SESSION HAS BEEN SETUPED ##############################
##########################################################################################
"""

print(warning_message)

app.stop()
exit()
