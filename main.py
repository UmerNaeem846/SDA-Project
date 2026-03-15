import json
import multiprocessing

from core.worker import worker_process
from core.aggregator import aggregator_process


def load_config():

    with open("config/config.json") as f:
        return json.load(f)


def create_workers(raw_queue, verified_queue, config):

    workers = []

    num_workers = config["pipeline_dynamics"]["core_parallelism"]

    for _ in range(num_workers):

        p = multiprocessing.Process(
            target=worker_process,
            args=(raw_queue, verified_queue, config)
        )

        p.start()
        workers.append(p)

    return workers


def create_aggregator(verified_queue, processed_queue, config):

    p = multiprocessing.Process(
        target=aggregator_process,
        args=(verified_queue, processed_queue, config)
    )

    p.start()

    return p


def main():

    config = load_config()

    queue_size = config["pipeline_dynamics"]["stream_queue_max_size"]

    raw_queue = multiprocessing.Queue(maxsize=queue_size)
    verified_queue = multiprocessing.Queue(maxsize=queue_size)
    processed_queue = multiprocessing.Queue(maxsize=queue_size)

    workers = create_workers(raw_queue, verified_queue, config)

    aggregator = create_aggregator(
        verified_queue,
        processed_queue,
        config
    )

    print("Core pipeline started.")
    print("Workers running:", len(workers))

    # Placeholder until Input Module pushes data
    while True:
        pass


if __name__ == "__main__":
    main()