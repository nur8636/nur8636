import json

'''
assuming parameter target_key is a list
'''


def remove_json_element(target_key):

    with open("test_payload.json") as f:
        data = json.load(f)

    for i in range(len(target_key)):
        for key in data.keys():
            if target_key[i] == key:
                del data[target_key[i]]
                break
            elif target_key[i] in data[key]:
                del data[key][target_key[i]]
                break
    with open("updated.json", 'w') as wr:
        json.dump(data, wr, indent=2)


# test the function
remove_json_element(['outParams', 'appdate'])
