from lib.createaccount import CreateAccount
from lib.validation import  Validation
from flask import Flask,request
from flask_mail import Mail, Message
app=Flask(__name__)
app.secret_key="73456732475fhvb89iporhfioweq8092346gh";
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'arghunandi@gmail.com'
app.config['MAIL_PASSWORD'] = 'avunix9143'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
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
        msg.body = "Your account is successfully created . OTP Code is {0}".format(otp_code)
        mail.send(msg)
        return {"errorText":"Step 1 finished sucessfully","errorCode":"6000"}

    else:
        return {"error":"method is not post"}


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
        return {"error":"method is not post"}

app.run(debug=True)