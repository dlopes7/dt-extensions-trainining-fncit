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
        navios = self.get_ships()
        for navio in navios:
            log.info(f"Processando navio {navio.get('ship_name', 'Desconhecido')}")

            # Cria o custom device, que vai receber as metricas
            device = grupo.create_device(navio.get('ship_id'), navio.get('ship_name'))

            # Manda um valor absoluto
            device.absolute("combustivel", navio.get("fuel"))

            # Adiciona metricas com dimensao
            for motor in navio.get("thrust"):
                device.absolute("potencia", motor.get("power"), dimensions={"Motor": motor.get("engine")})

            # Adiciona endpoint (topologia)
            device.add_endpoint(navio.get("ship_ip"))

            # Adiciona propriedades (max 20)
            device.report_property("Tipo", f"{navio.get('ship_type')}")
            device.report_property("Ano construido", f"{navio.get('year_built')}")
            device.report_property("Porto", f"{navio.get('home_port')}")

            device.state_metric("clima", navio.get("weather"))

    def get_ships(self) -> List[Dict[str, Any]]:
        # Obtem a lista de navios
        return requests.get(self.config.get("url")).json()



