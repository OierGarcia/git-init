def agur(izena="Lagun", hizkuntza="eu"):
    if hizkuntza == "es":
        print(f"¡Hola, {izena}!")
    elif hizkuntza == "en":
        print(f"Hello, {izena}!")
    else:
        print(f"Kaixo, {izena}!")


def agur_eman():
    print("Gero arte!")


if __name__ == "__main__":
    agur("Oier", "eu")
    agur("Mikel", "es")
    agur_eman()
