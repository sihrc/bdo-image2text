
from aiohttp import web

from bdo.threads import threaded
from bdo.image_to_names import main as name_extraction

routes = web.RouteTableDef()

name_extraction = threaded(name_extraction)

@routes.post('/image2text')
async def extract(request):
    try:
        data = await request.json()
        link = data["link"]
        names = await name_extraction(link)

        return web.json_response({
            "names": names
        })
    except:
        import traceback; traceback.print_exc()
        return web.json_response({
            "names": [],
            "error": "something failed"
        })


app = web.Application()
app.add_routes(routes)
web.run_app(app)
