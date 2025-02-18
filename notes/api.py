from rest_framework import serializers
from .models import PersonalNote
from rest_framework import serializers, viewsets

class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):
     # Inner class nested inside PersonalNoteSerializer
    class Meta:
        model = PersonalNote
        fields = ('title', 'content')

     # !!! Broken code still missing the user field

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

class PersonalNoteViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNoteSerializer
    queryset = PersonalNote.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNote.objects.none()
        else:
            return PersonalNote.objects.filter(user=user)