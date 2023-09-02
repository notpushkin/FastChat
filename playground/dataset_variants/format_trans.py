import argparse
import json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--output-file", type=str, required=True)
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        data = json.load(f)

    train_data = []
    for conv in data:
        conversation = []
        for chat in conv["conversation"]:
            conversation.append({"from": chat["role"], "value": chat["content"]})
        train_data.append({"id": conv["conversation_id"], "conversation": conversation})

    with open(args.output_file, "w") as f:
        json.dump(train_data, f)
