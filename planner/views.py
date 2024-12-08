from django.shortcuts import render
from django.utils.timezone import now
from .models import Note

def index(request):
    selected_date = request.GET.get('date', now().date())
    try:
        selected_date = selected_date if isinstance(selected_date, str) else selected_date.strftime("%Y-%m-%d")
    except Exception:
        selected_date = now().date()
    note, created = Note.objects.get_or_create(date=selected_date)

    if request.method == 'POST':
        content = request.POST.get('content', '')
        note.content = content
        note.save()

    context = {
        'note': note,
        'selected_date': selected_date,
    }
    return render(request, 'planner/index.html', context)