from django.http import JsonResponse
from django.shortcuts import redirect, render
from scripts.forms import UploadScriptForm
from .models import UploadScript, UploadImage
from PIL import Image
import numpy as np
from django.core.files.base import ContentFile
from io import BytesIO
import importlib
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/signin/')
def enter_script(request):
    if request.method == 'POST':
        form = UploadScriptForm(request.POST, request.FILES)
        print(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            # Getting the current instance object to display in the template
            # img_object = form.instance

            return redirect("/thanks/")
        else:
            print("PROBLEM in form")
    return render(request, 'add_script.html', {})


def thanks(request):
    return render(request, 'thanks.html', {"title":"Thank you","Note": "Thank you for contributing to our website!"})


def archive(request):
    return render(request, 'thanks.html', {"title":"Archive","Note": "This page is under progress and meant to be a archive of all the scripts that have been uploaded to the website."})


def home(request):
    return render(request, 'home.html', {})


def documentation(request):
    return render(request, 'documentation.html', {})


def image_filter(request):
    if request.POST:
        img = request.FILES.get('file')
        script_no = int(request.POST.get('script'))
        # print(img.name)
        # print(img.content_type)
        pil_img = Image.open(img)
        cv_img = np.array(pil_img)
        # try:
        script = UploadScript.objects.get(id=script_no)
        try:
            media_import = importlib.import_module(
                f"media.scripts.{str(script.file)[8:-3]}")
            # exec("from media.scripts.img_to_painting import *")
            img = media_import.convert(cv_img)
        except:
            print("Problem in script script_no: ", script_no)
            img = cv_img

        # except:
        #     img = cv_img
        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()
        t = UploadImage()
        t.image = request.FILES.get('image')
        t.converted_image.save("img.png", ContentFile(image_png), save=False)
        t.save()
        return JsonResponse({'converted_image': t.converted_image.url})
    else:
        data = UploadScript.objects.all()
        thumbnails = {}
        for i in data:
            img = i.image
            id = i.id
            name=i.name
            description=i.description
            thumbnails[id] = {"img": img, "name": name, "description": description}
            # thumbnails[name]=name
            # thumbnails[description]=description
    return render(request, 'image_filter.html', {"thumbnails": thumbnails})
