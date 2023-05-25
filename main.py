from sanic import Sanic
from sanic.response import json
import aiohttp

app = Sanic("my-hello-world-app")

async def fetch(client):
    async with client.get('http://python.org') as resp:
        assert resp.status == 200
        return await resp.text()

client = aiohttp.ClientSession()

@app.route('/')
async def test(request):
    async with aiohttp.ClientSession() as client:
        html = await fetch(client)
        return json({"html": html})


if __name__ == '__main__':
    app.run()
