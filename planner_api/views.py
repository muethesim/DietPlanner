from django.http import JsonResponse
from . import gpt

def get_diet(request):
    age = request.GET.get("age")
    height = request.GET.get("height")
    weight = request.GET.get("weight")
    days = request.GET.get("days")
    prompt = f'''
Consider the following circumstances and generate a healthy diet plan
age:${age},
height:${height},
weight:${weight} for a total of ${days} days.
Keep it short and upto point.
No tip or others needed. Just diet plans.
'''
    
    responce = gpt.get_responce(prompt)
    responce_data = responce.choices[0].message.content

    data = {
        'result' : responce_data
    }
    return JsonResponse(data)
