#!/usr/bin/env python
import ast

def data_augmentation(saved_file="label_honglou.txt"):
    speakers = []
    contexts = []
    combined_res = [] 
    # combine N speakers with M contexts to get N*M examples
    with open(saved_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            res = ast.literal_eval(line)
            speakers.append(res['speaker'])
            ctx = res['context']
            ctx_left = ctx[:res["istart"]]
            ctx_right = ctx[res["iend"]:]
            contexts.append([ctx_left, ctx_right, res["istart"]])
            
    uid = 0   
    len_truncate = 128
    for speaker in speakers:
        for ctx in contexts:
            try:
                new_ctx = ctx[0] + speaker + ctx[1]
                istart = ctx[2]
                new_iend = istart + len(speaker)
                new_speaker = speaker
                # truncate the input if the speaker is contained in the last 128 words
                if len(new_ctx) > len_truncate and (len(new_ctx)-istart)<len_truncate:
                    truncated_ctx = new_ctx[-len_truncate:]
                    istart = ctx[2] - (len(new_ctx) - len_truncate)
                    new_iend = istart + len(speaker)
                    new_speaker = truncated_ctx[istart:new_iend]
                res = {'uid':uid, 
                   'context':new_ctx,
                   'speaker':new_speaker,
                   'istart':istart, 
                   'iend':new_iend}
                combined_res.append(res)
                uid = uid + 1
            except:
                continue
    return combined_res

speakers = data_augmentation()
