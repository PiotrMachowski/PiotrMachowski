# Tauron AMIplus sensor

This sensor uses unofficial API to get energy usage data from [_*TAURON eLicznik*_](https://elicznik.tauron-dystrybucja.pl).

WARNING: Currently it only supports only G12 tariff.

## Example usage

```
sensor:
  - platform: tauron_amiplus
    name: Tauron AMIPlus
    username: !secret tauron_amiplus.username
    password: !secret tauron_amiplus.password
    energy_meter_id: !secret tauron_amiplus.energy_meter_id
    monitored_variables:
      - zone
      - consumption_daily
      - consumption_monthly
      - consumption_yearly
```
