from django.shortcuts import render
from comenapp.models import *
from comenapp.forms import *
from django.contrib.auth.models import User

# Create your views here.

def form_comen(request):
    comen = Coments.objects.all()

    if request.method == "POST":

        fcomen = ComentForm(request.POST)

        if fcomen.is_valid():
            
            coment = fcomen.save(commit=False)
            coment.remitente = request.user 
            coment.save()
            

        return render(request, "comenapp/comen_list.html")
            
    else:

        fcomen = ComentForm()
        
    return render(request, "comenapp/comen_list.html", {"form_comentarios": fcomen, "list_comentarios":comen})

# def add_comment_to_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm()
#     return render(request, 'blog/add_comment_to_post.html', {'form': form})