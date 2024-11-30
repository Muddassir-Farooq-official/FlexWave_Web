import flet as ft

from Views import *

def route_change(route_event, page):
    route = route_event.route
    print("Route change:", route)
    if route == "/":
        print("Hello")
        Home(page)

    elif route == "/Register":
        print("Register")
        Register(page)
    
    
    
    
    print("Current views:", page.views)
    page.update()


def view_pop(view, page):
    page.views.pop()
    top_view = page.views[-1]
    page.go(top_view.route)


def main(page: ft.Page):
    page.title = "Routes Example"
    page.on_route_change = lambda route: route_change(route, page)
    page.on_view_pop = lambda view: view_pop(view, page)
    page.go(page.route)
    page.theme_mode = 'light'
    page.window_width = 370
    page.auto_scroll = True
    page.window.always_on_top = True



app = ft.app(target=main,view=ft.WEB_BROWSER,export_asgi_app=True,port=8000)
