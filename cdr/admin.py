from django.contrib import admin

# Register your models here.
from django.contrib import admin


# Register your models here.


#EJEMPLOSSSSSSSSSS......
from django.http import HttpResponse,JsonResponse
from cdr.models import *
from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

import csv


admin.site.disable_action('delete_selected')




@admin.register(Cdr)
class CdrAdmin(admin.ModelAdmin):

	list_display = ('calldate','billsec','disposition','accountcode')
	search_fields =('calldate',)
	list_filter =('disposition','accountcode')
	actions = ['Genera_CSV',]



	def Genera_CSV(self, request,queryset):



		my_filter={}


		for a in request.GET:

			if a == 'disposition':

				my_filter['disposition']=request.GET['disposition']
			
			if a=='accountcode':

				my_filter['accountcode']=request.GET['accountcode']
			
			if a=='drf__calldate__gte':



				my_filter['calldate__gte']=request.GET['drf__calldate__gte']

			if a=='drf__calldate__lte':

				my_filter['calldate__lte']=request.GET['drf__calldate__lte']


		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Reporte.csv'

		writer = csv.writer(response)

		writer.writerow(['Calldate','Billsec','Disposition','Accountcode'])

		_cdr=Cdr.objects.filter(**my_filter)

		for q in _cdr:

			writer.writerow([q.calldate,q.billsec ,q.disposition,q.accountcode])

		return response


