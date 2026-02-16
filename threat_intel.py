attack_stats = {

    "port_scan":0,
    "dos":0,
    "credential":0,
    "ai_anomaly":0
}

def inc(type):

    attack_stats[type]+=1

def get():

    return attack_stats
