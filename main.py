import flet as ft
import os
import shutil
import zipfile


def main(page: ft.Page):
    options = {}
    def load_packages(path_packages,path_build):
        """Copy the dependencies in the app.zip generated in build"""
        packages_to_load = []
        path_app = path_build + "\\windows\\data\\flutter_assets\\app\\app.zip"
        for option in path_packages.controls:
            if option.value:
                packages_to_load.append(option.label)
        current_dir = os.path.abspath(".")
        loader = current_dir + "\\__pypackages__"
        if not os.path.exists(loader):
            os.makedirs(loader)
        for pack in packages_to_load:
            module_to_load = options[pack]
            shutil.copytree(module_to_load,loader + f"\\{pack}",dirs_exist_ok=True)
        with zipfile.ZipFile(path_app,"r") as zip_file:
            zip_file.extractall(".\\temp")
            shutil.copytree(".\\__pypackages__\\",".\\temp\\__pypackages__\\",dirs_exist_ok=True)
        os.remove(path_app)
        shutil.make_archive(path_app[:-4],"zip",".\\temp\\")
            

        shutil.rmtree(loader)
        shutil.rmtree(".\\temp")
        text_select.controls.append(ft.Text("✅ Loading completed successfully"))
        text_select.update()
            
    def give_path_packages(e):
        """Get path to packages from pickle_packages"""
        nonlocal options
        ciclo = 0
        for element in os.listdir(e.path):
            path_package = e.path + f"\\{element}"
            if os.path.isdir(path_package):
                # packages[element] = path_package
                ciclo += 1
                options[element] = path_package
        for pack in options.keys():
            check = ft.Switch(label=f"{pack}")
            text_select.controls.append(check)
            text_select.update()
        
    
    def give_path_build(e):
        """Get path to build from pickle_build"""
        input_build.value = e.path if e.path else ""
        input_build.update()
    
    # Componets
    layout = ft.Column()
    field_packages = ft.Row()
    field_build = ft.Row()
    
    # Pickle
    pickle_packages = ft.FilePicker(on_result=give_path_packages)
    pickle_build = ft.FilePicker(on_result=give_path_build)
    page.add(pickle_packages,pickle_build)
    
    # Path
    input_packages = ft.TextField(
        hint_text="Path to Packages",
        )
    button_packages = ft.FilledButton(
        text="Packages",
        icon=ft.icons.DRIVE_FILE_MOVE_RTL_SHARP,
        icon_color=ft.colors.YELLOW_200,
        expand=True,
        on_click= lambda _: pickle_packages.get_directory_path("Select the path to Packages")
    )
    
    input_build = ft.TextField(
        hint_text="Path to build"
        )
    
    button_build = ft.FilledButton(
        text="Build",
        icon=ft.icons.DRIVE_FILE_MOVE_RTL_SHARP,
        icon_color=ft.colors.YELLOW_200,
        expand=True,
        on_click= lambda _: pickle_build.get_directory_path("Select the path to Build"),
    )
    
    field_packages.controls.append(input_packages)
    field_packages.controls.append(button_packages)
    field_build.controls.append(input_build)
    field_build.controls.append(button_build)
    
    # Button load packages
    field_button = ft.Row()
    confirm_button = ft.FilledButton(
        text="Ok",
        icon=ft.icons.CHECK_CIRCLE_OUTLINE_OUTLINED,
        icon_color=ft.colors.LIGHT_GREEN_500,
        on_click=lambda _:load_packages(text_select,input_build.value),
        expand=True,
        adaptive=True
    )
    field_button.controls.append(confirm_button)
    
    
    layout.controls.append(field_packages)
    layout.controls.append(field_build)
    layout.controls.append(field_button)
    
    # View select packages
    field_select = ft.Column()
    text_select = ft.ListView(auto_scroll=True)
    field_select.controls.append(text_select)
    
    layout.controls.append(field_select)
    
    
    
    page.add(layout)
    page.title = "Flet Packages Loader"
    page.window_height = 400
    page.window_width = 300
    page.update()

ft.app(target=main, assets_dir=".\\assets")
