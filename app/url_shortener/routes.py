from app.short_link_service.views import index


# настраиваем пути, которые будут вести к нашей странице
def setup_routes(app):
   app.router.add_route('POST', '/', index)
   app.router.add_route('GET', '/', index)