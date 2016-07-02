from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import Cards
from django.contrib.auth.decorators import login_required
from apps.comments.forms import CommentsForm
from apps.comments.models import Comments
from apps.likes.models import Likes

from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def home(request):
    """Display all cards."""
    context = {}
    all_cards = Cards.objects.all()
    paginator = Paginator(all_cards, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        cards = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cards = paginator.page(paginator.num_pages)

    context = {'cards': cards}
    template = 'home.html'
    return render(request, template, context)


def private_cards(request):
    """Display all cards."""
    context = {}
    if request.user.is_authenticated():
        private_cards = Cards.objects.filter(user=request.user, private=True)
    else:
        private_cards = None

    paginator = Paginator(private_cards, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        cards = paginator.page(page)
    except(EmptyPage, InvalidPage):
        cards = paginator.page(paginator.num_pages)

    context = {'cards': cards}
    template = 'private_cards.html'
    return render(request, template, context)


def view_card(request, card_id):
    """Display specific card."""
    context = {}
    card_info = Cards.objects.get(id=card_id)
    if card_info.private is False:
        card = card_info
        try:
            likes = Likes.objects.get(card=card)
        except:
            likes = None
        form = CommentsForm()
        comments = Comments.objects.filter(cards=card)
        context = {'card': card, 'comments': comments, 'form': form, 'likes': likes}
        template = 'view_card.html'
        context.update(csrf(request))
        return render(request, template, context)
    else:
        if request.user.is_authenticated():
            if card_info.user == request.user:
                card = card_info
                try:
                    likes = Likes.objects.get(card=card)
                except:
                    likes = None
                form = CommentsForm()
                comments = Comments.objects.filter(cards=card)
                context = {'card': card, 'comments': comments, 'form': form, 'likes': likes}
                template = 'view_card.html'
                context.update(csrf(request))
                return render(request, template, context)
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')


def search(request):
    context = {}
    search_list = []
    if request.method == 'POST':
        try:
            searchtext = request.POST.get('searchText')

            cards = Cards.objects.filter(card_title__icontains=searchtext)
            search_list = cards
            # for card in cards:
            #     if card.card_title == searchtext:
            #         search_list.append(card)

            context = {'search_list': search_list}
            context.update(csrf(request))
            template = "search.html"
            return render(request, template, context)
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    return HttpResponseRedirect('/')


@login_required(login_url='/users/login/')
def create_card(request):
    """Creating new cards."""
    context = {}
    if request.method == 'POST':
        try:
            card_title = request.POST.get('card_title')
            card_description = request.POST.get('card_description')
            card_picture = request.FILES.get('card_picture')
            if request.POST.get('private') == 'on':
                card_private = True
            else:
                card_private = False
            try:
                created_by = request.user
            except:
                created_by = None

            if created_by is not None:
                card_info = Cards(
                    card_title=card_title,
                    user=created_by,
                    card_description=card_description,
                    card_hero_image=card_picture,
                    private=card_private)
            else:
                card_info = Cards(
                    card_title=card_title,
                    card_description=card_description,
                    card_hero_image=card_picture,
                    private=card_private)

            card_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    template = "create_card.html"
    return render(request, template, context)
