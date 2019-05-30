# Custom ROM Discord Bot
Can show latest builds from official devices for each respective supported roms.

prefix: !
#### Supported ROMS:
* AOSP Extended (aex/aospextended)
* Android Open Source illusion Project (aosip/illusion)
* BootleggersROM (btlg/bootleggers)
* crDroid (crdroid)
* DotOS (dotos/dot)
* Evolution-X (evo/evox/evolutionx)
* HavocOS (havoc/havocos)
* LineageOS (los/lineage)
* PearlOS (pearl)
* Pixel Experience (pe/pixelexperience)
* PixysOS (pixy/pixys/pixysos)
* Potato Open Sauce Project (posp/potato/potatorom)
* Resurrection Remix (rr/ressurection/ressurectionremix/ressurectionremixos)
* RevengeOS(revenge/revengeos)
* SuperiorOS(superior/superioros)
* Syberia (syberia)
* ViperOS (viper/viperos)

### How to setup:
##### On Windows:

```
py -3 -m pip install -r requirements.txt
```
##### On Ubuntu/Linux:
```
python3 -m pip install -r requirements.txt
```

Then add an environment variable for your token:
##### Windows:
```
setx token (token here) /M
```

##### Ubuntu/Linux:
```
export token=(token here)
```

### How to use:
 Start it by:
 ```
 python3 main.py
 ```
 add the bot to your server, then do !help
