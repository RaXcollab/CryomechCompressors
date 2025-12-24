# OBSOLETE

This repo has been archived, superseded by [RaXcollab/LabMonitoring](https://github.com/RaXcollab/LabMonitoring).

# Cryomech Communicate

This is a simple python client to communicate with Cryomech corporation cyrogenetic
helium compressors to read and write state information over ModBus TCP

## Usage

```
usage: cryomech_communicate.py [-h] --ip IP [--port PORT]

Dump Cryomech Data

options:
  -h, --help   show this help message and exit
  --ip IP      IP of cryomech device (default: None)
  --port PORT  port for ModBusTCP (default: 502)
```

Just point the software at the IP address of the cryomech to query the status,
it returns a json string:
```
$ cryomech_communicate.py --ip 1.2.3.4
{"datetime": "2022-10-05T10:16:52.766194", "Operating State": "Running", "Compressor State": "On", "Warning State": "No warnings", "Alarm State": "No warnings", "Coolant In Temp": 71.13200378417969, "Coolant Out Temp": 97.32599639892578, "Oil Temp": 99.0469970703125, "Helium Temp": 150.86099243164062, "Low Pressure": 71.3375015258789, "Low Pressure Average": 77.24246978759766, "High Pressure": 288.22088623046875, "High Pressure Average": 291.1910705566406, "Delta Pressure Average": 216.88339233398438, "Motor Current": 26.719694137573242, "Hours of Opperation": 24735.5, "Pressure Unit": "psi", "Temperature Unit": "F", "Serial Number": XXXXX, "Model": "28H7", "Software Revision": "2.155"}
```

Use `jq` for improved formatting if examining on the command line:
```
$ cryomech_communicate.py --ip 1.2.3.4 | jq
{
  "datetime": "2022-10-05T10:19:27.848124",
  "Operating State": "Running",
  "Compressor State": "On",
  "Warning State": "No warnings",
  "Alarm State": "No warnings",
  "Coolant In Temp": 70.84400177001953,
  "Coolant Out Temp": 97.16300201416016,
  "Oil Temp": 98.9260025024414,
  "Helium Temp": 150.87100219726562,
  "Low Pressure": 82.19590759277344,
  "Low Pressure Average": 77.18533325195312,
  "High Pressure": 292.0447998046875,
  "High Pressure Average": 291.2262878417969,
  "Delta Pressure Average": 209.84889221191406,
  "Motor Current": 26.52256965637207,
  "Hours of Opperation": 24735.5,
  "Pressure Unit": "psi",
  "Temperature Unit": "F",
  "Serial Number": XXXX,
  "Model": "28H7",
  "Software Revision": "2.155"
}
```
