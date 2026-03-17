import csv
import time
from utils.schema_mapper import map_row_to_packet


def input_process(raw_q, config):

    path = config["dataset_path"]
    delay = config["pipeline_dynamics"]["input_delay_seconds"]
    schema = config["schema_mapping"]["columns"]

    with open(path) as f:

        reader = csv.DictReader(f)

        for row in reader:

            packet = map_row_to_packet(row, schema)

            raw_q.put(packet)

            time.sleep(delay)

    # send stop signals for workers
    workers = config["pipeline_dynamics"]["core_parallelism"]

    for _ in range(workers):
        raw_q.put("STOP")