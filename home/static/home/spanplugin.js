(function() {
    (function($) {
        return $.widget('IKS.spanplugin', {
            options: {
                uuid: '',
                editable: null
            },
            populateToolbar: function(toolbar) {
                var button, getEnclosingLink, widget;

                widget = this;
                getEnclosingLink = function() {
                    var node;

                    node = widget.options.editable.getSelection().commonAncestorContainer;
                    return $(node).parents('span').get(0);
                };

                button = $('<span class="' + this.widgetName + '"></span>');
                button.hallobutton({
                    uuid: this.options.uuid,
                    editable: this.options.editable,
                    label: 'Span',
                    icon: 'icon-placeholder',
                    command: null,
                    queryState: function(event) {
                        return button.hallobutton('checked', !!getEnclosingLink());
                    }
                });

                toolbar.append(button);
                return button.on('click', function(event) {
                    var enclosingLink, lastSelection, url;

                    enclosingLink = getEnclosingLink();
                    if (enclosingLink) {
                        $(enclosingLink).replaceWith(enclosingLink.innerHTML);
                        button.hallobutton('checked', false);
                        return widget.options.editable.element.trigger('change');
                    } else {
                        lastSelection = widget.options.editable.getSelection();
                        if (lastSelection.collapsed) {
                            url = '/admin/span-form/?prompt_for_text=true';
                        } else {
                            url = '/admin/span-form/?';
                        }

                        return ModalWorkflow({
                            url: url,
                            responses: {
                                spanChosen: function(pageData) {
                                    var span;

                                    span = document.createElement('span');
                                    span.setAttribute('class', pageData.css_class);
                                    if (pageData.id) {
                                        span.setAttribute('data-id', pageData.id);
                                        span.setAttribute('data-linktype', 'page');
                                    }

                                    if ((!lastSelection.collapsed) && lastSelection.canSurroundContents()) {
                                        lastSelection.surroundContents(span);
                                    } else {
                                        span.appendChild(document.createTextNode(pageData.text));
                                        lastSelection.insertNode(span);
                                    }

                                    return widget.options.editable.element.trigger('change');
                                }
                            }
                        });
                    }
                });
            }
        });
    })(jQuery);

}).call(this);