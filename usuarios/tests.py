from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from usuarios.models import Profile
from usuarios.decorators import role_required
from django.http import HttpResponse

# Vista simulada protegida por el decorador
@role_required(allowed_roles=['ADMIN'])
def vista_protegida(request):
    return HttpResponse("Acceso permitido")

class UsuariosTests(TestCase):
    def setUp(self):
        # Crea usuario y perfil
        self.admin_user = User.objects.create_user(username='admin1', password='1234')
        Profile.objects.create(user=self.admin_user, role='ADMIN')

        self.doctor_user = User.objects.create_user(username='doctor1', password='abcd')
        Profile.objects.create(user=self.doctor_user, role='DOCTOR')

        self.factory = RequestFactory()

    def test_str_profile(self):
        profile = self.admin_user.profile
        self.assertEqual(str(profile), 'admin1 - ADMIN')

    def test_decorator_acceso_permitido(self):
        request = self.factory.get('/ruta-ficticia/')
        request.user = self.admin_user
        response = vista_protegida(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Acceso permitido")

    def test_decorator_sin_permiso(self):
        request = self.factory.get('/ruta-ficticia/')
        request.user = self.doctor_user
        response = vista_protegida(request)
        self.assertEqual(response.status_code, 403)

    def test_decorator_sin_login(self):
        request = self.factory.get('/ruta-ficticia/')
        request.user = AnonymousUser()
        response = vista_protegida(request)
        self.assertEqual(response.status_code, 403)
