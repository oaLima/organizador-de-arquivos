from pathlib import Path

pasta_dowloads = Path.home() / "Downloads"

mapeamento ={
    "Imagens" : [".jpg", ".jpeg", ".png"],
    "Documentos": [".pdf", ".docx", ".txt", ".pptx", ".odt"],
    "Planilhas": [".xlsx"],
    "Videos": [".mp4"],
    "Compactados": [".zip", ".rar", ".7z"],
}

for pasta in mapeamento.keys():
    nova_pasta = pasta_dowloads / pasta
    nova_pasta.mkdir(exist_ok=True)

for arquivo in pasta_dowloads.iterdir():
    if arquivo.is_file():
        extensao = arquivo.suffix.lower()
        movido = False

        for pasta, extensoes in mapeamento.items():
            if extensao in extensoes:
                destino = pasta_dowloads / pasta /arquivo.name
                arquivo.rename(destino)
                movido = True
                break

        if not movido:
            outros_pasta = pasta_dowloads / "Outros"
            outros_pasta.mkdir(exist_ok=True)
            arquivo.rename(pasta_dowloads / "Outros" / arquivo.name)


print("Pasta organizada")
