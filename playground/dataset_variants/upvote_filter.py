import argparse
import json


def gen_upvote_data(input_file, output_file):
    with open(input_file, "r") as f:
        all_data = json.load(f)
    print(all_data[0])
    print(all_data[0].keys())

    upvote_data = []
    for conv in all_data:
        if conv["model"] not in ["claude-1", "claude-instant-1", "claude-2", "palm-2", "gpt-4", "gpt-3.5-turbo"]:
            upvote_data.append(conv)
    print("upvote data size", len(upvote_data))

    with open(output_file, "w") as f:
        json.dump(upvote_data, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, default="clean_mergedvote_conv_20230831.json")
    parser.add_argument("--output-file", type=str, default="upvote.json")
    args = parser.parse_args()

    upvote_data = gen_upvote_data(args.input_file, args.output_file)
