from aiohttp import web, hdrs
from datetime import datetime

async def handler(request):
    userAgent = request.headers.get(hdrs.USER_AGENT, "Anonymous")
    date = datetime.now().strftime("%Y-%m-%d")

    return web.Response(text=f'Current date is: {date}, \nyour browser is: {userAgent}')


if __name__ == "__main__":
    app = web.Application()
    app.router.add_get("/", handler)

    web.run_app(app)