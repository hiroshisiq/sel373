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

# try:
#     webpush(
#         subscription_info={"endpoint":"https://fcm.googleapis.com/fcm/send/eCtA_FJQbc4:APA91bFvLf7rTOqTQ6iypIVzMtEt84v5dXWCGA3y1Zkv0KtLs1XNVjlCYh4bgY9CwK-ZhoAUq1b84DypIFKfY5JNzCoHD159JNtpqXQ4sKlfiaqSYo_n05l_O371lqUT6fKMH4fOsq3w","keys":{"p256dh":"BKIZep6GHapeL6zQFPPg1h_KrBSGvDiHkl5T3pmnpKbKC1JV7H4ktKGRHN_NmTjKtk9TtEoHYcYIel-xckiTpD8","auth":"H8yu0wiEYKb3bRT0gZoaBw"}},
#         data="Mary had a little lamb, with a nice mint jelly",
#         vapid_private_key="dK60ppISZEvGacfe20FhUuYGhkt3tP5V5rDz1BhsclU",
#         vapid_claims={"sub": "mailto:anderson.hiroshi.siqueira@usp.br"})
# except WebPushException as ex:
#     print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
#     # Mozilla returns additional information in the body of the response.
#     if ex.response and ex.response.json():
#         extra = ex.response.json()
#         print("Remote service replied with a {}:{}, {}",
#               extra.code,
#               extra.errno,
#               extra.message
#               )
