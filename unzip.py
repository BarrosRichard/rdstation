import zipfile
import os

def unzip(empresa):
    with zipfile.ZipFile(f'./leads/{empresa.name_project}/rd-bild-leads-todos-os-contatos-da-base-de-leads.zip', 'r') as zip_ref:
        zip_ref.extractall(f'./leads/{empresa.name_project}')

    os.remove(f'./leads/{empresa.name_project}/rd-bild-leads-todos-os-contatos-da-base-de-leads.zip')
