# -*- coding: utf-8 -*-

"""Views for the application/"""

from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.

def upload_file(request):
    """Upload a File"""
    if request.method =='POST':
        file_data1 = request.data['file'].read().decode("utf-8")
        file_data2 = request.data['file'].read().decode("utf-8")
    elif request.method == 'GET':
        return HttpResponse("""
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="UTF-8">
                <title>Title of the document</title>
              </head>
              <body>
                <form method="post" enctype="multipart/form-data">
                    <input type="file" name="file">
                    <button type="submit">Upload</button>
                </form>
              </body>
            </html> 
        """)    

    return HttpResponse("Hello world!")