from lib.createaccount import CreateAccount,encrypt_text
obj=CreateAccount()
obj.email="pcic095@gmail.com"
obj.password="avunix9143"
obj.otp_code="96527"
print(obj.verify_me())