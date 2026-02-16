import time

packet_count = 0
start_time = time.time()
active_ips = set()

def update(packet):

    global packet_count

    packet_count += 1

    try:
        active_ips.add(packet["src"])
    except:
        pass

def get():

    elapsed = time.time() - start_time

    pps = packet_count / elapsed if elapsed>0 else 0

    return {

        "packets":packet_count,
        "pps":round(pps,2),
        "ips":len(active_ips)
    }
