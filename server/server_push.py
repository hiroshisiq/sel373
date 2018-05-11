from pywebpush import webpush, WebPushException
import json

with open("json/data_file.json", "r") as read_file:
    data = json.load(read_file)

for sub in data:
    try:
        webpush(
            subscription_info=sub,
            data="My Sun...is setting...It's dark.....so dark.",
            vapid_private_key="dK60ppISZEvGacfe20FhUuYGhkt3tP5V5rDz1BhsclU",
            vapid_claims={"sub": "mailto:anderson.hiroshi.siqueira@usp.br"})
    except WebPushException as ex:
        print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
        # Mozilla returns additional information in the body of the response.
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}",
                  extra.code,
                  extra.errno,
                  extra.message
                  )
