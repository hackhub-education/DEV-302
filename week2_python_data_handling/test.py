# issues:

# True/true vs true/false
# null vs None
# double quotation

import json


with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    for each in data['data']:
        each['_id'] = each['_id'][1::2]


print(json.dumps(data, sort_keys=True, indent=4))


# 1. generate an list of _ids, which has inconsistent data:  0 (we want them be stored as boolean)
# 2. correct data by rule:
# if all of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are True  then change "enable_all" to True

# if any one of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are False, then change "enable_all" to False
