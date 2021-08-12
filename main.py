from telethon import TelegramClient, events

client = TelegramClient('session', id, 'token')

# MessageReceiver
@client.on(events.NewMessage())
async def event_handler(event):

    await event.message.mark_read()
    if "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')
    elif "Your_string" in event.text.lower():
        await event.message.forward_to('me')


# My personal, test.
@client.on(events.NewMessage(from_users=My_id))
async def my_handler(event):
    await event.message.mark_read()
    await event.reply("Everything works!")

client.start()

client.run_until_disconnected()
