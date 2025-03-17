from django.http import HttpResponse
import os
import getpass
import subprocess
from datetime import datetime
import pytz

def htop_view(request):
    server_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -bn1')

    response = f"""
    <h1>Name: Satyendu Shukla</h1>
    <h2>Username: {getpass.getuser()}</h2>
    <h2>Server Time in IST: {server_time}</h2>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response)
