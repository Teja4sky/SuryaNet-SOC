from scapy.all import sniff,IP
from protocol_analyzer import analyze
from logger import log_packet
from stats import update
from dashboard import show
from attack_detector import detect as detect_attack
from credential_detector import detect as detect_cred
from ai_detector import analyze as ai
from ip_geo import locate
from sensor_client import send

def process(packet):

    if packet.haslayer(IP):

        src=packet[IP].src
        dst=packet[IP].dst

        proto=analyze(packet)

        size=len(packet)

        log_packet(src,dst,proto,size)

        update({"src":src})

        detect_attack(packet)

        detect_cred(packet)

        ai(size)

        loc=locate(src)

        send(f"{src} {dst} {proto} {loc}")

        show()

def start():

    sniff(prn=process,store=False)
