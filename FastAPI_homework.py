from fastapi import FastAPI

app = FastAPI()

##### HOMEWORK #####

## Step one, ask central website for price of chocolate bar using postion in the machine.

@app.get("/price/{postion}")
async def get_price(position):
    return {"price": {position}}

## Step two, get payment card number from reader.

@app.get("/payments/{card_number}")
async def read_card(card_number):
    return {"card number": card_number}

## Step three, tell bank the card number and request authoriation to charge, including a check on fund availibility.

@app.post("/bank_address/{card_number}/{price}")
async def send_card(card_number):
    if card_number in ValidCardNumberList: # checks for valid details
        if price < total: # checks bank balance
            return {"authorisation": TRUE} # accepts payments
    else: 
        return {"authorisation": FALSE} # rejects payments
    
        

## Step four, record details of transaction for future data analysis

@app.put("/transaction_record/{machine_number}")
async def putData():
    temp = {['Date': {DateTime},'Data': {card_number}, 'Price':{price}]}
    return {temp}

## Step five, delete chocolate bar from stock list to allow planned restocking. 

@app.delete("/DeletingData")
async def deletingData():
    return {'Data': {Code}}



#@app.get("/")
#async def root():
#    return {"message": "Hello Emma another word" }

#@app.get("/about")
#async def about():
#    return {'Data': 'about'}#

#@app.post("/sendingData")
#async def sendingData():
#    return {'Data': 'sendingData'}

#@app.put("/putData")
#async def putData():
#    return {'Data': 'Values'}

#@app.delete("/DeletingData")
#async def deletingData():
#    return {'Data': 'Values'}

#@app.get("/items_int/{item_id}")
#async def read_item(item_id: int):
#    if item_id == 42:
 #       return{'That is':'The answer'}
 #   else: 
 #       return {"item_id": item_id}



