import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """ Factory for the model CallRecord """

    class Meta:
        model = User

    name = 'Test Name'
    email = 'name@test.com'
