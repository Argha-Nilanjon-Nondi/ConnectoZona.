from hashlib import sha256
import random
def generate_random(num=100000):
    randstr=str(random.randrange(num))
    return randstr

def encrypt_text(text):
    return sha256(text.encode("utf-8")).hexdigest()

status_code=[

{"errorText":"All filed should be filled","errorCode":"5000"},
{"errorText": "Email should be validated", "errorCode": "5001"},
{"errorText": "Password should be validated", "errorCode": "5002"},
{"errorText":"Internal error","errorCode":"5003"},
{"errorText": "User already exist", "errorCode": "5004"},
{"errorText":"Email,Password or OTP code is not valid","errorCode":"5005"},
{"errorText": "OTP code is expired", "errorCode": "5006"},
{"errorText":"Email or password is incorrect","errorCode":"5007"},
{"errorText":"method is not post","errorCode":"5008"},
{"errorText":"Friend request is already placed","errorCode":"5009"},
{"errorText":"There is no friend with the entered friend_id","errorCode":"5010"},
{"errorText":"Already you are friends","errorCode":"5011"},
{"errorText":"API key is invalid","errorCode":"5012"},
{"errorText":"Enter all required parameters","errorCode":"5013"},
{"errorText":"You can not sent friend request to your own account","errorCode":"5014"},
{"errorText":"Step 1 finished sucessfully","errorCode":"6000"},
{"errorText": "Account verified", "errorCode": "6001"},
{"errorText": "Login sucessfully", "errorCode": "6002"},
{"errorText":"Friend list is here","errorCode":"6003"},
{"errorText":"Friend requests is successfully placed","errorCode":"6004"},
{"errorText":"Friend is successfully added","errorCode":"6005"},
{"errorText":"Friend is successfully unfriended","errorCode":"6006"},
    {"errorCode":"6007","errorText":"Request friend list is here"}
]

