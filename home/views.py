from django import forms

from wagtail.wagtailadmin.modal_workflow import render_modal_workflow

SPAN_CSS_CLASS_OPTIONS = (
    ('highlight-red', 'Red Highlight'),
    ('highlight-yellow', 'Yellow Highlight'),
    ('highlight-gray', 'Gray Highlight'),
)


class SpanForm(forms.Form):
    text = forms.CharField()
    css_class = forms.ChoiceField(choices=SPAN_CSS_CLASS_OPTIONS)


class ShortSpanForm(forms.Form):
    css_class = forms.ChoiceField(choices=SPAN_CSS_CLASS_OPTIONS)


def span_form(request):
    prompt_for_text = bool(request.GET.get('prompt_for_text'))

    if prompt_for_text:
        form_class = SpanForm
    else:
        form_class = ShortSpanForm

    if request.POST:
        form = form_class(request.POST)
        if form.is_valid():
            return render_modal_workflow(
                request,
                None, 'home/span_form_chosen.js',
                {
                    'css_class': form.cleaned_data['css_class'],
                    'text': form.cleaned_data['text'] if prompt_for_text else form.cleaned_data['css_class']
                }
            )
    else:
        form = form_class()

    return render_modal_workflow(
        request,
        'home/span_form.html', 'home/span_form.js',
        {'form': form,}
    )