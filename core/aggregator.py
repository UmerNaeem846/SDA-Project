from functools import reduce


def compute_average(values):

    if not values:
        return 0

    total = reduce(lambda a, b: a + b, values)

    return total / len(values)


def update_window(window, value, size):

    new_window = window + [value]

    return new_window[-size:]


def aggregator_process(verified_queue, processed_queue, config):

    size = config["processing"]["stateful_tasks"]["running_average_window_size"]

    window = []

    while True:

        packet = verified_queue.get()

        if packet == "STOP":
            processed_queue.put("STOP")
            break

        value = packet["metric_value"]

        window = update_window(window, value, size)

        avg = compute_average(window)

        packet["computed_metric"] = avg

        processed_queue.put(packet)