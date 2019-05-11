# Lovelace Xiaomi Vacuum Map card

This card enables you to specify target or start zoned cleanup using map, just like in Xiaomi Home app. Additionally you can define a list of zones and choose ones to be cleaned.


![Example](https://github.com/PiotrMachowski/Home-Assistant/blob/master/custom_lovelace_cards/xiaomi_vacuum_map_card/s1.png)

## Go to target
![Go to target](https://github.com/PiotrMachowski/Home-Assistant/blob/master/custom_lovelace_cards/xiaomi_vacuum_map_card/s2.png)

## Zoned cleanup
![Zoned cleanup](https://github.com/PiotrMachowski/Home-Assistant/blob/master/custom_lovelace_cards/xiaomi_vacuum_map_card/s3.png)

## Defined zones
![Defined zones](https://github.com/PiotrMachowski/Home-Assistant/blob/master/custom_lovelace_cards/xiaomi_vacuum_map_card/s4.png)

## Installation
1. Download [xiaomi-vacuum-map-card.js](https://github.com/PiotrMachowski/Home-Assistant/raw/master/custom_lovelace_cards/xiaomi_vacuum_map_card/xiaomi-vacuum-map-card.js), [texts.js](https://github.com/PiotrMachowski/Home-Assistant/raw/master/custom_lovelace_cards/xiaomi_vacuum_map_card/texts.js) and [style.js](https://github.com/PiotrMachowski/Home-Assistant/raw/master/custom_lovelace_cards/xiaomi_vacuum_map_card/style.js) to `/www/custom_lovelace/xiaomi_vacuum_map_card` folder
2. Add card to resources:
```yaml
resources:
  - url: /local/custom_lovelace/xiaomi_vacuum_map_card/xiaomi-vacuum-map-card.js
    type: module
```

## Configuration
Example:
```yaml
views:
- name: Example
  cards:
  - type: custom:xiaomi-vacuum-map-card
    entity: vacuum.xiaomi_vacuum
    map_image: '/local/custom_lovelace/xiaomi_vacuum_map_card/map.png'
    base_position:
      x: 1889
      y: 1600
    reference_point:
      x: 1625
      y: 1336
    zones:
      - [[25500, 25500, 26500, 26500]]
      - [[24215, 28125, 29465, 32175]]
      - [[24245, 25190, 27495, 27940], [27492, 26789, 28942, 27889]]
      - [[28972, 26715, 31072, 27915], [29457, 27903, 31107, 29203], [30198, 29215, 31498, 31215], [29461, 31228, 31511, 32478]]
```
* `map_image` - path to image of a map
* `base_position` - coordinates of pixel corresponding to `[25500, 25500]` on the map image
* `reference_point` - coordinates of pixel corresponding to `[26500, 26500]` on the map image
* `zones` - list of zones (optional)

### Hints
* To find out values for `base_position` and `reference_point` use service `vacuum.send_command` with data:
  * `base_postion`:
    ```json
    {
      "entity_id": "vacuum.xiaomi_vacuum",
      "command": "app_goto_target",
      "params": [25500, 25500]
    }
    ```
  * `reference_point`:
    ```json
    {
      "entity_id": "vacuum.xiaomi_vacuum",
      "command": "app_goto_target",
      "params": [26500, 26500]
    }
    ```
* You can find out coordinates for zones using app [FloleVac](https://play.google.com/store/apps/details?id=de.flole.xiaomi)

* For Polish version download [textsPL.js](https://github.com/PiotrMachowski/Home-Assistant/raw/master/custom_lovelace_cards/xiaomi_vacuum_map_card/textsPL.js) and change filename to `texts.js`