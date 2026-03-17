from functools import reduce


def cast_value(value, dtype):

    casts = {
        "integer": int,
        "float": float,
        "string": str
    }

    return casts.get(dtype, lambda x: x)(value)


def map_row_to_packet(row, schema):

    def reducer(packet, column):

        src = column["source_name"]
        dest = column["internal_mapping"]
        dtype = column["data_type"]

        packet[dest] = cast_value(row[src], dtype)

        return packet

    return reduce(reducer, schema, {})