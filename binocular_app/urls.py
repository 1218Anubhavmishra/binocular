from django.urls import path
from . import views
urlpatterns = [ path("",views.home,name="home"),
                path("aboutus/",views.aboutus,name="aboutus"),
                path("codingexample/",views.codingexample,name="codingexample"),
                path("python_intro/",views.python_intro,name="python_intro"),
                
                path("html_intro/",views.html_intro,name="html_intro"),
                path("html_attributes/",views.html_attributes,name="html_attributes"),
                path("html_head/",views.html_head,name="html_head"),
                path("html_headings/",views.html_headings,name="html_headings"),
                path("html_paragraphs/",views.html_paragraphs,name="html_paragraphs"),
                path("html_comments/",views.html_comments,name="html_comments"),
                path("html_text_formatting/",views.html_text_formatting,name="html_text_formatting"),
                path("html_quotation/",views.html_quotation,name="html_quotation"),
                path("html_links/",views.html_links,name="html_links"),
                path("html_examples/",views.html_examples,name="html_examples"),
              ]