from rest_framework import serializers
from .models import Usuario

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    def save(self):
        nuevo_usuario = Usuario(**self.validated_data)
        nuevo_usuario.set_password(self.validated_data.get('password'))
        nuevo_usuario.save()
        return nuevo_usuario

    class Meta:
        model = Usuario
        exclude = ['groups', 'user_permissions']
        # fields = '__all__'
        extra_kwargs = {
            'id':{'read_only':True},
            'password':{'write_only':True},
        }