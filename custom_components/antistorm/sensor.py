import logging
import requests

import voluptuous as vol

from homeassistant.components.sensor import (PLATFORM_SCHEMA, ENTITY_ID_FORMAT)
from homeassistant.const import CONF_MONITORED_CONDITIONS, CONF_NAME
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity import async_generate_entity_id

_LOGGER = logging.getLogger(__name__)

CONF_STATION_ID = 'station_id'

DEFAULT_NAME = 'Antistorm'

SENSOR_TYPES = {
    'storm_probability': ['p_b', 'Prawdopodobieństwo burzy', ' '],
    'storm_time': ['t_b', 'Czas do burzy', ' '],
    'rain_probability': ['p_o', 'Prawdopodobieństwo opadów', ' '],
    'rain_time': ['t_o', 'Czas do opadów', ' '],
}

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME, default=DEFAULT_NAME): cv.string,
    vol.Required(CONF_STATION_ID): cv.string,
    vol.Required(CONF_MONITORED_CONDITIONS, default=[]):
        vol.All(cv.ensure_list, [vol.In(SENSOR_TYPES)])
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    station_id = config.get(CONF_STATION_ID)
    name = config.get(CONF_NAME)
    address = 'http://antistorm.eu/webservice.php?id=' + str(station_id)
    request = requests.get(address)
    request.encoding = 'utf-8'
    city_name = request.json()['m']
    dev = []
    for monitored_condition in config[CONF_MONITORED_CONDITIONS]:
        uid = '{}_{}_{}'.format(DEFAULT_NAME, station_id, monitored_condition)
        entity_id = async_generate_entity_id(ENTITY_ID_FORMAT, uid, hass=hass)
        dev.append(AntistormSensor(entity_id, name, city_name, monitored_condition, station_id))
    add_entities(dev, True)


class AntistormSensor(Entity):
    def __init__(self, entity_id, name, city_name, sensor_type, station_id):
        self.entity_id = entity_id
        self._name = name
        self.city_name = city_name
        self.station_id = station_id
        self.sensor_type = sensor_type
        self.data = None
        self._state = None
        self._jsonParameter = SENSOR_TYPES[sensor_type][0]
        self._name = SENSOR_TYPES[sensor_type][1]
        self._unit_of_measurement = SENSOR_TYPES[sensor_type][2]

    @property
    def name(self):
        return '{} {} - {}'.format(self._name, self.city_name, SENSOR_TYPES[self.sensor_type][1])

    @property
    def state(self):
        if self.data is not None:
            self._state = self.data[self._jsonParameter]
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    def update(self):
        address = 'http://antistorm.eu/webservice.php?id=' + str(self.station_id)
        request = requests.get(address)
        if request.status_code == 200 and request.content.__len__() > 0:
            self.data = request.json()
