<<<<<<< HEAD
# Python
import uuid

=======
>>>>>>> 984084a2207a36f6070aed74c596a38203909407
# Django
from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.db.models.query import QuerySet
<<<<<<< HEAD
from django.db.models.functions import Lower
from django.views.generic import View
from django.core.files.uploadedfile import InMemoryUploadedFile


# Local
from .models import Game, Genre, Company , AdditionalImage


class MainView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/index.html'
        return render(
            request=request,
            template_name=template_name,
            context={}
        )
    

class GameListView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        template_name: str = 'games/video.html'
        queryset: QuerySet[Game] = Game.objects.all().order_by('-id')
        genres: QuerySet[Genre] = Genre.objects.all()
        return render(
            request=request,
            template_name=template_name,
            context={
                'games': queryset,
                'genres': genres

            }
        )
    
    def post(self, request: HttpRequest) -> HttpResponse:
        data: dict = request.POST
        files: dict = request.FILES

        main_image: InMemoryUploadedFile = None
        additional_images: list = []
        if 'main_imgor' in files:
            main_image = files['main_imgor']
            main_image.name = f'{uuid.uuid1()}.png'

        if 'additional_images' in files:
            for image_file in files.getlist('additional_images'):
                image_file.name = f'{uuid.uuid1()}.png'
                additional_images.append(image_file)

        try:
            company: Company = Company.objects.annotate(
                lower_igor=Lower('name')
            ).get(
                lower_igor=str(data.get('company')).lower()
            )
        except Company.DoesNotExist:
            return HttpResponse(
                f"Компании {data.get('company')} не существует"
            )

        game: Game = Game.objects.create(
            name=data.get('name'),
            price=float(data.get('price')),
            datetime_created=data.get('datetime_created'),
            company=company,
            main_imgor=main_image
        )

        for key in data:
            if 'genre_' in key:
                genre: Genre = Genre.objects.get(
                    id=int(key.strip('genre_'))
                )
                game.genres.add(genre)

        game.save()

        # Сохранение дополнительных изображений
        for image_file in additional_images:
            AdditionalImage.objects.create(game=game, image=image_file)

        return HttpResponse("Игра успешно создана и дополнительные изображения добавлены.")

class GameView(View):

    def get(self, request: HttpRequest, game_id: int) -> HttpResponse:
        try:
            game: Game = Game.objects.get(id=game_id)
        except Game.DoesNotExist as e:
            return HttpResponse(
                f'<h1>Игры с id {game_id} не существует!</h1>'
            )
        
        additional_images: QuerySet[AdditionalImage] = game.additional_images.all()

        return render(
            request=request,
            template_name='games/store-product.html',
            context={
                'igor': game,
                'add_img':additional_images
            }
        )
    
=======

# Local
from .models import Game


def index(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/index.html'
    return render(
        request=request,
        template_name=template_name,
        context={
        }
    )

def games(request: HttpRequest):
    template_name: str = 'games/video.html'
    quriset : QuerySet[Game] =Game.objects.all()
    return render(
        request=request,
        template_name=template_name,
        context={
            'game': quriset
        }
    )


>>>>>>> 984084a2207a36f6070aed74c596a38203909407
def about(request: HttpRequest) -> HttpResponse:
    template_name: str = 'games/about.html'
    return render(
        request=request,
        template_name=template_name,
        context={}
    )

<<<<<<< HEAD
=======
def get_game(request: HttpRequest, game_id: int) -> HttpResponse:
    try:
        game: Game = Game.objects.get(id=game_id)
    except Game.DoesNotExist as e:
        return HttpResponse(
            f'<h1>Игры с id {game_id} не существует!</h1>'
        )
    return HttpResponse(
        f'<h1>ID: {game.name}</h1>'
    )
>>>>>>> 984084a2207a36f6070aed74c596a38203909407
