# this file created by Bhagyashri

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def analise(request):
    djtext = request.POST.get('text','default')
    print(djtext)
    rempunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fulcaps','off')
    lowercase= request.POST.get('lowercase','off')
    newlinerem= request.POST.get('newlinerem','off')
    spacerem= request.POST.get('spacerem','off')
    charcount= request.POST.get('charcount','off')

    punctuation='''~!@#$%^&*()_+<>?,./:";'|'''
    if(rempunc=='on'):
        analysed=""
        for char in djtext:
            if char not in punctuation:
                analysed = analysed+char
        params={'purpose':'Punctuations removed','modified_text':analysed}

        djtext=analysed

    if(fullcaps=='on'):

        analysed=str.upper(djtext)
        params = {'purpose': 'Text in Uppercasse', 'modified_text': analysed}
        djtext=analysed


    if(lowercase=='on'):

        analysed=str.lower(djtext)
        params = {'purpose': 'Text in Lowercase', 'modified_text': analysed}

        djtext=analysed

    if(newlinerem=='on'):
        analysed=""
        for char in djtext:
            if char !='\n'and char!='\r':
                analysed= analysed + char
        params = {'purpose': 'all new lines are removed ', 'modified_text': analysed}
        djtext=analysed

    if(spacerem=='on'):
        analysed=""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" "and djtext[index+1]==" "):
                analysed=analysed+char
        params = {'purpose': 'all new lines are removed ', 'modified_text':analysed}
        djtext=analysed

    if (charcount == 'on'):

        djtext = djtext.replace(' ', '')
        analysed = len(djtext)
        params = {'purpose': 'Text in Lowercase', 'modified_text':analysed}
        djtext=analysed
    if (rempunc !="on" and fullcaps !="on" and  lowercase!="on" and newlinerem!="on" and spacerem!="on" and charcount != "on"):
       return HttpResponse("<h3>Please select any operation and try again</h3>")

    return render(request, 'analise.html', params)