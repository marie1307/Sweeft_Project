from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Exercise, PersonalPlan, PersonalPlanExercise, PersonalGoal


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
            raise serializers.ValidationError("Invalid username or password.")
        else:
            raise serializers.ValidationError(
                "Must include 'username' and 'password'.")
        
        
class ExerciseSerializer(serializers.Serializer):
    class Meta:
        model = Exercise   
        fields = "__all__" 

    
class PersonalPlanSerializer(serializers.Serializer):
    class Meta:
        model = PersonalPlan   
        fields = "__all__" 


class PersonalPlanExerciseSerializer(serializers.Serializer):
    class Meta:
        model = PersonalPlanExercise
        fields = "__all__"


class PersonalGoalSerializer(serializers.Serializer):
    class Meta:
        model = PersonalGoal
        fields = "__all__"
