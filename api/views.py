from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .operation import *

# Create your views here.
def student_api(request):
    if request.method == 'GET':
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id', None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu=Student.objects.all()
        serializer=StudentSerializer(stu, many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
            
def videofetch(request):
        url = request.GET.get('url',None)
        start_time = request.GET.get('start_time',None)
        end_time = request.GET.get('end_time',None)
        print(url)
        print(start_time)
        print(end_time)
        # transfer_data(url)
        if link_validity(url):
            if time_validation(start_time,end_time):
                main_func(url,start_time,end_time)

                # msg=error_response.m+main.s+" "+title.text 
                if findt.text != "":
                    msg=findt.text
                else:
                    msg=error_response.m+main.s
                # return HttpResponse(msg)
            else:
                msg="Please enter valid time duration"
        else:
            msg="Please open youtube video in current tab"
        # videofetch.msg=msg
        return HttpResponse(msg)            
    


