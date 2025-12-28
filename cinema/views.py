from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Session, Ticket


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movies': movies})


def session_list(request, movie_id):
    sessions = Session.objects.filter(movie_id=movie_id)
    return render(request, 'cinema/session_list.html', {'sessions': sessions})


def buy_ticket(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    taken_seats = Ticket.objects.filter(session=session).values_list(
        'seat_number', flat=True
    )

    if request.method == 'POST':
        seat = int(request.POST.get('seat'))

        if seat in taken_seats:
            return render(
                request,
                'cinema/buy_ticket.html',
                {
                    'session': session,
                    'taken_seats': taken_seats,
                    'error': 'Это место уже занято'
                }
            )

        Ticket.objects.create(session=session, seat_number=seat)
        return redirect('success')

    return render(
        request,
        'cinema/buy_ticket.html',
        {
            'session': session,
            'taken_seats': taken_seats
        }
    )

def success(request):
    return render(request, 'cinema/success.html')
