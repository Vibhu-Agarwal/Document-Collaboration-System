from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe
import json
from .models import Commits
from django.db import connection
from django.http import HttpResponseRedirect
import datetime
import hashlib

def index(request):
    return render(request, 'docapp/index.html', {})

def main(request, room_name,c_name):
    q=Commits.objects.filter(Docid=room_name).all()
    Document=""
    if q.count()>0:
        q=q[len(q)-1]
        Document=q.Document
    return render(request, 'docapp/edit.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'name_json': mark_safe(json.dumps(c_name)),
        'para': Document
    })
    
def compare(request, room_name,c_name):
    q=Commits.objects.filter(Docid=room_name).all()
    Document=""
    if q.count()>0:
        q=q[len(q)-1]
        Document=q.Document
    return render(request, 'docapp/edit.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'name_json': mark_safe(json.dumps(c_name)),
        'para': Document
    })
    
def history(request, room_name,c_name):
    q=Commits.objects.filter(Docid=room_name).all()
    Document=""
    if q.count()>0:
        q=q[len(q)-1]
        Document=q.Document
    return render(request, 'docapp/edit.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'name_json': mark_safe(json.dumps(c_name)),
        'para': Document
    })
    
def saveit(request):
    if request.method=='POST':
        Docid=request.POST['docid']
        author=request.POST['author']
        Document=request.POST['Document']
        sha = hashlib.sha1(Document.encode())
        sha = sha.hexdigest()
        q=Commits.objects.filter(Docid=Docid).all()
        if q.count()>0:
            q=q[len(q)-1]
            if q.sha!=sha:
                q=Commits(Docid=Docid,author=author,Document=Document,sha=sha)
                q.save()
        else:
            q=Commits(Docid=Docid,author=author,Document=Document,sha=sha)
            q.save()
        string="/doc/"+author+'/'+Docid+"/"
        return HttpResponseRedirect(string)
    else:
        return HttpResponseRedirect("/")