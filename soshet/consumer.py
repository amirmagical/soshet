# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        self.user_id= self.scope['url_route']['kwargs']['username1']
        self.group_name= f"chat_{self.user_id}"
        
     
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name

        )
       
        
        await self.accept()

    async def disconnect(self,event):
           await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name

        )
        
      
    async def receive(self, text_data):
        self.user_id= json.loads(text_data)['username']
        self.group_name= f"chat_{self.user_id}"
        
        message = json.loads(text_data)['message']
        username = self.scope['url_route']['kwargs']['username1']
        time=json.loads(text_data)['time']
        await self.channel_layer.group_send(
             self.group_name,{
             'type':'sendmessage',
             'message':message,
             'username':username,
             'time':time,
        })


    
    async def sendmessage(self,event):
        message = event["message"]
        username = event["username"]
        time = event["time"]
        await self.send(text_data=json.dumps({"message": message, "username": username, "time": time}))






