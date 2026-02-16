import time
from scapy.all import IP,TCP
from logger import log_alert
from threat_intel import inc

scan={}
dos={}

def detect(packet):

    try:

        src=packet[IP].src

    except:
        return

    now=time.time()

    if packet.haslayer(TCP):

        port=packet[TCP].dport

        if src not in scan:
            scan[src]=[]

        scan[src].append((port,now))

        recent=[p for p,t in scan[src] if now-t<5]

        if len(set(recent))>10:

            log_alert("Port Scan",src,"network","multiple ports")

            inc("port_scan")

            print("[SOC ALERT] Port Scan",src)

            scan[src]=[]

    if src not in dos:
        dos[src]=[]

    dos[src].append(now)

    recent=[t for t in dos[src] if now-t<5]

    if len(recent)>50:

        log_alert("DoS",src,"network","flood")

        inc("dos")

        print("[SOC ALERT] DoS",src)

        dos[src]=[]
