from cryomech_communicate import *
from datetime import datetime, timezone
import influxdb_client, os, time
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client import Point, WriteOptions, WritePrecision
import keyring

PT310_IPADDRESS = "192.168.0.67"
PT425_IPADDRESS = "192.168.0.68"

# InfluxDB
BUCKET = "RaX_Lab"
ORG = "RaXcollab"
URL = "http://localhost:8086"

LOOP_DELAY_SECONDS = 1


def main():
    # Initialize compressors
    pt310 = PTC(PT425_IPADDRESS)
    pt425 = PTC(PT425_IPADDRESS)

    devices = [pt310, pt425]
    device_ids = ["PT310 Compressor", "PT425 Compressor"]

    # Connect to InfluxDB
    token = keyring.get_password("InfluxDB_Token", "influx")
    client = influxdb_client.InfluxDBClient(url=URL, token=token, org=ORG)
    write_api = client.write_api(write_options=SYNCHRONOUS)


    try:
        while True:
            points = []
            for device, device_id in zip(devices, device_ids):
                dataflag, data = device.get_data()
                timestamp = datetime.now(timezone.utc)

                if not dataflag:
                    datapoint = (
                        Point("CompressorReadings")
                        .tag("sensor_id", device_id)
                        .time(timestamp)
                    )

                    for key, value in data.items():
                        clean_key = key.replace(" ", "_") # Remove spaces in keys
                        datapoint = datapoint.field(key, value)

                    points.append(datapoint)

            write_api.write(bucket=BUCKET, org=ORG, record=points) # InfluxDB
            time.sleep(LOOP_DELAY_SECONDS)

    except KeyboardInterrupt:
        print("Program closed by KeyboardInterrupt, exiting")

    finally:
        try:
            write_api.flush()
        except:
            pass
        client.close()




if __name__ == "__main__":
    main()
