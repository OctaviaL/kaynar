from rest_framework import serializers
from volunteering.models import Volunteer
from volunteering.send_email import send_order_confirmation_code

class VolunteerSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    
    class Meta:
        model = Volunteer
        fields = '__all__'

    def create(self, validated_data):
        pet = validated_data.get('pet')
        volunteer = Volunteer.objects.create(**validated_data)
        send_order_confirmation_code(volunteer.owner.email, volunteer.activation_code, volunteer.product.title, volunteer.total_price)

        return volunteer