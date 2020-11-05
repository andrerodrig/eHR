import io
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa


# class Render:
#     @staticmethod
#     def render(path: str, params: dict, filename: str):
#         template = get_template(path)
#         breakpoint()
#         html = template.render(params)
#         response = io.BytesIO()
#
#         pdf = pisa.pisaDocument(
#             io.BytesIO(html.encode("UTF-8")), response)
#
#         if not pdf.err:
#             response = HttpResponse(
#                 response.getvalue(), content_type='application/pdf')
#             response['Content-Disposition'] = \
#                 'attachment;filename=%s.pdf' % (filename)
#             return response
#         else:
#             return HttpResponse('Error rendering pdf', status=400)


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = \
            'attachment;filename=%s.pdf' % (filename)
        breakpoint()
        pisa_status = pisa.CreatePDF(html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
