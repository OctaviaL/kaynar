from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from volunteering.models import Volunteer
from volunteering.serializers import VolunteerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class VolunteerModelViewSet(ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class VolunteerConfirmAPIView(APIView):
    def get(self, request, code):
        order = get_object_or_404(Volunteer, activation_code=code)

        if not order.is_confirm:
            order.is_confirm = True
            order.save()
            return Response({'message': 'Поздравляю, волонтерство подтверждено!'}, status=status.HTTP_200_OK)
        return Response({'message': 'Волонтерство уже подтверждено!'}, status=status.HTTP_400_BAD_REQUEST)

