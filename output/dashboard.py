import matplotlib.pyplot as plt # type:ignore


def get_color(value):

    if value < 0.3:
        return "green"

    elif value < 0.7:
        return "yellow"

    else:
        return "red"


def dashboard_process(processed_q, telemetry_q):

    xs = []
    values = []
    avgs = []

    plt.ion()

    fig = plt.figure(figsize=(10,8))

    ax_graph = fig.add_subplot(211)
    ax_telemetry = fig.add_subplot(212)

    while True:

        if not processed_q.empty():

            packet = processed_q.get()

            if packet == "STOP":
                break

            xs.append(packet["time_period"])
            values.append(packet["metric_value"])
            avgs.append(packet["computed_metric"])

        if not telemetry_q.empty():

            telemetry = telemetry_q.get()

            raw = telemetry["raw"]
            ver = telemetry["verified"]
            proc = telemetry["processed"]

            ax_telemetry.clear()

            ax_telemetry.barh(
                ["Raw Queue","Verified Queue","Processed Queue"],
                [raw, ver, proc],
                color=[
                    get_color(raw),
                    get_color(ver),
                    get_color(proc)
                ]
            )

            ax_telemetry.set_xlim(0,1)
            ax_telemetry.set_title("Pipeline Telemetry")

        ax_graph.clear()

        ax_graph.plot(xs, values, label="Sensor Value")
        ax_graph.plot(xs, avgs, label="Running Average")

        ax_graph.set_title("Live Sensor Values")
        ax_graph.set_xlabel("Time")
        ax_graph.set_ylabel("Value")

        ax_graph.legend()

        plt.pause(0.01)