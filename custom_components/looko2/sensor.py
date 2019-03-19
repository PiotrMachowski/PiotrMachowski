from datetime import timedelta
import logging
import requests

import voluptuous as vol

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (CONF_MONITORED_CONDITIONS, CONF_NAME, TEMP_CELSIUS, CONF_API_KEY)
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

CONF_STATION_ID = 'station_id'

DEFAULT_NAME = 'LookO2'

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=60)

SENSOR_TYPES = {
    'AverageHCHO': ['Średni formaldehyd', 'µg/m³'],
    'AveragePM1': ['Średnie PM1', 'µg/m³'],
    'AveragePM10': ['Średnie PM10', 'µg/m³'],
    'AveragePM25': ['Średnie PM2.5', 'µg/m³'],
    'Color': ['Kolor', None],
    'HCHO': ['Formaldehyd', 'µg/m³'],
    'Humidity': ['Wilgotność', '%'],
    'IJP': ['IJP', ' '],
    'IJPDescription': ['IJP Opis', None],
    'IJPDescriptionEN': ['IJP Opis EN', None],
    'IJPString': ['IJP Nazwa', None],
    'IJPStringEN': ['IJP Nazwa EN', None],
    'Indoor': ['Wewnętrzny', None],
    'PM1': ['PM1', 'µg/m³'],
    'PM10': ['PM10', 'µg/m³'],
    'PM25': ['PM2.5', 'µg/m³'],
    'PreviousIJP': ['Poprzednie IJP', ' '],
    'Temperature': ['Temperatura', TEMP_CELSIUS]
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_STATION_ID): cv.string,
    vol.Required(CONF_API_KEY): cv.string,
    vol.Optional(CONF_MONITORED_CONDITIONS, default=[]):
        vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)]),
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    token = config.get(CONF_API_KEY)
    station_id = config.get(CONF_STATION_ID)
    dev = []
    for variable in config[CONF_MONITORED_CONDITIONS]:
        dev.append(LookO2Sensor(name, variable, station_id, token))
    add_entities(dev, True)


class LookO2Sensor(Entity):
    def __init__(self, name, sensor_type, station_id, token):
        self.client_name = name
        self.station_id = station_id
        self.type = sensor_type
        self.token = token
        self.data = None
        self._state = None
        self._unit_of_measurement = SENSOR_TYPES[sensor_type][1]

    @property
    def name(self):
        return '{} {}'.format(self.client_name, self.type)

    @property
    def state(self):
        if self.data is not None:
            self._state = self.data[self.type]
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    def update(self):
        address = 'http://api.looko2.com/?method=GetLOOKO&id=' + self.station_id + '&token=' + self.token
        request = requests.get(address)
        if request.status_code == 200 and request.content.__len__() > 0:
            self.data = request.json()
