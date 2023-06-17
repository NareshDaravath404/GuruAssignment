# wallet/views.py
from django.http import JsonResponse
from django.shortcuts import render
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

    if timer_running:
        return JsonResponse({"message": "Timer is already running."})
    
    timer_running = True

    # Start the timer thread
    threading.Thread(target=run_timer, args=(user_id,)).start()

    return JsonResponse({"message": "Timer started successfully."})

@csrf_exempt
def stop_timer(request):
    global timer_running
    user_id = request.POST.get("user_id")
    user = User.objects.get(id=user_id)

    if not timer_running:
        return JsonResponse({"message": "Timer is not running."})
    
    timer_running = False

    transactions = Transaction.objects.filter(user=user)
    total_coins = sum(transaction.coins for transaction in transactions)
    remaining_coins = user.wallet_balance + total_coins

    return JsonResponse({"remaining_coins": remaining_coins})

def home(request):
    users = User.objects.all()
    transactions=Transaction.objects.all()
    return render(request, 'home.html', {'users': users,'transactions':transactions})
