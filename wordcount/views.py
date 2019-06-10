from django.shortcuts import render

# Create your views here.





def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')



def result(request):
    
  
    words_dictionary = {}
    
    text1 = request.GET['f1']
    text2 = request.GET['f2']
    count = 0    
 

    for word in words_dictionary:
            if(word==text1):
                count+=1

    if(count==0):
        words_dictionary = {text1 : text2}

    return render(request,'result.html', {'word': text1, 'word2':text2, 'dictionary': words_dictionary.items})    


    