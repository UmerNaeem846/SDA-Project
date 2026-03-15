from .verifier import verify_signature


def worker_process(raw_q, verified_q, config):

    while True:

        packet = raw_q.get()

        if packet == "STOP":
            verified_q.put("STOP")
            break

        if verify_signature(packet, config):

            verified_q.put(packet)