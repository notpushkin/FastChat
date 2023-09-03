import argparse
import json
from tqdm import tqdm
from transformers import AutoTokenizer, PreTrainedTokenizer, PreTrainedTokenizerFast


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", type=str, required=True)
    args = parser.parse_args()

    with open(args.input_file, "r") as f:
        data = json.load(f)

    tokenizer = AutoTokenizer.from_pretrained("huggyllama/llama-7b")

    count = 0
    for conv in tqdm(data):
        for chat in conv["conversations"]:
            sentence = chat["value"]
            input_ids = tokenizer(sentence).input_ids
            count += len(input_ids)

    print("num conversation", len(data))
    print("num token", count)
