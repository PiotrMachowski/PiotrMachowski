# Antistorm sensor

This sensor uses official API to get storm warnings from [_*Antistorm*_](https://antistorm.eu/).

## Configuration options

| Key | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `name` | `string` | `False` | `Antistorm` | Name of sensor |
| `station_id` | `positive int` | `True` | - | ID of monitored station |
| `monitored_conditions` | `list` | `True` | - | List of conditions to monitor |

### Possible monitored conditions

#### Binary sensor
| Key | Description |
| --- | --- | 
| `storm_alarm` | Status of storm alarm |
| `rain_alarm` | Status of rain alarm |
| `storm_active` | Active storm |

#### Sensor
| Key | Description |
| --- | --- | 
| `storm_probability` | Probability of storm |
| `storm_time` | Estimated time until storm |
| `rain_probability` | Probability of rain |
| `rain_time` | Estimated time until rain |

## Example usage

```
binary_sensor:
  - platform: antistorm
    station_id: 408
    monitored_conditions:
      - 'storm_alarm'
      - 'rain_alarm'
      - 'storm_active'
```

```
sensor:
  - platform: antistorm
    station_id: 408
    monitored_conditions:
      - 'storm_probability'
      - 'storm_time'
      - 'rain_probability'
      - 'rain_time'
```
