from datetime import datetime
import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

import serial

def show_graph(request,template_name='live_graph.html'):
    return render(request,template_name)


def fetch_sensor_values_ajax(request):
    data={}
    if request.is_ajax():
            COM2 = request.GET.get('id', None)
            sensor_data=[]
            now=datetime.now()
            ok_date=str(now.strftime('%Y-%m-%d %H:%M:%S'))
            try:
                sr=serial.Serial(COM2,9600)
                st=list(str(sr.readline(),'utf-8'))
                sr.close()
                sensor_val=str(''.join(st[:]))
                if(sensor_val):
                    sensor_data.append(str(sensor_val)+','+ok_date)
                else:
                    sensor_data.append(str(sensor_val)+','+ok_date)
            except Exception as e:
                    sensor_data.append(str(sensor_val)+','+ok_date)
            data['result']=sensor_data
    else:
        data['result']='Not Ajax'
    return JsonResponse(data)
