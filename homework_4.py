import flet as ft
from datetime import datetime


def app(page: ft.Page):
    # button = ft.Button(content="Кнопка")
    plain_text = ft.Text(value="Hello world!")
    # page.theme_mode = ft.ThemeMode.LIGHT
    history = []

    def clear_history(e):
        history.clear()
        history_text.value = ""

    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    history_text = ft.Text()

    def sort_history(e):
        history.sort()
        history_text.value = "История имен: \n"+", \n".join(history)

    sort_button = ft.TextButton("Сортировать по алфовиту", on_click=sort_history)



    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)


    def change(e):
        txt = user_input.value.strip()
        user_input.value = ""
        history.append(txt)
        history_text.value = "История имен: \n"+", \n".join(history)
        date = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

        
        if txt:
            plain_text.color = None
            plain_text.value = f"{date} - Привет, {txt}!"
        else:
            plain_text.value = "Введите правельное имя"
            plain_text.color = ft.Colors.RED
 

    # button.content = "Другая кнопка"
    # button.color = ft.Colors.GREEN_900
    btn = ft.TextButton("Отправить", on_click=change)
    user_input = ft.TextField(label="enter name", on_submit=change)
    icon_row = ft.Row([icon_button], alignment=ft.MainAxisAlignment.END)
    row = ft.Row(
        [user_input, btn, icon_button ],
         alignment=ft.MainAxisAlignment.START,
    )

    main_row = ft.Row([row, icon_row], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(
        plain_text,
        row,
        history_text,
        sort_button,
        delete_button,
    )

ft.app(app)