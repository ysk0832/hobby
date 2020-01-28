from __future__ import print_function
import discord
import pickle
import os
import os.path
import queue
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import commands



# -------------google drive 認証-------------------------------------------------
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']

"""Shows basic usage of the Drive v3 API.
Prints the names and ids of the first 10 files the user has access to.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json', SCOPES)
        creds = flow.run_console()
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('drive', 'v3', credentials=creds)
# --------------------------------------------------------------------------------


# 自分のBotのアクセストークンに置き換えてください
TOKEN = '?????????????????????'

# 接続に必要なオブジェクトを生成
client = discord.Client()

voice = None
audio_queue = queue.Queue()
audiofile_list = []
def check_queue(e):
    os.remove(audiofile_list.pop(0))
    try:
        if not audio_queue.empty():
            audio_source = audio_queue.get()
            voice.play(audio_source,after=check_queue)
    except:
        print(e)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global voice
    guild = message.guild
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content.startswith('/play'):
        voice_channel = client.get_channel(??????????????????)
        voice_client = message.guild.voice_client

        search_word=message.content.split(" ",1)
        results = service.files().list(q="mimeType != 'application/vnd.google-apps.folder' and name contains '"+search_word[1]+"'",
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if len(items) == 0:
            await message.channel.send("その曲はないみたい")
        elif len(items) == 1: #1曲のときのみ再生する
            filename = items[0]['name']
            if not os.path.exists(filename):
                request = service.files().get_media(fileId=items[0]['id']) #httpリクエストを返す
                fh = io.FileIO(filename, "wb")
                downloader = MediaIoBaseDownload(fh, request)
                await message.channel.send("ダウンロードしてくるからちょっと待ってて！")
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print ("Download %d%%." % int(status.progress() * 100))

            audio_source = discord.FFmpegPCMAudio(filename)
            audiofile_list.append(filename)
            if not voice: #ボイチャ接続
                voice = await voice_channel.connect()
            # 再生中，一時停止中はキューに入れる
            if audio_queue.empty() and not voice.is_playing() and not voice.is_paused():
                await message.channel.send("**"+filename+"**を再生するよー！")
                voice.play(audio_source,after=check_queue)
            else:
                await message.channel.send("**"+filename+"**を再生リストに入れておくね！")
                audio_queue.put(audio_source)
        elif len(items) >= 2: #10曲まで表示する
            await message.channel.send("**どれにするー？**")
            await message.channel.send("----------------------------")
            for item in items:
                await message.channel.send(item['name'])
            await message.channel.send("----------------------------")
    
    if message.content.startswith('/stop'):
        # voice_client = message.guild.voice_client
        if voice.is_playing():
            await message.channel.send("曲，止めちゃうの？")
            voice.stop()
        else:
            await message.channel.send("もう止まってるよ？")

    if message.content.startswith('/pause'):
        # voice_client = message.guild.voice_client
        if voice.is_paused():
            await message.channel.send("再開は/resumeだよー")
        else:
            await message.channel.send("一時停止ｸﾞｻｧｰｯ!")
            voice.pause()

    if message.content.startswith('/resume'):
        # voice_client = message.guild.voice_client
        if voice.is_paused():
            await message.channel.send("再開するよ！")
            voice.resume()
        else:
            await message.channel.send("再生中だよー")

    if message.content.startswith('/list'):
        if audiofile_list != []:
            await message.channel.send("今の再生リストはこんな感じだよー")
            await message.channel.send("----------------------------")
            for i in range(0,len(audiofile_list)):
                await message.channel.send("**"+str(i+1)+".** "+audiofile_list[i])
            await message.channel.send("----------------------------")
        else:
            await message.channel.send("静かだねぇ〜")

    if message.content.startswith('/yuzu'):
        await message.channel.send("なになに？柚とお話したいの？")

    if message.content == '/bye':
        await message.channel.send("じゃあねー♪")
        await client.logout()

    if message.content == '/help':
        await message.channel.send(commands.commands)
        await message.channel.send("etc.")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)