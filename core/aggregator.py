def compute_running_average(values):
    """
    Functional core (pure function)
    """

    if len(values) == 0:
        return 0

    return sum(values) / len(values)


def aggregator_process(verified_queue, processed_queue, config):

    window_size = config["processing"]["stateful_tasks"]["running_average_window_size"]

    window = []

    while True:

        packet = verified_queue.get()

        if packet == "STOP":
            break

        value = packet["metric_value"]

        window.append(value)

        if len(window) > window_size:
            window.pop(0)

        avg = compute_running_average(window)

        packet["computed_metric"] = avg

        processed_queue.put(packet)