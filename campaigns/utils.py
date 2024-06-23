from django.template import Template as DjangoTemplate, Context


def render_text_template(template_string, context):
    template = DjangoTemplate(template_string)
    return template.render(Context(context))

