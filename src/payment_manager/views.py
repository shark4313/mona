from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from models import PaymentsHistory

@csrf_exempt
def get_month_report(request):
    if request.method == 'GET':
        return render(request, 'reports.html')
    elif request.method == 'POST':
        import datetime
        month = request.POST.get('month', '')
        year = request.POST.get('year', '')
#        return HttpResponse(month)
        if month and year:
            date = datetime.date(int(year), int(month), 18)    
            records = PaymentsHistory.objects.filter(month=date)
            return render_to_response('reports.html', RequestContext(request, {'records':records}))
    