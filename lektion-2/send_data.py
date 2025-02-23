import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Din anslutningssträng från IoT Hub
CONNECTION_STRING = "HostName=iot-hub-demo.azure-devices.net;DeviceId=sensor-pi;SharedAccessKey=XXXXXX"

# Skapa en IoT Hub-klient
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_telemetry():
    while True:
        temperature = round(random.uniform(20, 30), 2)
        humidity = round(random.uniform(30, 50), 2)
        message = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')
        
        print(f"Skickar data: {message}")
        client.send_message(message)
        
        time.sleep(5)

try:
    send_telemetry()
except KeyboardInterrupt:
    print("Avslutar...")
    client.disconnect()
