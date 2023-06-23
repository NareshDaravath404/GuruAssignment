# wallet/views.py
from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Transaction
import threading

# Global variable to store the timer state
timer_running = False

# Function to run the timer thread
def run_timer(user_id):
    global timer_running
    user = User.objects.get(id=user_id)

    while timer_running:
        user.wallet_balance -= 10
        user.save()
        Transaction.objects.create(user=user, coins=10)
        # Sleep for 1 minute
        threading.Event().wait(60)

@csrf_exempt
def start_timer(request):
    global timer_running
    user_id = request.POST.get("user_id")
    user = User.objects.get(id=user_id)

    timer_running = True

    # Start the timer thread
    threading.Thread(target=run_timer, args=(user_id,)).start()

    return JsonResponse({"message": "Timer started successfully."})

@csrf_exempt
def stop_timer(request):
    global timer_running
    user_id = request.POST.get("user_id")
    user = User.objects.get(id=user_id)

    timer_running = False

    transactions = Transaction.objects.filter(user=user)
    remaining_coins = user.wallet_balance

    return JsonResponse({"remaining_coins": remaining_coins})

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        user=User.objects.filter(name=name)
        if user is not None:
            users = user
            transactions=Transaction.objects.all()
            return render(request, 'home.html', {'users': users,'transactions':transactions.reverse})
        else:
            message.error(request,"You are not a active user")

def signin(request):
    return render(request,'userpage.html')

def signup(request):
    return render(request,'signin.html')

def addcoins(request):
    if request.method=="POST":
        name=request.POST['name']
        balance=request.POST['balance']
        myuser=User(name=name,wallet_balance=balance)
        myuser.save()
        return render(request,'userpage.html')




