#!env /usr/bin/python3

import asyncio
import websockets
import json
import dict_digger
from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    R = 3959.87433 # this is in miles. For Earth radius in kilometers use 6372.8 km
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
    c = 2*asin(sqrt(a))
    return R * c

async def subscribe_with_source():
    # URI for your specific server address
    uri = "ws://192.168.1.116:80/signalk/v1/stream?subscribe=none"

    async with websockets.connect(uri) as websocket:
        # Subscribe to position with instant updates
        msg = {
            "context": "vessels.self",
            "subscribe": [{"path": "navigation.position",
                           "policy": "instant"}]
            #               "minPeriod": 1000}]
        }
        await websocket.send(json.dumps(msg))

        gps_lat = 0.0
        gps_lon = 0.0
        starlink_lat = 0.0
        starlink_lon = 0.0

        while True:
            try:
                message = await websocket.recv()
                data = json.loads(message)

                if "updates" in data:
                    for update in data["updates"]:
                        # print (update)

                        if (dict_digger.dig(update, "source", "type") == "NMEA2000"):
                            gps_lat = dict_digger.dig(update, "values", 0, "value", "latitude")
                            gps_lon = dict_digger.dig(update, "values", 0, "value", "longitude")
                        elif (dict_digger.dig(update, "$source") == "signalk-starlink"):
                            starlink_lat = dict_digger.dig(update, "values", 0, "value", "latitude")
                            starlink_lon = dict_digger.dig(update, "values", 0, "value", "longitude")
                            if (starlink_lat is not None and starlink_lon is not None
                                and gps_lat is not None and gps_lon is not None):
                                print ("Starlink Lat: ", starlink_lat, "Lon: ", starlink_lon)
                                print ("GPS Lat: ", gps_lat, "Lon: ", gps_lon)
                                distance = haversine(gps_lat, gps_lon, starlink_lat, starlink_lon)
                                print("Distance between GPS and Starlink: ", distance, "miles\n")
                        else:
                            print("Failed to parse source info")
                            print (update)

            except Exception as e:
                print(f"Error: {e}")
                break

if __name__ == "__main__":
    asyncio.run(subscribe_with_source())

