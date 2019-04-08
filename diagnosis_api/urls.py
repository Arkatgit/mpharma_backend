from django.urls import path , include
from diagnosis_api.views  import ( DiagnosisCategoryViewSet , DiagnosisViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register('diagnosis-category', DiagnosisCategoryViewSet, base_name='diagnosis-category')
router.register('diagnosis', DiagnosisViewSet, base_name='diagnosis')


app_name = 'diagnosis_api'


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += router.urls
