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
    if hasNewSubscription:
        with open("json/data_file.json", "r") as read_file:
            subscriptionList = json.load(read_file)

        seen = set()
        unique = []
        for sub in subscriptionList:
            if sub not in seen:
                unique.append(x)
                seen.add(x)

        with open("json/data_file.json", "w") as write_file:
            json.dump(unique, write_file)

        hasNewSubscription = False
