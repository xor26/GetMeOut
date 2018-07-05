import requests

from ComingTransportModel import ComingTransportModel
from Gateway import Gateway

url = "http://transport.orgp.spb.ru/Portal/transport/stops/poi/arrive"

params = {'poi-id': '25778'}

respond = requests.get(url=url, params=params)
jsonArray = respond.json()
gate = Gateway()
gate.flushTransportTable()
for upcomingTransport in jsonArray['result']['forecast']:
    upcomingTransportModel = ComingTransportModel(
        upcomingTransport['routeNumber'],
        upcomingTransport['vehicleLabel'],
        upcomingTransport['arrivingTime']
    )
    gate.saveTransportModel(upcomingTransportModel)
    print(upcomingTransportModel.__dict__)

print('end')
