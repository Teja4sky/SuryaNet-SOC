from scapy.all import *
from config import SUSPICIOUS_PORTS
from logger import log_alert

def detect_threat(packet):

    if packet.haslayer(TCP):

        src = packet[IP].src
        dst = packet[IP].dst
        dport = packet[TCP].dport

        if dport in SUSPICIOUS_PORTS:

            log_alert(
                "Suspicious Port Access",
                src,
                dst,
                f"Port {dport}"
            )

            print(f"[ALERT] Suspicious port access → {dport}")
