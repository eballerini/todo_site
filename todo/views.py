from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import JsonResponse, HttpResponse, Http404
from django.template import loader
from .models import AccessToken, Item

@login_required
def index(request):
    latest_item_list = Item.objects.filter(owner=request.user).order_by('-due_date')
    template = loader.get_template('todo/index.html')
    context = {
        'latest_item_list': latest_item_list,
    }
    return HttpResponse(template.render(context, request))
    
@login_required
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'todo/detail.html', {'item': item})
    # return HttpResponse("You're looking at item %s." % item_id)
    
@login_required
def add(request):
    if request.method == 'POST':
        description = request.POST['description']
        due_date_input = request.POST['due_date']
        if due_date_input.strip() == '':
            due_date = None
        else:
            due_date = due_date_input
        item = Item(description=description, due_date=due_date, owner=request.user)
        item.save()
        return redirect('todo:index')
    
    return render(request, 'todo/add.html', {})
    
# must check accessToken and retrieve user based on that (is there a way to retrieve the user in the lambda's session?)
# load items based on that user
# return json
def get_items_list(request):
    access_token = request.GET.get('access_token')
    if not access_token:
        raise Http404
        
    # TODO check for expiry date
    access_token = get_object_or_404(AccessToken, token=access_token)
    latest_item_list = Item.objects.filter(owner=access_token.user).order_by('-due_date')
    
    data = {}
    items = []
    for item in latest_item_list:
        items.append(item.to_json())
    
    data['items'] = items
    
    return JsonResponse(data)
