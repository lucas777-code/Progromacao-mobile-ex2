import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Função para alternar tema claro/escuro
    def alternar_tema(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    # Campos de entrada
    peso = ft.TextField(
        label="Peso (kg)",
        width=300,
        prefix_icon=ft.Icons.FITNESS_CENTER,
    )

    altura = ft.TextField(
        label="Altura (m)",
        width=300,
        prefix_icon=ft.Icons.HEIGHT,
    )

    # Texto resultado
    resultado = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)

    # Função para calcular IMC
    def calcular_imc(e):
        try:
            p = float(peso.value)
            a = float(altura.value)
            imc = p / (a * a)
            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 24.9:
                classificacao = "Peso normal"
            elif imc < 29.9:
                classificacao = "Sobrepeso"
            else:
                classificacao = "Obesidade"
            resultado.value = f"IMC: {imc:.2f} - {classificacao}"
        except:
            resultado.value = "Informe valores válidos!"
        page.update()

    # Função para limpar
    def limpar(e):
        peso.value = ""
        altura.value = ""
        resultado.value = ""
        page.update()

    # Botões (cores corrigidas)
    btn_calcular = ft.ElevatedButton(
        text="Calcular IMC",
        bgcolor="#673AB7",  # Deep Purple
        color="white",
        on_click=calcular_imc,
    )

    btn_limpar = ft.ElevatedButton(
        text="Limpar",
        bgcolor="red",
        color="white",
        on_click=limpar,
    )

    # Ícone do tema
    icone_tema = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        on_click=alternar_tema,
        tooltip="Alternar tema",
    )

    # Layout final
    page.add(
        ft.Column(
            [
                ft.Row(
                    [ft.Text("Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD)],
                    alignment="center",
                ),
                ft.Row(
                    [ft.Text("Informe seus dados", size=16)],
                    alignment="center",
                ),
                peso,
                altura,
                ft.Row([btn_calcular, btn_limpar], alignment="spaceAround"),
                resultado,
            ],
            spacing=20,
            horizontal_alignment="center",
        ),
        icone_tema,
    )

# Executar app
ft.app(target=main, view=ft.WEB_BROWSER)