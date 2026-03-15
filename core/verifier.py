import hashlib


def verify_signature(packet, config):
    """
    Stateless verification using PBKDF2-HMAC
    """

    try:

        secret_key = config["processing"]["stateless_tasks"]["secret_key"]
        iterations = config["processing"]["stateless_tasks"]["iterations"]

        value = packet["metric_value"]
        received_hash = packet["security_hash"]

        # dataset requires rounding to 2 decimals
        value_str = f"{value:.2f}"

        computed_hash = hashlib.pbkdf2_hmac(
            "sha256",
            secret_key.encode(),
            value_str.encode(),
            iterations
        ).hex()

        return computed_hash == received_hash

    except Exception:
        return False