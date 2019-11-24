# issues:

# True/true vs true/false
# null vs None
# double quotation

import json


with open('data_test.json', 'r') as json_file:
    data = json.load(json_file)
    type_error_list = []
    enable_all_issue_list = []
    for each in data['data']:
        each['_id'] = each['_id'][1::2]
        for each_option in each['options']:

            if type(each.get("options")[each_option]) != bool:
                if each['_id'] not in type_error_list:
                    type_error_list.append(each['_id'])
                if each.get("options")[each_option] == 1 or each.get("options")[each_option] == "true":
                    each.get("options")[each_option] = True
                elif each.get("options")[each_option] == 0 or each.get("options")[each_option] == "false":
                    each.get("options")[each_option] = False
            
            print(each.get("options")[each_option]) 

        if each.get("options").get("enable_all_notification"):
            for each_option in each['options']:
                if each.get("options")[each_option] != True:
                    each["options"]["enable_all_notification"] = False
                    enable_all_issue_list.append(each.get('_id'))
                    break
        elif each.get("options").get("enable_all_notification") != True:
            options_all_true = True
            for each_option in each['options']:
                if each_option == "enable_all_notification":
                    continue
                if each.get("options")[each_option] == False:
                    options_all_true = False
                    break
            if options_all_true:
                enable_all_issue_list.append(each.get('_id'))
                each["options"]["eenable_all_notification"] = True


        for each_option in each['options']:
            print(each.get("options")[each_option])

    print("type errors exit in following id")
    for each_id in type_error_list:
        print(each_id)

    print("enable all errors exit in following id")
    for each_id in enable_all_issue_list:
        print(each_id)



print(json.dumps(data, sort_keys=True, indent=4))


# 1. generate an list of _ids, which has inconsistent data:  0 (we want them be stored as boolean)
# 2. correct data by rule:
# if all of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are True  then change "enable_all" to True

# if any one of "enable_cancel_notification", "enable_new_user_notification",           "enable_renewal_notification" are False, then change "enable_all" to False
