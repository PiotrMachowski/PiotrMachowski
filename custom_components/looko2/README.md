# LookO2 sensor

This sensor uses official API to get air quality data [_*LookO2*_](https://looko2.com/).

## Example usage

```
sensor:
  - platform: looko2
    api_key: !secret looko2.api_key
    name: LookO2
    station_id: '5CCF7F0C2E8B'
    scan_interval:
      minutes: 5
    monitored_conditions:
      - 'AverageHCHO'
      - 'AveragePM1'
      - 'AveragePM10'
      - 'AveragePM25'
      - 'Color'
      - 'HCHO'
      - 'Humidity'
      - 'IJP'
      - 'IJPDescription'
      - 'IJPDescriptionEN'
      - 'IJPString'
      - 'IJPStringEN'
      - 'Indoor'
      - 'PM1'
      - 'PM10'
      - 'PM25'
      - 'PreviousIJP'
      - 'Temperature
```
