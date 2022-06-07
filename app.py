from flask import Flask,request
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse




app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/cht", methods=['POST'])
def bot():
    
    
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    
    
    

    user_msg = request.form.get('Body').lower()

    if 'hello' in user_msg:
        msg.body("Are you a Corn Grower ? \n yes  \n no ")
        
    if "yes" in user_msg:
            msg.body("""Did You Know that Fortenza Duo can secure your plant stand ? 
            \n 1. if  you want to manage early season pests
            \n 2. if  you want to have excellent establishment
            \n 3. if  you want better yields""")
            # msg.body("")
            # msg.body("")
            # msg.body("")

    if '1' in user_msg:
                msg.body("videos1")
                msg.body("Do you want to purchase FD ? \n yes \n no") 

    if '2' in user_msg:
                msg.body("videos2")
                msg.body("Do you want to purchase FD ? \n yes \n no") 

    if '3' in user_msg:
                msg.body("videos3") 
                msg.body("Do you want to purchase FD ? \n yes \n no") 
        
    
    elif 'no' in user_msg:
            msg.body("Do you a Grow any other crop ? ")
            # msg.body("Yes")
            # msg.body("No") 

     
    
            

   


    return str(bot_resp)
    # return user_msg

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
