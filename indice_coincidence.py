def indice_coincidence(text):
    text = text.replace(" ", "").upper()

    n = len(text)
    frequence = {}
    for lettre in text:
        if lettre in frequence:
            frequence[lettre] += 1
        else :
            frequence[lettre] = 1
    ic = 0
    for fi in frequence.values():
        ic += fi * (fi - 1)

    if n > 1:
        ic /= n * (n - 1)
    else:
        ic = 0

    return ic

texte = ""
ic = indice_coincidence(texte)
print(f"Le voilà ton putain d'indice de clochard espèce de bouffon va\n{ic : .6f}")
