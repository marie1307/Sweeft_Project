from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExercisesViewSet, PersonalPlanViewSet, PersonalPlanExerciseViewSet, PersonalGoalViewSet


router = DefaultRouter()
router.register(r'exercises', ExercisesViewSet, basename='exercises')
router.register(r'personal_plan', PersonalPlanViewSet, basename='personal_plan')
router.register(r'personal_plan_exercises', PersonalPlanExerciseViewSet, basename='personal_plan_exercises')
router.register(r'persona_goal', PersonalGoalViewSet, basename='persona_goal')

urlpatterns = [
    path('', include(router.urls)),
]
