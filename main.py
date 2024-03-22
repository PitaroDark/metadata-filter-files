import os
import sys
import docx
import openpyxl
import PyPDF2

def extract_docx_metadata(file_path):
    doc = docx.Document(file_path)
    metadata = {}
    properties = [a for a in dir(doc.core_properties) if not a.startswith('__')]
    for prop in properties:
        metadata[prop] = getattr(doc.core_properties, prop)
    return metadata

def extract_xlsx_metadata(file_path):
    wb = openpyxl.load_workbook(filename=file_path)
    metadata = {}
    props = wb.properties
    metadata['title'] = props.title
    metadata['author'] = props.creator
    metadata['created'] = props.created
    metadata['modified'] = props.modified
    return metadata

def extract_pdf_metadata(file_path):
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        metadata = reader.getDocumentInfo()
    return metadata

def extract_metadata(file_path):
    _, extension = os.path.splitext(file_path)
    if extension == '.docx':
        return extract_docx_metadata(file_path)
    elif extension == '.xlsx':
        return extract_xlsx_metadata(file_path)
    elif extension == '.pdf':
        return extract_pdf_metadata(file_path)
    else:
        return None

def main(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            metadata = extract_metadata(file_path)
            if metadata:
                print(end='\n\n')
                print(f"Metadata for {file}:")
                for key, value in metadata.items():
                    print(f"{key}: {value}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Modo de uso: python main.py <directorio absoluto> || python3 main.py <directorio absoluto>")
        sys.exit(1)
    directory = sys.argv[1]
    main(directory)
    print(end='\n')
    print("Proceso finalizado", end='\n\n')