from .verifier import verify_signature


def worker_process(raw_queue, verified_queue, config):
    """
    Core worker performing stateless tasks
    """

    while True:

        packet = raw_queue.get()

        if packet == "STOP":
            break

        valid = verify_signature(packet, config)

        if valid:
            verified_queue.put(packet)