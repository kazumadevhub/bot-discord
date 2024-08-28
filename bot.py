import discord
import os

# Inisialisasi objek Client dengan Intents
intents = discord.Intents.default()
intents.message_content = True  # Memberikan izin untuk membaca konten pesan

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Menghindari bot merespons dirinya sendiri
    if message.author == client.user:
        return

    # Perintah sederhana
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Menjalankan bot menggunakan token yang disimpan di environment variable
client.run(os.getenv('DISCORD_TOKEN'))