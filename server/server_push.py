from pywebpush import webpush, WebPushException

try:
    webpush(
        subscription_info={"endpoint":"https://fcm.googleapis.com/fcm/send/e_x1jiLlCoM:APA91bENBX5ySQ_eTB6N--xUv8CbYgi4ZJcUo-9-A72h99yQTxvxmqSIF319lVIA2NYwLhSpRQzKEVyWSmiI02Hglpa0CR4Zmbpo8hzzPsZaQIdRCnCO7z77Q0WXEdzkWBEi7IRAR7hX","keys":{"p256dh":"BCJyLdht8oQeuPmd_7C_VnnoPgcmqip-Grnrr65I3bZxu73wLcR6hbz1ZfjHpv5I78opDlukXY7sXnmw_9hpUhs","auth":"j9fePyA7FWfetxu6TIcGEw"}},
        data="Mary had a little lamb, with a nice mint jelly",
        vapid_private_key="pushkeys/private.key")
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
