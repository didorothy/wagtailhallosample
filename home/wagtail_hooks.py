from django.conf import settings
from django.conf.urls import url
from django.utils.html import format_html, format_html_join, mark_safe

from wagtail.wagtailcore import hooks

from . import views


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'home/spanplugin.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes + format_html(
      """
      <script>
        registerHalloPlugin('spanplugin');
      </script>
      """
    )

@hooks.register('insert_editor_css')
def editor_css():
    return mark_safe(
    '''
    <style>
    .highlight-red { background: red; color: white; }
    .highlight-yellow { background: yellow; color: black; }
    .highlight-red { background: gray; color: red; }
    </style>
    ''')

@hooks.register('register_admin_urls')
def urlconf_time():
    return [
        url(r'^span-form/$', views.span_form, name='wagtailadmin_span_form'),
    ]