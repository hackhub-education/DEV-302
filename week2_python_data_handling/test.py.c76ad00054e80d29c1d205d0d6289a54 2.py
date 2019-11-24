# issues:

# True/true vs true/false
# null vs None
# double quotation

import json


# with open('data.json', 'r') as json_file:
#     data = json.load(json_file)
#     for each in data['data']:
#         each['_id'] = each['_id'][1::2]


# print(json.dumps(data, sort_keys=True, indent=4))


# 1. generate an list of _ids, which has inconsistent data:  0 (we want them be stored as boolean)
# 2. correct data by rule:
# if all of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are True  then change "enable_all" to True

# if any one of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are False, then change "enable_all" to False

inconsistentData = []
counter = 0
with open('data1.json', 'r+') as json_file:
    data = json.load(json_file)
    for each in data['data']:
        for option, value in each['options'].items():
            if type(value) != bool:
                inconsistentData.append(each['_id'])

            if value == 0:
                each['options'][option] = False
            elif value == 1:
                each['options'][option] = True
    json_file.seek(0)
    json.dump(data, json_file, indent=4)
    json_file.truncate()


inconsistentDataSet = set(inconsistentData)
print(len(inconsistentDataSet))
# print(data)


# test = {
#     "_id": "58700b1d1b8441a142238eb1",
#            "created_at": "2017-06-12T19:00:26",
#            "created_by": "annie",
#            "modified_at": "2019-10-30T21:00:24",
#            "modified_by": "lixiaojie",
#            "options": {
#                "enable_all_notification": 0,
#                "enable_cancel_notification": 0,
#                "enable_new_user_notification": 0,
#                "enable_renewal_notification": 0
#            }
# }
# print(type(test['options']))
