from django.http import HttpResponse
from .models import Region, District

def index(request):
    html = """
    <html>
    <head>
    </head>
    <body>
    <strong>Welcome to REGION - DISTRICT</strong><br>
    <strong>Option which is you can search: </strong><br>
    <strong>Regions/</strong><br>
    <strong>Districts/</strong><br>
    <strong>Contacts/</strong><br>
    <strong>Regions/ID</strong><br>
    <strong>Regions/Search element</strong><br>
    </body>
    </html>
    """ 

    return HttpResponse(html)

def contacts(request):
    html = """
        <h2>Biz bilan aloqa</h2>
        <strong>Tel: 99-087-45-54</strong><br>
        <strong>email: index@index.com</strong>
    """
    return HttpResponse(html)

def get_regions(request, id=None):
    if id is not None:
        reg = Region.get_by_id(id)
        return HttpResponse(reg.name)
    else:
        html = ""
        for region in Region.objects():
            html += f'<a href={region.id}>{region.name}</a><br>'
        return HttpResponse(html)

def find_by_name(request, text):
    html = ""
    array = text.split('-')
    for region in Region.objects():
        if region.name in array:
            html += f'<a href={region.id}>{region.name}</a><br>'
    return HttpResponse(html)

def get_districts(request, id = None):
    if id is not None:
        dist = District.get_by_id(id)
        return HttpResponse(dist.name)
    else:
        html = ""
        for district in District.objects():
            html += f"<a href = {district.id}> {district.name}</a><br>"
        return HttpResponse(html)

def find_by_name_districts(request, text):
    html = ""
    array = text.split('-')
    for district in District.objects():
        if district.name in array:
            html += f'<a href={district.id}> {district.name}</a><br>'
            return HttpResponse(html)
