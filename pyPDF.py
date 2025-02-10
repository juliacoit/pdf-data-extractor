from PyPDF2 import PdfReader

# Caminho do arquivo PDF (use r"caminho" para evitar problemas com barras invertidas no Windows)
caminho_pdf = r'pdfs\diagClasse.pdf'

# Abrir o PDF
reader = PdfReader(caminho_pdf)

# Número total de páginas
print(f"Total de páginas: {len(reader.pages)}\n")

# Iterar sobre todas as páginas e imprimir o texto
for i, page in enumerate(reader.pages):
    print(f"--- Página {i + 1} ---\n")
    print(page.extract_text())
    print("\n" + "-" * 40 + "\n")  # Separador entre páginas
