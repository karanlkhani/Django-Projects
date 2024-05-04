from django.shortcuts import render
import requests

def index(request):
   if request.method == 'POST':
       game_name = request.POST.get("Game_Name")
       api_url = f'http://127.0.0.1:8000/api/game/?name={game_name}'
       response = requests.get(api_url)
       if response.status_code == 200:
           game_data = response.json()
           return render(request, 'results.html', {'games': game_data})
       else:
           return render(request, 'index.html', {'message': 'Failed to fetch game details. Check Again!'})
   
   return render(request, 'index.html')
