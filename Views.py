import flet as ft
from style import *
from Home import *
from Register import *


logo =ft.Container(
                    content=ft.Image(
                        src="https://miflexwave.com/wp-content/uploads/2024/10/cropped-Untitled-design-1-e1730014625178.png.webp",
                        height=200
                    ),
                    alignment=ft.alignment.center
                )
def Home(page):
    print("Adding home view", flush=True)
    # Add box1 to the page first before animating it
    page.views.append(
        ft.View(
            "/",
            [
                logo,
                ft.Container(
                    content=ft.Row(
                        [
                            ft.TextButton("Courses", style=home_button_theme),
                            ft.TextButton("Register", style=home_button_theme,
                                on_click=lambda _: page.go("/Register")),
                            ft.TextButton("Login", style=home_button_theme),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    bgcolor='black',padding=10
                ),
                Home_View(),
                ft.BottomAppBar(
                    ft.Text("Powered By FlexWave Technologies",color='white',
                            text_align="center"),
                    
                    bgcolor='black',height=50
                )

            ],
            padding=0,
            bgcolor=''
        )
    )
    page.update()
    return page.views


def Register(page):
    print("Adding Register view", flush=True)
    # Add box1 to the page first before animating it
    page.views.append(
        ft.View(
            "/Register",
            [
                ft.AppBar(
                    leading=ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_color='white',
                        on_click=lambda _: page.go("/")
                    ),
                    title=ft.Text("Register Now",color='white'),
                    bgcolor=theme_color
                ),
                logo,
                Register_View(),
                ft.BottomAppBar(
                    ft.Text("Powered By FlexWave Technologies",color='white',
                            text_align="center"),
                    
                    bgcolor='black',height=50
                )

            ],
            padding=0,
            bgcolor='',
            horizontal_alignment="center",
            scroll=ft.ScrollMode.HIDDEN,
            
        )
    )
    page.update()
    return page.views