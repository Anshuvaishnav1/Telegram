from telethon import TelegramClient, events

client = TelegramClient('KnowYourEnemy', 2004793, 'ccf2ff5e4d22e084fce49aeb43a61adc')

"""client = TelegramClient(None, 2004793, 'ccf2ff5e4d22e084fce49aeb43a61adc')
client.session.set_dc(6, '149.154.167.50', 80 )"""

# MessageReceiver
@client.on(events.NewMessage())
async def event_handler(event):

    await event.message.mark_read()
    if "эстония" in event.text.lower():
        await event.message.forward_to('me')
    elif "эстонии" in event.text.lower():
        await event.message.forward_to('me')
    elif "🇪🇪" in event.text.lower():
        await event.message.forward_to('me')
    elif "силы обороны эстонии" in event.text.lower():
        await event.message.forward_to('me')
    elif "армия эстонии" in event.text.lower():
        await event.message.forward_to('me')
    elif "президент эстонии" in event.text.lower():
        await event.message.forward_to('me')
    elif "таллин" in event.text.lower():
        await event.message.forward_to('me')
    elif "юри луйк" in event.text.lower():
        await event.message.forward_to('me')


# MInu personal, test.
@client.on(events.NewMessage(from_users=627702907))
async def my_handler(event):
    await event.message.mark_read()
    await event.reply("Everything is okay")

client.start()

client.run_until_disconnected()
