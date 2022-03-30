from infra.config import Database
from infra.Models import SeleniumKeys

def auth(empresa):
    infra = Database().infra
    selenium_keys = infra.query(SeleniumKeys).filter_by(id_empresas=82).first()
    return selenium_keys.rdstation_user, selenium_keys.rdstation_pass
