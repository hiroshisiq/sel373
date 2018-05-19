import json

hasNewSubscription = False

# Append subscription to list of subscribers
def appendSubscription(subscriptionJson):
    with open("json/data_file.json", "r") as read_file:
        subscriptionList = json.load(read_file)

    subscriptionList.append(subscriptionJson)

    with open("json/data_file.json", "w") as write_file:
        json.dump(subscriptionList, write_file)

    hasNewSubscription = True
    return

# Remove duplicates from list
def removeDuplicate():
    if True:
        with open("json/data_file.json", "r") as read_file:
            subscriptionList = json.load(read_file)

        L = subscriptionList
        subscriptionList = list({v['endpoint']:v for v in L}.values())

        with open("json/data_file.json", "w") as write_file:
            json.dump(subscriptionList, write_file)

        hasNewSubscription = False
