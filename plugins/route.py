#(©)𝔭𝔞𝔫𝔦𝔪𝔢𝔦𝔡





from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("𝔭𝔞𝔫𝔦𝔪𝔢𝔦𝔡")
