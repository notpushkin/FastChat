import argparse
import json


def get_distill_data(filepath):
    with open(filepath, "r") as f:
        all_data = json.load(f)
    print(all_data[0].keys())

    distill_data = []
    for conv in all_data:
        if conv["model"] in ["claude-1", "claude-instant-1", "gpt-4", "claude-2"]:
            distill_data.apend(conv)

    models = set()
    for conv in distill_data:
        models.add(conv["model"])
    print(models)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--filepath", type=str, default="clean_conv_20230809_1M.json")
    args = parser.parse_args()

    distill_data = get_distill_data(args.filepath)
