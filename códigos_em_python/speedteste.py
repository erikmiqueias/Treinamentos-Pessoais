# Testando velocidade de Internet com python
import speedtest
from time import sleep

spt = speedtest.Speedtest()
spt.get_best_server()

spt_ping = spt.results.ping
spt_download = round(spt.download() / 1000 / 1000, 1)
spt_upload = round(spt.upload() / 1000 / 1000, 1)

print(f"Velocidade de Download {spt_download}")
print(f"Velocidae de Upload {spt_upload}")
print(f"Nível de Ping {spt_ping:.2f}")