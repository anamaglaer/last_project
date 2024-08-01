from main.models import Manufacturer, Brand


def get_context_data(request):
    brands = Brand.objects.all()
    manufacturs = Manufacturer.objects.all()
    context = {'brand': brands, 'manufacturer': manufacturs}
    return context

