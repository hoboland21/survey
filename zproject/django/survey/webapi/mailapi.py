from rest_framework import status,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from portal.mail.reports import send_api_report
from django.http import Http404

from configparser import ConfigParser
import json

class MailPost(APIView):

  def post(self, request, format=None):

    if send_api_report(request.data) :
      return Response({"run":"ok"}, status=status.HTTP_201_CREATED)
    else :
      return Response({"error" : "no mail"}, status=status.HTTP_400_BAD_REQUEST)



class SystemConfigView(APIView) :

  def get (self, request,  format=None) :
    config = ConfigParser()
    config.read('static/config/mcsap.conf')
    return Response(config.defaults())
