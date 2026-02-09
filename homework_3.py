import flet as ft
from datetime import datetime


def app(page: ft.Page):
    # button = ft.Button(content="Кнопка")
    plain_text = ft.Text(value="Hello world!")
    # page.theme_mode = ft.ThemeMode.LIGHT

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)


    def change(e):
        txt = user_input.value.strip()
        user_input.value = ""

        
        if txt:
            now = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
            plain_text.color = None
            plain_text.value = f"{now} - Привет, {txt}!"
        else:
            plain_text.value = "Введите правельное имя"
            plain_text.color = ft.Colors.RED
 

    # button.content = "Другая кнопка"
    # button.color = ft.Colors.GREEN_900
    btn = ft.TextButton("Отправить", on_click=change)
    user_input = ft.TextField(label="enter name", on_submit=change)
    page.add(
        plain_text,
        user_input,
        btn,
        icon_button,
    )

ft.app(app)