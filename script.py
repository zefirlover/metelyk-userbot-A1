from pyrogram import Client, types

api_id = 18533141
api_hash = "1a4ca40f3d29182267c4a506a1e6e644"

chat_id = "@FormatA1_UUA"
reaction = "🖕"
app = Client("my_account", api_id, api_hash)

async def main():
    async with app:
        # get_chat_history(chat_id, 20) get last 20 messages
        async for messages in app.get_chat_history(chat_id, 10):
            print(messages.reactions)
            if messages.reactions == [] or messages.reactions == None or messages.reactions != [types.Reaction(count=int,chosen=True,emoji=reaction)]:
                await app.send_reaction(chat_id, messages.id, reaction)

app.run(main())