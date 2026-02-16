sessions = {}

def track_session(packet):

    key = (packet[0][1].src, packet[0][1].dst)

    if key not in sessions:
        sessions[key] = 0

    sessions[key] += 1

    return sessions[key]
