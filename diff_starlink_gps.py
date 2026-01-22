#!/usr/bin/env python3
import asyncio
from aio_timers import Timer
import websockets
import json
import dict_digger
import math
import threading, time
import paho.mqtt.client as mqtt

# lat/lon in decimal degrees
starlink_lat = 0.0
starlink_lon = 0.0
ais_gps_lat = 0.0
ais_gps_lon = 0.0
plotter_gps_lat = 0.0
plotter_gps_lon = 0.0

#uri = "ws://192.168.1.116:80/signalk/v1/stream?subscribe=self"
uri = "ws://192.168.1.116:80/signalk/v1/stream?subscribe=none"

subscribe = {
  "context": "vessels.self",
  "subscribe": [
    {
      "path": "environment.wind.speedApparent",
      "format": "delta",
      "minPeriod": 10000
    },
    {
      "path": "environment.wind.directionTrue",
      "format": "delta",
      "minPeriod": 10000
    },
    {
      "path": "navigation.courseOverGroundTrue",
      "format": "delta",
      "minPeriod": 10000
    },
    {
      "path": "navigation.speedOverGround",
      "format": "delta",
      "minPeriod": 10000
    },
    {
      "path": "environment.inside.temperature",
      "format": "delta",
      "minPeriod": 10000
    },
    {
      "path": "environment.outside.temperature",
      "format": "delta",
      "minPeriod": 10000
    }
  ]
}

def signalk_parse(msg):
  global plotter_gps_lat, plotter_gps_lon
  global ais_gps_lat, ais_gps_lon
  global starlink_lat, starlink_lon

  try:
    load_json = json.loads(msg)
    updates = dict_digger.dig(load_json, 'updates', 0)
    values = dict_digger.dig(updates, 'values', 0)
    path = values["path"]
#    print("path: ", path)
    if path == "navigation.courseOverGroundTrue":
      path = "COG: "
      COG = round(math.degrees(values["value"]),1)
      coglist.append(COG)
      #print("coglist: ", coglist)
      #print(path, COG, "degrees", updates["timestamp"],"\n")
    elif path == "environment.wind.speedApparent":
      path = "TWS: "
      TWS = round(values["value"] * 1.94384, 1)
      twslist.append(TWS)
      #print(path, TWS, "knots", updates["timestamp"],"\n")
    elif path == "environment.wind.directionTrue":
      path = "TWD: "
      TWD = round(math.degrees(values["value"]),1)
      twdlist.append(TWD)
      #print(path, TWD, "degrees", updates["timestamp"],"\n")
    elif path == "navigation.speedOverGround":
      path = "SOG: "
      SOG = round(values["value"] * 1.94384, 1)
      soglist.append(SOG)
      #print(path, SOG, "knots", updates["timestamp"],"\n")
    elif path == "environment.inside.temperature":
      path = "Cabin Temp: "
      CabinTemp = round(((values["value"] - 273.15) * 9/5) +32, 1)
      #print(path, CabinTemp, "F", updates["timestamp"],"\n")
    elif path == "environment.outside.temperature":
      path = "Cockpit Temp: "
      CockpitTemp = round(((values["value"] - 273.15) * 9/5) +32, 1)
      #print(path, CockpitTemp, "F", updates["timestamp"],"\n")
    return
  except:
    print("\nnot a frame we were looking for")

async def sigk(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(subscribe))
        async for delta in websocket:
          signalk_parse(delta)

#
# Main 
#

asyncio.get_event_loop().run_until_complete(sigk(uri))
