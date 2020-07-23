from django.contrib import auth, messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from .forms import UserForm, EditProfileForm, UpdatePasswordForm
from .models import AbstractUser, User


# Create your views here.

# Create your views here.
def index(request):
    if request.session._session:
        uid = request.user.id
        # kid = uid - 1
        mydata = User.objects.filter(id=uid)
        dbdata = {'mydata': mydata}
        return render(request, "accounts/index.html", dbdata)
    else:
        return render(request, "accounts/index.html")


def user_register(request):
    return render(request, "accounts/register.html")


def join(request):
    # context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            # user.save()
            # profile = profile_form.save(commit=False)
            # profile.user = user
            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']
            user.save()
            registered = True
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                    )
            auth_login(request, new_user)
            return HttpResponseRedirect('/accounts/userhome/')
        else:
            return HttpResponse(user_form.errors)

        # The request is not a HTTP POST and already logined, so display the  Header menu with User details.
    elif request.session._session:
        uid = request.user.id
        # kid = uid - 1
        mydata = User.objects.filter(id=uid)
        dbdata = {'mydata': mydata}
        return render(request, 'accounts/login.html', dbdata)

    # The request is not a HTTP POST and Not Logged in so display the Signup Form
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()
        mydata = {'user_form': user_form, 'registered': registered}
        return render(request, 'accounts/join.html', mydata)


def login(request):
    # context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                auth_login(request, user)
                request.session["name"] = request.user.id
                return redirect('/accounts/userhome/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your PMPro account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST and already logined, so display the  Header menu with User details.
    elif request.session._session:
        uid = request.user.id
        mydata = User.objects.filter(id=uid)
        dbdata = {'mydata': mydata}
        return render(request, 'accounts/login.html', dbdata)

    # The request is not a HTTP POST, so display the login form.
    else:
        return render(request, 'accounts/login.html')


@login_required
def userhome(request):
    uid = request.user.id
    # kid = uid - 1
    mydata = User.objects.filter(id=uid)
    dbdata = {'mydata': mydata}
    return render(request, "accounts/user_home.html", dbdata)


def reg_users(request):
    users = User.objects.all()
    mydata = {'users': users}
    return render(request, 'accounts/users.html', mydata)


def profile(request):
    return HttpResponse("User Registration Successfull.")


@login_required
def update_user(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = request.user
            user.save()  # Save the Updated User Details
            return redirect('/accounts/profile_updated/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {}
        # args.update(csrf(request))
        uid = request.user.id
        mydata = User.objects.filter(id=uid)
        args['form'] = form
        args['mydata'] = mydata
        return render(request, 'accounts/update_user.html', args)


@login_required
def update_password(request):
        if request.method == 'POST':
            form = UpdatePasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/accounts/profile_updated/')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = UpdatePasswordForm(request.user)
        return render(request, 'accounts/update_password.html', {'form': form})


def profile_updated(request):
    messages.info(request, 'Your Profile has been Updated successfully!')
    return HttpResponseRedirect('/accounts/userhome/')


def logout(request):
    auth.logout(request)
    return redirect('/accounts/')
