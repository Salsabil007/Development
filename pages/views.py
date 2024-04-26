from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class FdaProjectView(TemplateView):
    template_name = "proj_fda.html"

# views.py

from django.shortcuts import render
from django.http import HttpResponse

def input_view(request):
    if request.method == 'POST':
        # Get the input value from the form
        input_string = request.POST.get('input_string',[])
        input_string2 = request.POST.get('input_string2',[])
        
        # Process the input_string (e.g., perform some operation on it)
        # For demonstration purposes, let's just return the reversed string
        reversed_string = input_string[::-1]
        reversed_string2 = input_string2[::-1]
        context = {}
        context.update({'reversed_string': reversed_string})
        context.update({'reversed_string2': reversed_string2})
        
        # Render the template with the reversed_string
        return render(request, 'result.html', context)
    
    # If the request method is GET, render the template with an empty string
    return render(request, 'input_form.html')
