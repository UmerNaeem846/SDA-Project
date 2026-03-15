import hashlib


def compute_hash(value, secret, iterations):

    value_str = f"{value:.2f}"

    return hashlib.pbkdf2_hmac(
        "sha256",
        secret.encode(),
        value_str.encode(),
        iterations
    ).hex()


def verify_signature(packet, config):

    secret = config["processing"]["stateless_tasks"]["secret_key"]
    iterations = config["processing"]["stateless_tasks"]["iterations"]

    expected_hash = compute_hash(packet["metric_value"], secret, iterations)

    return expected_hash == packet["security_hash"]