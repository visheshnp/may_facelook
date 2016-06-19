from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.core.context_processors import csrf
from .models import Cards
from django.contrib.auth.decorators import login_required
from apps.comments.forms import CommentsForm
from apps.comments.models import Comments
from apps.likes.models import Likes
# Create your views here.


def home(request):
    """Display all cards."""
    context = {}
    cards = Cards.objects.all()
    public_cards = Cards.objects.filter(private=False)
    if request.user.is_authenticated():
        private_cards = Cards.objects.filter(user=request.user, private=True)
    else:
        private_cards = None
    context = {'cards': cards, 'public_cards': public_cards, 'private_cards': private_cards}
    template = 'home.html'
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
