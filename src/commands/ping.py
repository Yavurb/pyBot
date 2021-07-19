import time

async def ping(message, client):
  before = time.monotonic()
  message = await message.channel.send("Pong!")
  ping = (time.monotonic() - before) * 1000
  await message.edit(content=f"Pong 🏓 \n`ping took {int(ping)}ms`")
  print(f'Ping  {int(ping)}ms')