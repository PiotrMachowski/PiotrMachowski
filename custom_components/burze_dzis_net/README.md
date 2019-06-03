# Burze.dzis.net sensor

This sensor uses official API to get weather warnings [_*Burze.dzis.net*_](https://burze.dzis.net/).

## Configuration options

| Key | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `False` | `Burze.dzis.net` | Name of sensor |
| `api_key` | `string` | `True` | - | API key for Burze.dzis.net |
| `latitude` | `float` | `False` | Latitude of home | Latitude of monitored point. |
| `longitude` | `float` | `False` | Longitude of home | Longitude of monitored point. |
| `warnings` | `list` | `False` | - | List of monitored warnings. |
| `storms_nearby` | - | `False` | - | Enables monitoring nearby storms. |

### Configuration options of `storms_nearby`

| Key | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `radius` | `positive int` | `True` | - | Radius of nearby storms monitoring. |

### Possible monitored warnings

| Key | Description |
| --- | --- | 
| `frost_warning` | Enables frost warnings monitoring |
| `heat_warning` | Enables heat warnings monitoring |
| `wind_warning` | Enables wind warnings monitoring |
| `precipitation_warning` | Enables precipitation warnings monitoring |
| `storm_warning` | Enables storm warnings monitoring |
| `tornado_warning` | Enables tornado warnings monitoring |

## Example usage

```
sensor:
  - platform: burze_dzis_net
    api_key: !secret burze_dzis_net.api_key
    warnings:
      - frost_warning
      - heat_warning
      - wind_warning
      - precipitation_warning
      - storm_warning
      - tornado_warning
    storms_nearby:
      radius: 30
```
