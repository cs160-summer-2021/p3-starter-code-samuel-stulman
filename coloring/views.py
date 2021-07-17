from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def demo(request):
    return render(request, 'coloring/demo.html')

def new_interaction(request):
    return render(request, 'coloring/new_interaction.html')

def gallery(request):
    return render(request, 'coloring/gallery.html')

def template(request):
    return render(request, 'coloring/template.html')
    
def drawing(request):
    return render(request, 'coloring/drawing.html')

def pony_template(request):
    return render(request, 'coloring/pony_template.html')