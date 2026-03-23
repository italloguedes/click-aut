"""
Auto Clicker - Automação de cliques do mouse em posições da tela.

Instalação das dependências:
    pip install pyautogui keyboard

Uso:
    1. Execute como Administrador: python auto_clicker.py
    2. Para SALVAR uma posição: Ctrl + F7/F8/F9/F10/F11
    3. Para CLICAR na posição salva: F7/F8/F9/F10/F11
    4. ESC para encerrar.
"""

import pyautogui
import keyboard
import sys

pyautogui.FAILSAFE = True

# Posições salvas
posicoes: dict[str, tuple[int, int]] = {}

TECLAS = {
    "f1":  "1ª",
    "f2":  "2ª",
    "f3":  "3ª",
    "f4":  "4ª",
    "f5":  "5ª",
    "f6":  "6ª",
    "f7":  "7ª",
    "f8":  "8ª",
    "f9":  "9ª",
    "f10": "10ª",
    "f11": "11ª",
    "f12": "12ª",
}


def salvar_posicao(tecla: str):
    """Ctrl+F7–F11 → salva a posição atual do mouse."""
    label = TECLAS[tecla]
    x, y = pyautogui.position()
    posicoes[tecla] = (x, y)
    print(f"  ✔ {label} posição ({tecla.upper()}) salva: ({x}, {y})")


def clicar_posicao(tecla: str):
    """F7–F11 → clica na posição salva."""
    label = TECLAS[tecla]
    if tecla not in posicoes:
        print(f"  ⚠ {label} posição ({tecla.upper()}) ainda não foi salva! Use Ctrl+{tecla.upper()} antes.")
        return
    x, y = posicoes[tecla]
    print(f"  ▶ Clicando na {label} posição ({tecla.upper()}): ({x}, {y})")
    pyautogui.click(x, y)


def encerrar():
    print("\n  ✖ Programa encerrado (ESC).\n")
    sys.exit(0)


def main():
    print("=" * 56)
    print("         AUTO CLICKER — Automação de Cliques")
    print("=" * 56)
    print()
    print("  SALVAR posição:   Ctrl + F7 / F8 / F9 / F10 / F11")
    print("  CLICAR posição:         F7 / F8 / F9 / F10 / F11")
    print("  ENCERRAR:               ESC")
    print()
    print("  Fluxo:")
    print("    1. Posicione o mouse onde deseja clicar.")
    print("    2. Pressione Ctrl+F7 (ou F8, F9...) para salvar.")
    print("    3. Pressione F7 (ou F8, F9...) para clicar lá.")
    print("-" * 56)
    print()

    # Registrar hotkeys
    for tecla in TECLAS:
        # Ctrl+Fx → salvar
        keyboard.add_hotkey(f"ctrl+{tecla}", salvar_posicao, args=(tecla,), suppress=True)
        # Fx → clicar
        keyboard.add_hotkey(tecla, clicar_posicao, args=(tecla,), suppress=True)

    keyboard.add_hotkey("esc", encerrar)

    print("  Aguardando comandos...\n")
    keyboard.wait()


if __name__ == "__main__":
    main()
