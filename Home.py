import flet as ft

class Home_View(ft.Container):
    def __init__(self):
        super().__init__()

        # Dropdown for Product Status
        self.box1 = ft.Container(
                    content=ft.Text("FlexWave Learning Management System (LMS) Is Under Development",text_align="center"),
                     bgcolor='',padding=10,
                     alignment=ft.alignment.center
                )
        
        # Main content with Dropdown and data display container
        self.content = ft.Container(
            content=ft.Column(
                [
                    self.box1
                ],
            ),
            padding=5,
            border_radius=20,
            margin=10,
        )