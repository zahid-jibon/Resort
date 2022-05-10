from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import ( 
    Hero,
    ServiceChart,
    About,
    Services,
    Team,
    Gallery,
    RoomsRates,
    Visitors,
    saveContact,
    saveChecking,
    searchBooking,
    booking,
)

from .forms import BookingForm, SaveContactForm

# Create your views here.
def home(request):
    hero = Hero.objects.filter(is_active=True)
    service_chart = ServiceChart.objects.filter(is_active=True)
    about = About.objects.filter(is_active=True)
    service = Services.objects.filter(is_active=True)
    team = Team.objects.filter(is_active=True)
    gallery = Gallery.objects.filter(is_active=True)
    rooms = RoomsRates.objects.filter(is_active=True)
    visitors = Visitors.objects.filter(is_active=True)

    context = { 'hero': hero, 'service_chart': service_chart, 'about': about, 'service': service, 'team': team, 'gallery': gallery, 'rooms': rooms, 'visitors': visitors }

    return render(request, 'home.html', context)


def checking(request):
    return render(request, 'checking.html')


def contact(request):
    return render(request, 'contact.html')


class SaveContact(generic.FormView):
    template_name = "contact.html"
    form_class = SaveContactForm
    success_url = reverse_lazy('contact')
	
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)


def saveChecking(request):
    if request.method == 'POST':
        roomtype = request.POST.get('roomtype')
        adate = request.POST.get('adate')
        ddate = request.POST.get('ddate')

        checking = saveChecking(roomtype=roomtype, adate=adate, ddate=ddate)
        checking.save()
    

    return render(request, 'checking.html')


def searchBooking(request):
    displaydata = searchBooking.objects.all()
    

    return render(request, 'checking.html', {'data': displaydata})



class BookingForm(generic.FormView):
	template_name = "booking-form.html"
	form_class = BookingForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


