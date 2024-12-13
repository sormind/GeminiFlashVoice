import asyncio
import base64
import json
import os
import pyaudio
from websockets.asyncio.client import connect

class SimpleGeminiVoice:
    def __init__(self):
        self.audio_queue = asyncio.Queue()
        self.api_key = os.getenv("GEMINI_API_KEY", "your_api_key_here")
        if self.api_key == "your_api_key_here":
            raise ValueError("Set 'GEMINI_API_KEY' in env or script.")
        self.model = "gemini-2.0-flash-exp"
        self.uri = f"wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1alpha.GenerativeService?key={self.api_key}"
        self.FORMAT, self.CHANNELS, self.RATE, self.CHUNK = pyaudio.paInt16, 1, 16000, 512

    async def start(self):
        try:
            print("Connecting to Gemini...")
            self.ws = await connect(self.uri, additional_headers={"Content-Type": "application/json"})
            await self.ws.send(json.dumps({"setup": {"model": f"models/{self.model}"}}))
            print("Connected! Start talking...")
            async with asyncio.TaskGroup() as tg:
                tg.create_task(self.capture_audio())
                tg.create_task(self.stream_audio())
                tg.create_task(self.play_response())
        except Exception as e:
            print(f"Error: {e}")

    async def capture_audio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)
        while True:
            data = await asyncio.to_thread(stream.read, self.CHUNK)
            await self.ws.send(json.dumps({"realtime_input": {
                "media_chunks": [{"data": base64.b64encode(data).decode("utf-8"), "mime_type": "audio/pcm"}]
            }}))

    async def stream_audio(self):
        while True:
            try:
                response = json.loads(await self.ws.recv())
                audio_data = base64.b64decode(response["serverContent"]["modelTurn"]["parts"][0]["inlineData"]["data"])
                await self.audio_queue.put(audio_data)
            except Exception:
                pass

    async def play_response(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=24000, output=True)
        while True:
            data = await self.audio_queue.get()
            await asyncio.to_thread(stream.write, data)

if __name__ == "__main__":
    try:
        asyncio.run(SimpleGeminiVoice().start())
    except KeyboardInterrupt:
        print("\nExiting...")