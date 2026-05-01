from django.shortcuts import render

# Create your views here.

def index(request):
    # Define a list of hardcoded topics (our "menu" of data)
    topics = [
        {
            'title': 'How to learn Django fast?',
            'content': "I'm just starting out and wanted to know the best resources to master Django in a few weeks."
        },
        {
            'title': 'The future of web development',
            'content': "With AI on the rise, what do you think the next 5 years look like for junior developers?"
        },
        {
            'title': 'My first Echo post!',
            'content': "Just testing out this cool new platform I'm building. It feels great to see it coming together!"
        },
    ]
    
    # Put the data into a "context" dictionary so the template can see it
    context = {
        'topics': topics
    }
    
    # Send the request, the template path, and the context data to the browser
    return render(request, 'posts/index.html', context)
