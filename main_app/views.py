# todo/views.py
from django.shortcuts import render, redirect
from rest_framework import viewsets, serializers
from .serializers import ProductSerializer, BlogSerializer, UserSerializer
from .models import Product, Blog
from rest_framework.validators import UniqueValidator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# superuser add delete create product/ blog routes


def login_view(request):
    # if post, then authenticate (the user will be submitting a username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data.get('password')
            user = authenticate(username=u, password=p)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/' + u)
                else:
                    print(f"The account for {u} has been disabled.")
            else:
                print('The username and/or password is incorrect.')
        else:
            form = AuthenticationForm()
            # return render(request, 'login.html', {'form': form})
    else:  # get request that sent up empty form
        form = AuthenticationForm()
        # return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/cats')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return HttpResponseRedirect('/user/' + str(user))
        else:
            form = UserCreationForm()
            # return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        # return render(request, 'signup.html', {'form': form})


# def superuser


class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class UserSerializer(serializers.ModelSerializer):
#     fistname = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     lastname = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     username = serializers.CharField(
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(min_length=8)

#     def create(self, validated_data):
#         user = User.objects.create_user(validated_data['username'], validated_data['email'],
#                                         validated_data['password'])
#         return user

#     class Meta:
#         model = User
#         fields = ('id', 'firstname', 'lastname', 'username', 'email', 'password')
