import argparse


def get_args():
    parser = argparse.ArgumentParser(description="multimodel response aggregator")
    parser.add_argument(
        "-p",
        "--prompt",
        required=True,
        default="return a hello world python script",
        help="prompt for the model",
    )
    args = parser.parse_args()
    return args
