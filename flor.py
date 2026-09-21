import os
import flet as ft 

def main(page: ft.Page):
    page.title = "21 de Septiembre - Flores Amarillas"
    page.padding = 0  # Sin márgenes para llenar la pantalla
    page.window.width = 600 
    page.window.height = 650 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    
    # --- VISTA 1: FORMULARIO DE LOGIN ---
    texto_login = ft.Text(
        "💛🌻 LOGIN 💛🌻",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.ORANGE_400
    )
    
    texto_login_2 = ft.Text(
        "INGRESA SOLO CON TÚ NOMBRE 🌻🌻",
        size=20,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.ORANGE_400
    )

    login_input = ft.TextField(
        label="Nombre",
        hint_text="Ej. Nombre",
        border_radius=12,
        border_color=ft.Colors.AMBER_400,
        focused_border_color=ft.Colors.YELLOW_300,
        cursor_color=ft.Colors.AMBER_400,
        text_size=16,
        filled=True,
        bgcolor=ft.Colors.PURPLE_900,
        label_style=ft.TextStyle(color=ft.Colors.AMBER_200),
        prefix_icon=ft.Icons.LOCAL_FLORIST,
        text_style=ft.TextStyle(
            size=14,
            color=ft.Colors.AMBER_100,
            italic=True,
            font_family="Times New Roman"
        )
    )

    # --- VISTA 2: ELEMENTOS DE BIENVENIDA ---
    texto_bienvenida = ft.Text(
        size=22,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.AMBER_300,
        text_align=ft.TextAlign.CENTER
    )

    # Imagen de la flor amarilla (reemplaza al icono anterior)
    imagen_flor = ft.Image(
        src="2.jpeg",        # Archivo de la imagen del ramo de flores
        width=280,
        height=170,
        fit="cover",
        border_radius=15
    )

    # --- EVENTOS DE NAVEGACIÓN Y VALIDACIÓN ---
    def entrar_click(e):
        if not login_input.value or not login_input.value.strip():
            login_input.error_text = "Por favor ingrese su nombre"
            page.update()
            return 

        login_input.error_text = None
        # Texto actualizado con las frases solicitadas
        texto_bienvenida.value = (
            f"¡Holaaaaaaaa, {login_input.value.strip()}\n"
            f"Felíz 21 de Septiembre\n"
            f"Yo el Ing. Emanuel con mi aprecio\n"
            f"Te regalo una flor amarilla 🌻\n"
            f"No te quedes sin presumir hoy amiga/amigo!"
        )
        
        frame_login.visible = False
        frame_bienvenida.visible = True
        page.update()

    def volver_click(e):
        login_input.value = ""
        frame_bienvenida.visible = False
        frame_login.visible = True
        page.update()

    # --- BOTONES ---
    bot_entrar = ft.Button(
        content=ft.Text("Entrar", weight=ft.FontWeight.BOLD),
        icon=ft.Icons.SEARCH,
        style=ft.ButtonStyle(
            color=ft.Colors.PURPLE_900,
            bgcolor=ft.Colors.AMBER_400,
            padding=12,
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        height=45,
        width=130,
        on_click=entrar_click
    )

    bot_volver = ft.Button(
        content=ft.Text("Volver", weight=ft.FontWeight.BOLD),
        icon=ft.Icons.ARROW_BACK,
        style=ft.ButtonStyle(
            color=ft.Colors.PURPLE_900,
            bgcolor=ft.Colors.AMBER_400,
            padding=12,
            shape=ft.RoundedRectangleBorder(radius=12)
        ),
        height=45,
        width=130,
        on_click=volver_click
    )

    # --- MARCO 1: LOGIN ---
    frame_login = ft.Container(
        content=ft.Column(
            controls=[texto_login,texto_login_2, login_input, bot_entrar],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            width=380
        ),
        alignment=ft.Alignment(0, 0),
        expand=True,
        padding=20,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[ft.Colors.YELLOW_300, ft.Colors.AMBER_500]
        ),
        visible=True
    )

    # --- MARCO 2: BIENVENIDA CON IMAGEN Y MENSAJE ---
    frame_bienvenida = ft.Container(
        image=ft.DecorationImage(
            src="1.jpeg",  # Imagen de fondo
            fit="cover"
        ),
        content=ft.Container(
            content=ft.Column(
                controls=[
                    texto_bienvenida,
                    imagen_flor,  # Muestra la imagen 2.jpeg en lugar del icono
                    bot_volver
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=18
            ),
            bgcolor="#CC000000",
            padding=25,
            border_radius=20,
            border=ft.Border.all(2, ft.Colors.AMBER_400),
            width=430
        ),
        alignment=ft.Alignment(0, 0),
        expand=True,
        visible=False
    )

    page.add(frame_login, frame_bienvenida)

ft.run(main, assets_dir=".")
