import json
import multiprocessing

from core.worker import worker_process
from core.aggregator import aggregator_process

from input.input_reader import input_process
from output.dashboard import dashboard_process
from telemetry.telemetry_monitor import telemetry_monitor


def load_config():

    with open("config/config.json") as f:
        return json.load(f)


def create_workers(n, raw_q, verified_q, config):

    workers = []

    for _ in range(n):

        p = multiprocessing.Process(
            target=worker_process,
            args=(raw_q, verified_q, config)
        )

        workers.append(p)

    return workers


def main():

    config = load_config()

    size = config["pipeline_dynamics"]["stream_queue_max_size"]

    raw_q = multiprocessing.Queue(maxsize=size)
    verified_q = multiprocessing.Queue(maxsize=size)
    processed_q = multiprocessing.Queue(maxsize=size)

    telemetry_q = multiprocessing.Queue()

    workers = create_workers(
        config["pipeline_dynamics"]["core_parallelism"],
        raw_q,
        verified_q,
        config
    )

    input_p = multiprocessing.Process(
        target=input_process,
        args=(raw_q, config)
    )

    aggregator = multiprocessing.Process(
        target=aggregator_process,
        args=(verified_q, processed_q, config)
    )

    dashboard = multiprocessing.Process(
        target=dashboard_process,
        args=(processed_q, telemetry_q)
    )

    telemetry = multiprocessing.Process(
        target=telemetry_monitor,
        args=(raw_q, verified_q, processed_q, telemetry_q, config)
    )

    processes = [input_p, aggregator, dashboard, telemetry] + workers

    for p in processes:
        p.start()

    input_p.join()


if __name__ == "__main__":
    main()