from scapy.all import Raw,IP
from config import KEYWORDS
from logger import log_credential
from threat_intel import inc

def detect(packet):

    if packet.haslayer(Raw):

        payload=packet[Raw].load.decode(errors="ignore")

        for k in KEYWORDS:

            if k in payload.lower():

                src=packet[IP].src
                dst=packet[IP].dst

                log_credential(src,dst,k,payload)

                inc("credential")

                print("[SOC ALERT] Credential detected")
