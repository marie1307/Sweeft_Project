from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer, LoginSerializer, ExerciseSerializer, PersonalPlanExercise, PersonalPlanExerciseSerializer, PersonalGoalSerializer, CompletedWorkoutSerializer, ExerciseFeedbackSerializer, WorkoutSessionSerializer
from .models import Exercise, PersonalPlan, PersonalPlanExercise, PersonalGoal, CompletedWorkout, ExerciseFeedback, WorkoutSession
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

# Exercises list public
class ExercisesViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user and not user.is_anonymous:
            queryset = queryset.filter(user=user)
        return queryset


# General personal plan only for authenticated user
class PersonalPlanViewSet(viewsets.ModelViewSet):
    queryset = PersonalPlan.objects.all()
    serializer_class = PersonalPlanExercise
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user and not user.is_anonymous:
            queryset = queryset.filter(user=user)
        return queryset


# Personal plan per exercises only for authenticated user
class PersonalPlanExerciseViewSet(viewsets.ModelViewSet):
    queryset = PersonalPlanExercise.objects.all()
    serializer_class = PersonalPlanExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user and not user.is_anonymous:
            queryset = queryset.filter(user=user)
        return queryset


# Personal goals track only for authenticated user
class PersonalGoalViewSet(viewsets.ModelViewSet):
    queryset = PersonalGoal.objects.all()
    serializer_class = PersonalGoalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user and not user.is_anonymous:
            queryset = queryset.filter(user=user)
        return queryset
    

# Complete workout allowed only for authenticated user
class CompletedWorkoutViewSet(viewsets.ModelViewSet):
    queryset = CompletedWorkout.objects.all()
    serializer_class = CompletedWorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CompletedWorkout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Exercise Feedback allowed only for authenticated user
class ExerciseFeedbackViewSet(viewsets.ModelViewSet):
    queryset = ExerciseFeedback.objects.all()
    serializer_class = ExerciseFeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExerciseFeedback.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Workout session information allowed only for authenticated user
class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutSession.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
