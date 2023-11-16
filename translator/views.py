from django.shortcuts import render
from . import translate

# Create your views here.


def translator_view(request):
    if request.method == 'POST':
        source_language = request.POST.get('s_lang')
        target_language = request.POST.get('t_lang')
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text, source_language,
                                     target_language)
        return render(
            request, 'translator.html', {
                'output_text': output,
                'original_text': original_text,
                's_lang': source_language,
                't_lang': target_language,
            })
    else:
        return render(request, 'translator.html')
