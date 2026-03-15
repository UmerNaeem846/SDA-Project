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


def create_workers(n, raw_q, ver_q, config):

    return list(
        map(
            lambda _: multiprocessing.Process(
                target=worker_process,
                args=(raw_q, ver_q, config)
            ),
            range(n)
        )
    )


def main():

    config = load_config()

    size = config["pipeline_dynamics"]["stream_queue_max_size"]

    raw_q = multiprocessing.Queue(maxsize=size)
    ver_q = multiprocessing.Queue(maxsize=size)
    proc_q = multiprocessing.Queue(maxsize=size)

    workers = create_workers(
        config["pipeline_dynamics"]["core_parallelism"],
        raw_q,
        ver_q,
        config
    )

    input_p = multiprocessing.Process(
        target=input_process,
        args=(raw_q, config)
    )

    aggregator = multiprocessing.Process(
        target=aggregator_process,
        args=(ver_q, proc_q, config)
    )

    dashboard = multiprocessing.Process(
        target=dashboard_process,
        args=(proc_q,)
    )

    telemetry = multiprocessing.Process(
        target=telemetry_monitor,
        args=(raw_q, ver_q, proc_q, config)
    )

    processes = [input_p, aggregator, dashboard, telemetry] + workers

    list(map(lambda p: p.start(), processes))

    input_p.join()


if __name__ == "__main__":
    main()