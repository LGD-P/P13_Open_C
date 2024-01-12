.. _programming_interface:

=======================
Classes et Vues Django:
=======================

-------------
PROFILES APP: 
-------------

Profiles Class :
----------------

.. code-block:: python

    class Profile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

.. autoclass:: profiles.models.Profile
    :members:

Profiles View :
---------------

**The index view :**

.. code-block:: python

    def index(request):
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)


.. autofunction:: profiles.views.index
    

**The profile view :**

.. code-block:: python

    def profile(request, username):
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)

.. autofunction:: profiles.views.Profile
    
====================================================

-------------
LETTINGS APP: 
-------------

Address Class :
----------------

.. code-block:: python
    
    class Address(models.Model):
        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f'{self.number} {self.street}'


.. autoclass:: lettings.models.Address
    :members:

====================================================

Letting Class :
----------------

.. code-block:: python

    class Letting(models.Model):
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

.. autoclass:: lettings.models.Letting
    :members:



Letting Views :
----------------

**The index view :**

.. code-block:: python

    def index(request):
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)

.. autofunction:: lettings.views.index
    

====================================================

**The letting view :**

.. code-block:: python

    def letting(request, letting_id):
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)


.. autofunction:: lettings.views.letting
    
