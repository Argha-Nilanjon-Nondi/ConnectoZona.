from lib.createaccount import CreateAccount
from lib.login import Login
from lib.validation import  Validation
from lib.friends import Friend
from flask import Flask,request
from flask_mail import Mail, Message
import json
json_data=json.loads(open("data.json","r").read())
app=Flask(__name__)
app.secret_key=json_data["secret"]
app.config['MAIL_SERVER']=json_data["mail-server"]
app.config['MAIL_PORT'] = json_data["mail-port"]
app.config['MAIL_USERNAME'] = json_data["mail-user"]
app.config['MAIL_PASSWORD'] = json_data["mail-password"]
app.config['MAIL_USE_TLS'] =json_data["mail-use-tsl"]
app.config['MAIL_USE_SSL'] =json_data["mail-use-ssl"]
mail = Mail(app)

@app.route("/createacount/step1/",methods=["GET","POST"])
def createaccount_step1():
    if(request.method=="POST"):
        email=""
        password=""
        try:
            email=request.form["email"]
            password=request.form["password"]
        except Exception as error:
            return {"erroText":error,"errorCode":"5003"}
        obj=Validation()
        if(obj.required(email)==False or obj.required(password)==False):
            return {"errorText":"All filed should be filled","errorCode":"5000"}

        if (obj.emailValidate(email) == False):
            return {"errorText": "Email should be validated", "errorCode": "5001"}

        if(obj.passwordValidate(password)==False):
            return {"errorText": "Password should be validated", "errorCode": "5002"}

        if (obj.alreadyAccountExist(email) == True):
            return {"errorText": "User already exist", "errorCode": "5004"}

        obj=CreateAccount()
        obj.email=email
        obj.password=password
        otp_code=obj.create_me()
        msg = Message('Account Verification', sender = 'arghunandi@gmail.com', recipients = [email])
        msg.body = "Your account is successfully created . OTP Code is {0}".format(otp_code["data"]["otp-code"])
        mail.send(msg)
        return {"errorText":"Step 1 finished sucessfully","errorCode":"6000"}

    else:
        return {"errorText":"method is not post","errorCode":"5008"},


@app.route("/createacount/step2/",methods=["GET","POST"])
def createaccount_step2():
    if(request.method=="POST"):
        email=""
        password=""
        otp_code=""
        try:
            email+=request.form["email"]
            password+=request.form["password"]
            otp_code+=request.form["otp_code"]
        except Exception as error:
            return {"erroText":error,"errorCode":"5003"}
        obj=Validation()
        if(obj.required(email)==False or obj.required(password)==False or obj.required(otp_code)==False):
            return {"errorText":"All filed should be filled","errorCode":"5000"}

        if (obj.emailValidate(email) == False):
            print("email is",email)
            return {"errorText": "Email should be validated", "errorCode": "5001"}

        if(obj.passwordValidate(password)==False):
            return {"errorText": "Password should be validated", "errorCode": "5002"}

        if (obj.alreadyAccountExist(email) == True):
            return {"errorText": "User already exist", "errorCode": "5004"}

        obj = CreateAccount()
        obj.email = email
        obj.password = password
        obj.otp_code = otp_code
        return obj.verify_me()

    else:
        return {"errorText":"method is not post","errorCode":"5008"},



@app.route("/login/step1/",methods=["GET","POST"])
def login_step1():
    if(request.method=="POST"):
        email=""
        password=""
        try:
            email+=request.form["email"]
            password+=request.form["password"]
        except Exception as error:
            return {"erroText":error,"errorCode":"5003"}
        obj=Validation()
        if(obj.required(email)==False or obj.required(password)==False):
            return {"errorText":"All filed should be filled","errorCode":"5000"}

        if (obj.emailValidate(email) == False):
            print("email is",email)
            return {"errorText": "Email should be validated", "errorCode": "5001"}

        if(obj.passwordValidate(password)==False):
            return {"errorText": "Password should be validated", "errorCode": "5002"}

        obj = Login()
        obj.email = email
        obj.password = password
        otp_code=obj.step_one()
        msg = Message('Identify Verification', sender=json_data["mail-user"], recipients=[email])
        msg.body = "Your OTP code is here , enter it and login . OTP Code is {0}".format(otp_code["data"]["otp-code"])
        mail.send(msg)
        del otp_code["data"]
        return otp_code

    else:
        return {"errorText":"method is not post","errorCode":"5008"},


@app.route("/login/step2/",methods=["GET","POST"])
def login_step2():
    if(request.method=="POST"):
        email=""
        password=""
        otp_code=""
        try:
            email+=request.form["email"]
            password+=request.form["password"]
            otp_code+=request.form["otp_code"]
        except Exception as error:
            return {"erroText":error,"errorCode":"5003"}
        obj=Validation()
        if(obj.required(email)==False or obj.required(password)==False or obj.required(otp_code)==False):
            return {"errorText":"All filed should be filled","errorCode":"5000"}

        if (obj.emailValidate(email) == False):
            print("email is",email)
            return {"errorText": "Email should be validated", "errorCode": "5001"}

        if(obj.passwordValidate(password)==False):
            return {"errorText": "Password should be validated", "errorCode": "5002"}

        obj = Login()
        obj.email = email
        obj.password = password
        obj.otp_code=otp_code
        return obj.step_two()

    else:
        return {"errorText":"method is not post","errorCode":"5008"},


@app.route("/friend/<api_key>/",methods=["GET","POST","PUT","PATCH"])
def friend(api_key):
    obj=Validation()
    if(obj.ApiKeyExist(api_key)==False):
        return {"errorText":"API key is invalid","errorCode":"5012"}

    dbid=obj.ApiKeyToUserID(api_key=api_key)
    if(request.method=="GET"):
        obj = Friend(user_id=dbid)
        return obj.get_friends()

    if(request.method=="POST"):
        try:
            friend_id=request.form["friend_id"]
        except:
            return {"errorText":"Enter all required parameters","errorCode":"5013"}
        if(obj.UserIdExist(friend_id)==False):
            return {"errorText":"There is no friend with the entered friend_id","errorCode":"5010"}
        print(dbid==friend_id)
        if(friend_id==dbid):
            return {"errorText": "You can not sent friend request to your own account", "errorCode": "5014"}
        obj = Friend(user_id=dbid)
        return obj.request_friend(friend_id=friend_id)

    if(request.method=="PUT"):
        try:
            friend_id=request.form["friend_id"]
        except:
            return {"errorText":"Enter all required parameters","errorCode":"5013"}
        if(obj.UserIdExist(friend_id)==False):
            return {"errorText":"There is no friend with the entered friend_id","errorCode":"5010"}
        if(friend_id==dbid):
            return {"errorText": "You can not sent friend request to your own account", "errorCode": "5014"}
        obj = Friend(user_id=dbid)
        return obj.accept_friend(friend_id=friend_id)

    if(request.method=="PATCH"):
        try:
            friend_id=request.form["friend_id"]
        except:
            return {"errorText":"Enter all required parameters","errorCode":"5013"}
        if(obj.UserIdExist(friend_id)==False):
            return {"errorText":"There is no friend with the entered friend_id","errorCode":"5010"}
        if(friend_id==dbid):
            return {"errorText": "You can not sent friend request to your own account", "errorCode": "5014"}
        obj = Friend(user_id=dbid)
        return obj.delete_friend(friend_id=friend_id)
# @app.route("/friend/requests/<api_key>/",methods=["GET","POST"])
# def friend_requests(api_key):
#     if(request.method=="GET"):
#         obj = Friend(user_id=dbid)
#         return obj.get_friend_requsts()

app.run(debug=True)