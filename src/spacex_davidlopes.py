import logging
from typing import List, Dict, Any

import requests
from ruxit.api.base_plugin import RemoteBasePlugin


log = logging.getLogger(__name__)


class SpaceXExtension(RemoteBasePlugin):

    def query(self, **kwargs):
        meu_nome = "David Lopes"

        # Cria um grupo, usado para criar Custom Devices
        grupo = self.topology_builder.create_group(f"{meu_nome} Navios", f"{meu_nome} Navios")

        # Obtem a lista de navios
        navios = get_ships()
        for navio in navios:
            log.info(f"Processando navio {navio.get('ship_name', 'Desconhecido')}")

            # Cria o custom device, que vai receber as metricas
            device = grupo.create_device(navio.get('ship_id'), navio.get('ship_name'))

            # Manda um valor absoluto
            device.absolute("combustivel", navio.get("fuel"))


def get_ships() -> List[Dict[str, Any]]:
    # Obtem a lista de navios
    return requests.get("http://ec2-18-232-50-149.compute-1.amazonaws.com/v3/ships").json()



