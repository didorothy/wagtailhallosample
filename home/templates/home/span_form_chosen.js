function(modal) {
    modal.respond('spanChosen', {
        'css_class': '{{ css_class }}',
        'text': '{{ text|escapejs }}'
    });
    modal.close();
}