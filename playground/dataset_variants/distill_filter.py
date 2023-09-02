import argparse
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str, default="~/arena_dataset/clean_conv_20230809_1M.json")
    args = parser.parse_args()

    distill_data = get_distill_data(args.filepath)
