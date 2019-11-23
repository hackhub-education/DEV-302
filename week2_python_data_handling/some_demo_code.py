d = []

import json


with open('./data.json', 'r') as json_file:
    d = json.load(json_file)['data']

def getAll():

    acq_list = list()
    for acq in d:
        if acq['options']:
            # get all
            if type(acq['options']['enable_all_notification']) == bool:
                acq_list.append({'id': acq['_id'], 'created_by': acq['created_by'],
                                'modified_at': acq['modified_at'], 'modified_by': acq['modified_by']})
    return acq_list


def getAllWithUsersAndDate():
    ''''with user and dates constrain'''
    ignoreUsers = ['a list of person']
    timeStarted = '2019-09-09'

    acq_list = list()
    for acq in d:
        if acq['options']:
            # #if created by ignoreUsers, then ignore
            # if acq['created_by'] in ignoreUsers:
            #     continue

            # add time constrains
            # if acq['modified_at'] <= timeStarted:
            #     continue
            # get all
            if type(acq['options'].get('enable_all_notification')) == bool or \
               type(acq['options'].get('enable_cancel_notification')) == bool or\
                type(acq['options'].get('enable_renewal_notification')) == bool or\
                type(acq['options'].get('enable_new_user_notification')) == bool:

                acq_list.append({'id': acq['_id'], 'created_by': acq['created_by'], 'modified_at': acq['modified_at'],
                                'modified_by': acq['modified_by'], 'created_at': acq['created_at']})
    return acq_list


def getAllUserInvolved(acq_list):
    user_set=set()
    for acq in acq_list:
        user_set.add(acq['modified_by'])
    return user_set

# print(len(acq_list))

acq_list=getAllWithUsersAndDate()
# unique_user_list = getAllUserInvolved(acq_list)
# print(unique_user_list)
print(len(acq_list))

unique_user_list = getAllUserInvolved(acq_list)
print(unique_user_list)

# sorted by created by
acq_list.sort(key=lambda x: x['modified_by'], reverse=True)
# #print the list
# for acq in acq_list:
#     print(f"{acq['name']},{acq['modified_at'][:10]},{acq['modified_by']},{acq['created_at'][:10]},{acq['created_by']}")
