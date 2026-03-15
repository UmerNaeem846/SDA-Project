from .verifier import verify_signature


def worker_process(raw_queue, verified_queue, config):

    while True:

        packet = raw_queue.get()

        if packet == "STOP":
            verified_queue.put("STOP")
            break

        if verify_signature(packet, config):

            verified_queue.put(packet)