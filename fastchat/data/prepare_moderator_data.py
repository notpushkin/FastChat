import json
obj = json.load(open("/cpfs/29cd2992fe666f2a/user/mercy/datasets/sharegpt/sharegpt_20230521_2k_clean_lang_split_identity_gpt4.json"))

idx_all = list(range(len(obj)))

import random

sample_idx = random.choices(idx_all, k=3000)

conv_len = []
for conv in obj:
    conv_len.append(len(conv["conversations"]))
print(sum(conv_len)/len(conv_len))

outf = open("../../data/sharegpt_20230521_2k_clean_lang_split_identity_gpt4_sub3k.json", "w")
conv_all = []
for idx in sample_idx:
    conv = obj[idx].copy()
    conv["id"] = "sharegpt-"+conv["id"]
    conv_all.append(conv)
json.dump(conv_all, outf, ensure_ascii=False, indent=2)
outf.close()

data_1 = json.load(open("../../data/sharegpt_20230521_2k_clean_lang_split_identity_gpt4_sub3k.json"))
data_2 = json.load(open("../../data/moderator_train_data.json"))

json.dump(data_1 + data_2, open("../../data/sharegpt_sub3k_moderator_data.json", "w"), indent=2)