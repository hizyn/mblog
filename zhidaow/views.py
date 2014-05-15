from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from zhidaow.models import Post, Author, Column, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
pagenum = 2

def index(request):
	post_list = get_list_or_404(Post.objects.order_by('-date'), status=True)
	paginator = Paginator(post_list, pagenum)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request, 'zhidaow/index.html', {'posts': posts})

def post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.visits += 1
	post.save()
	return render(request, 'zhidaow/post.html', {'post': post})

def author(request, pk):
	author = get_object_or_404(Author, pk=pk)
	posts_list = get_list_or_404(Post.objects.order_by('-date'), status=True, author=author)
	paginator = Paginator(posts_list, pagenum)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'zhidaow/author_list.html', {'author': author, 'posts': posts})

def tag(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	posts_list = get_list_or_404(Post.objects.order_by('-date'), status=True, tag=tag)
	paginator = Paginator(posts_list, pagenum)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'zhidaow/tag_list.html', {'tag': tag, 'posts': posts})

def column(request, pk):
	column = get_object_or_404(Column, pk=pk)
	posts_list = get_list_or_404(Post.objects.order_by('-date'), status=True, column=column)
	paginator = Paginator(posts_list, pagenum)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request, 'zhidaow/column_list.html', {'column': column, 'posts': posts})

