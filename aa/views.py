from django.shortcuts import render,redirect
from django.views import View
import random
from .models import Rooms
from django.http import HttpResponse

def Chatt(request,username1,username2):
    return render(request,'chat2.html',{'username1':username1,'username2':username2})

# Create your views here.




class Find(View):
    def get(self,request,username):



        return render(request,'find.html',{'username':username})
    

    def post(self,request,username):

        rooms=Rooms.objects.all()
        none_rooms=[]


        for i in rooms:
            if i.username2 == 'None':
                none_rooms.append(i.name)
                

        

        
        if not  none_rooms:
            
            room_name= f'{username} +  room '
            rooms=Rooms.objects.all()
            rooms_name=[]
            for i in rooms:
                rooms_name.append(i.name)
            
           
            if room_name in rooms_name:
                
                        
                room=Rooms.objects.get(name=room_name)

                
          
                if room.username2 == 'None':
                    return render(request,'loading.html',{'username':username})
                else:
                    room=Rooms.objects.get(name=room_name)
                    user_2=room.username2
                    room.delete()
                    return redirect('chat',username1=username,username2=user_2)
               
        
            else:
            
                room=Rooms(username1=username,username2='None',name=room_name)

                room.save()
          
                if room.username2 == 'None':
                    return render(request,'loading.html',{'username':username})
            
                else:
                    room=Rooms.objects.get(name=room_name)
                    return HttpResponse(room.username1,room.username2)
        else:
            
            newroom=random.choice(none_rooms)
            
            newroom = Rooms.objects.get(name=newroom)
            if newroom.username1 == username:
                return render(request,'loading.html',{'username':username})









            else:
                newroom.username2 = username
                newroom.save()
                
                username1=newroom.username1

                return redirect('chat',username1=username,username2=username1)
            
          




class DeletRoom(View):
    def get(self,request,username):
        
        room=Rooms.objects.get(username1=username)
        room.delete()
        return redirect('find',username=username)

       

    def post(self,request,username):
        pass