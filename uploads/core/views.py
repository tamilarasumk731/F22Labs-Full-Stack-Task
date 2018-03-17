from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from PIL import Image as im
from PIL import ImageFilter as imf

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fil_type = request.POST['dropdown']
        ph = im.open(myfile)
        if fil_type == 'blur':
            phout = ph.filter(imf.BLUR)
        if fil_type == 'contourr':
            phout = ph.filter(imf.CONTOUR)
        if fil_type == 'detail':
            phout = ph.filter(imf.DETAIL)
        if fil_type == 'edge enhance more':
            phout = ph.filter(imf.EDGE_ENHANCE_MORE)
        if fil_type == 'edge enhance':
            phout = ph.filter(imf.EDGE_ENHANCE)
        if fil_type == 'emboss':
            phout = ph.filter(imf.EMBOSS)
        if fil_type == 'find edges':
            phout = ph.filter(imf.FIND_EDGES)
        if fil_type == 'smooth':
            phout = ph.filter(imf.SMOOTH)
        if fil_type == 'smooth more':
            phout = ph.filter(imf.SMOOTH_MORE)
        if fil_type == 'sharp':
            phout = ph.filter(imf.SHARPEN)
        phout.save("media/filtered/out.jpg")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


'''def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })'''
