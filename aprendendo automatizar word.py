#automacao de criacao arquivos Word

from docx import Document

documento = Document()
documento.add_heading('Titulo o documento',0)
documento.save('demo.docx')