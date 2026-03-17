import time


def telemetry_monitor(raw_q, ver_q, proc_q, telemetry_q, config):

    max_size = config["pipeline_dynamics"]["stream_queue_max_size"]

    while True:

        telemetry_data = {

            "raw": raw_q.qsize() / max_size,
            "verified": ver_q.qsize() / max_size,
            "processed": proc_q.qsize() / max_size
        }

        telemetry_q.put(telemetry_data)

        time.sleep(0.5)