import flet as ft
import os


def load_packages(path_packages,path_build):
    pass

def main(page: ft.Page):
    def give_path_packages(e):
        pass
    
    def give_path_build(e):
        pass
    
    field_packages = ft.Row()
    field_build = ft.Row()
    pickle_packages = ft.FilePicker(on_result=give_path_packages())
    pickle_build = ft.FilePicker(on_result=give_path_build())
    page.add(pickle_packages)
    field_button = ft.FilledButton(
        text="Ok",
        icon=ft.icons.CHECK_CIRCLE_OUTLINE_OUTLINED,
        icon_color=ft.colors.LIGHT_GREEN_500,
        on_click=lambda _:load_packages()
    )


ft.app(target=main)
