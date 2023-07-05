from sense_hat import SenseHat
import time
import yaml


# Open the YAML file and load its content
with open("sensors/config.yaml", "r") as file:
    config = yaml.safe_load(file)

sensors = {"humidity": 0, "temp": 0, "pressure": 0}
device_id = config["device_id"]
interval = float(config["event"]["humidity_temp_pressure"]["data_generation_interval"])

# setup sensehat
sense = SenseHat()

while True:
    fresh = {"humidity": sense.humidity, "temp": sense.temp, "pressure": sense.pressure}
    for key, val in fresh.items():
        if val != sensors[key]:
            message = f"{device_id} | {key} | {val} | {int(time.time())}"
            print(message)
            sensors[key] = val
        time.sleep(interval)