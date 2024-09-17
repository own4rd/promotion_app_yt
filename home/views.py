from django.shortcuts import render

promotions = [
    {
        'title': 'Join us for our grand opening',
        'content': 'Come join us for our grand opening on Saturday, July 1st!',
        'link': 'grand_opening'
    },
    {
        'title': 'Now offering free wifi',
        'content': 'We now have free wifi available for all of our customers.',
        'link': 'free_wifi'
    },
    {
        'title': 'Now open on Sundays',
        'content': 'We are now open on Sundays from 10am to 4pm.',
        'link': 'open_sundays'
    }
]

def home_view(request):
    return render(request, 'home/index.html', {
        'promotions': promotions
    })
