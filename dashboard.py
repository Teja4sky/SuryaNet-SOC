import os
from stats import get
from threat_intel import get as get_threat

def clear():
    os.system("cls")

def show():

    clear()

    s=get()
    t=get_threat()

    print("========= SuryaNet SOC =========")

    print("Packets:",s["packets"])
    print("PPS:",s["pps"])
    print("Active IPs:",s["ips"])

    print("\nATTACKS")

    print("Port Scan:",t["port_scan"])
    print("DoS:",t["dos"])
    print("Credential:",t["credential"])
    print("AI:",t["ai_anomaly"])
