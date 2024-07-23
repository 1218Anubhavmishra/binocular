from django.shortcuts import render
#from .models import
# from django.contrib import messages
# import joblib
# from sklearn.tree import DecisionTreeClassifier


# Create your views here.
def home(request):
     return render(request,'binocular_app/html/home.html')
 
def aboutus(request):
       return render(request,'binocular_app/html/aboutus.html')

def codingexample(request):
       return render(request,'binocular_app/html/codingexample.html')
  
def python_intro(request):
       return render(request,'binocular_app/tutorial_python/python_intro.html')

def html_intro(request):
       return render(request,'binocular_app/tutorial_html/html_intro.html')
def html_attributes(request):
       return render(request,'binocular_app/tutorial_html/html_attributes.html')
def html_head(request):
       return render(request,'binocular_app/tutorial_html/html_head.html')
def html_examples(request):
       return render(request,'binocular_app/tutorial_html/html_examples.html')
def html_headings(request):
       return render(request,'binocular_app/tutorial_html/html_headings.html')
def html_paragraphs(request):
       return render(request,'binocular_app/tutorial_html/html_paragraphs.html')
def html_comments(request):
       return render(request,'binocular_app/tutorial_html/html_comments.html')
def html_text_formatting(request):
       return render(request,'binocular_app/tutorial_html/html_text_formatting.html')
def html_quotation(request):
       return render(request,'binocular_app/tutorial_html/html_quotation.html')
def html_links(request):
       return render(request,'binocular_app/tutorial_html/html_links.html')
