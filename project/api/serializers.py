from api.models import Usuario


from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_active = serializers.BooleanField(
        label="Usuário Ativo",
        help_text="Indica que usuário está ativo."
    )

    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )

    class Meta:
        model = Usuario
        fields = ('username','email', 'password', 'password_confirm', 'is_active', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = Usuario(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            is_active=self.validated_data['is_active'],
            is_superuser=self.validated_data['is_superuser']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta