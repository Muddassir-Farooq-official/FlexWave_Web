import flet as ft
import requests
from style import *

class Register_View(ft.Container):
    def __init__(self):
        super().__init__()

        # Placeholder for fetched fields and their details
        self.fields_data = []
        self.selected_price = 0
        self.discount = 0  # Default discount in percentage
        self.total = 0  # Initial total
        self.month = 1  # Default duration

        # Dropdown for "Select Field"
        self.field = ft.Dropdown(
            label="Select Field",
            border_color=theme_color,
            label_style=field_theme,
            options=[],
            color=theme_color,
            on_change=self.update_total
        )

        # Fetch fields from API
        self.fetch_fields()

        # Create other widgets
        self.name = ft.TextField(
            label="Full Name",
            border_color=theme_color,
            label_style=field_theme,
            cursor_color=theme_color
        )
        self.email = ft.TextField(
            label="Email",
            border_color=theme_color,
            label_style=field_theme,
            cursor_color=theme_color
        )
        self.phone = ft.TextField(
            label="Phone No",
            border_color=theme_color,
            label_style=field_theme,
            cursor_color=theme_color
        )
        self.preference = ft.Dropdown(
            label="Select Preference",
            border_color=theme_color,
            label_style=field_theme,
            options=[
                ft.dropdown.Option("Online Classes"),
                ft.dropdown.Option("Physical Classes")
            ],
            color=theme_color
        )
        self.code = ft.TextField(
            label="Coupon Code",
            border_color=theme_color,
            label_style=field_theme,
            cursor_color=theme_color,
            on_change=self.apply_discount
        )

        # Billing display
        self.bill = ft.Container(
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Grand Total", weight="bold"),
                            ft.Text(f"Discount: {self.discount}%"),
                            ft.Text(f"Total: {self.total}"),
                        ],
                    ),
                    ft.Column(
                        [
                            ft.Text(""),
                            ft.Text(""),
                            ft.Text(f"Duration: {self.month} (Month)"),
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        )

        self.btn = ft.FilledButton(
            "Register Now",
            width=500,
            style=ft.ButtonStyle(
                bgcolor=theme_color, color=ft.colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
        )

        # Main content
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Enter Required Details To Enroll in SDP"),
                    self.name,
                    self.email,
                    self.phone,
                    self.field,
                    self.preference,
                    self.code,
                    self.bill,
                    self.btn
                ],
            ),
            padding=5,
            border_radius=20,
            margin=10,
            width=500,
            alignment=ft.alignment.center
        )

    def fetch_fields(self):
        """Fetch fields data from the API."""
        try:
            response = requests.get("https://flexwave-backend.onrender.com/Fields")
            if response.status_code == 200:
                data = response.json()
                self.fields_data = data.get("fields", [])
                self.update_dropdown()
            else:
                print(f"Failed to fetch fields: {response.status_code}")
        except Exception as e:
            print(f"Error fetching fields: {e}")

    def update_dropdown(self):
        """Update dropdown options based on fetched fields data."""
        self.field.options = [
            ft.dropdown.Option(field[1]) for field in self.fields_data
        ]
        self.field.update()

    def update_total(self, e=None):
        """Update the total and duration based on the selected field."""
        selected_field = self.field.value
        for field in self.fields_data:
            if field[1] == selected_field:
                self.selected_price = field[2]
                self.month = field[3]  # Assuming duration is in the 4th column of field data
                break

        # Apply discount and calculate total
        discounted_price = self.selected_price - (self.selected_price * self.discount / 100)
        self.total = round(discounted_price, 2)

        # Update the UI
        self.bill.content.controls[0].controls[1].value = f"Discount: {self.discount}%"
        self.bill.content.controls[0].controls[2].value = f"Total: {self.total}"
        self.bill.content.controls[1].controls[2].value = f"Duration: {self.month} (Month)"
        self.bill.update()

    def apply_discount(self, e):
        """Apply discount based on the coupon code."""
        entered_code = self.code.value.strip().lower()
        if entered_code == "getx001":
            self.discount = 10
        else:
            self.discount = 0

        # Update the total with the new discount
        self.update_total()
