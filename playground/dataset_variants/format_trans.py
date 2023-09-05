import argparse
import json


def translate(role):
    if role == "user":
        return "human"
    else:
        return "gpt"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    parser.add_argument("--output-file", type=str, required=True)
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        data = json.load(f)

    models = set()
    for conv in data:
        models.add(conv["model"])
    print(models)

    train_data = []
    for conv in data:
        conversation = []
        for chat in conv["conversation"]:
            conversation.append({"from": translate(chat["role"]), "value": chat["content"]})
        train_data.append({"id": conv["conversation_id"], "conversations": conversation})

    with open(args.output_file, "w") as f:
        json.dump(train_data, f)
