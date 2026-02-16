from datetime import datetime
from config import PACKET_LOG, ALERT_LOG, CREDENTIAL_LOG

def log_packet(src,dst,proto,length):

    with open(PACKET_LOG,"a",encoding="utf-8") as f:

        f.write(
            f"{datetime.now()} "
            f"{src} -> {dst} "
            f"{proto} LEN={length}\n"
        )

def log_alert(type,src,dst,info):

    with open(ALERT_LOG,"a",encoding="utf-8") as f:

        f.write(
            f"{datetime.now()} ALERT "
            f"{type} {src} -> {dst} "
            f"{info}\n"
        )

def log_credential(src,dst,keyword,data):

    with open(CREDENTIAL_LOG,"a",encoding="utf-8") as f:

        f.write(
            f"{datetime.now()} "
            f"{src} -> {dst} "
            f"{keyword} {data[:100]}\n"
        )
