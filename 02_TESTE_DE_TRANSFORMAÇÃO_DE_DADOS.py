import pdfplumber
import zipfile
import csv
import os

try:
    with zipfile.ZipFile('anexos.zip', 'r') as f:
        f.extractall()
except:
    print('Nao existe o arquivo "anexos.zip"')

csv_filename = "tabela.csv"

with pdfplumber.open("Anexo1.pdf") as pdf:
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for numpage, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            for table in tables:
                for num, row in enumerate(table):
                    if row[4] == "AMB":
                        row[4] = "Seg. Ambulatorial"

                    if row[3] == "OD":
                        row[3] = "Seg. Odontológica"

                    if num != 0 or numpage == 3:
                        writer.writerow(row)

with zipfile.ZipFile('Teste_Gabriel.zip', 'w') as zip:
    zip.write('tabela.csv')
