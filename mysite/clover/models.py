from django.db import models
from django.db import models

SBA_US_ENTITY_TYPE_CHOICES = (
    ('Sole Proprietorship', 'Sole Proprietorship'),
    ('Partnership', 'Partnership'),
    ('Limited Liability Company', 'Limited Liability Company'),
    ('Corporation', 'Corporation'),
    ('Cooperative', 'Cooperative'),
    ('Nonprofit', 'Nonprofit'),
    ('Trust', 'Trust'),
    ('Estate', 'Estate'),
    ('Other', 'Other'),
)

US_STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('MP', 'Northern Mariana Islands'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('VI', 'U.S. Virgin Islands'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)


class Account(models.Model):
    """
    Represents an account in the system.
    """
    entity_legal_name = models.CharField(max_length=30)
    entity_type = models.CharField(
        max_length=30, choices=SBA_US_ENTITY_TYPE_CHOICES)
    entity_state = models.CharField(max_length=2, choices=US_STATE_CHOICES)

    def __str__(self):
        return self.entity_legal_name


class AccountProfile(models.Model):
    """
    Represents an account profile.
    """
    aware_clientid = models.IntegerField()
    ein_number = models.CharField(max_length=9)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)


class Person(models.Model):
    """
    Represents a person in the system.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name


class PersonProfile(models.Model):
    """
    Represents a person's profile.
    """
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    mobile_phone_country_code = models.CharField(max_length=2)
    mobile_phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


class Brand(models.Model):
    """
    Represents a brand in the system.
    """

    brand = models.CharField(max_length=30)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.account.entity_legal_name + " | " + self.brand


class BrandProfile(models.Model):
    """
    Represents a brand profile.

    Attributes:
        logo (ImageField): The logo of the brand.
        primary_color (CharField): The primary color of the brand.
        description (CharField): A brief description of the brand.
        secondary_color (CharField): The secondary color of the brand.
        acccent_color (CharField): The accent color of the brand.
        extra_color (CharField): An additional color of the brand.
        primary_font (CharField): The primary font of the brand.
        seconary_font (CharField): The secondary font of the brand.
        brand (ForeignKey): The brand associated with the profile.
    """

    logo = models.ImageField(upload_to='brand_logos')
    primary_color = models.CharField(max_length=6)
    description = models.CharField(max_length=30)
    secondary_color = models.CharField(max_length=6)
    acccent_color = models.CharField(max_length=6)
    extra_color = models.CharField(max_length=6)
    primary_font = models.CharField(max_length=30)
    seconary_font = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Domain(models.Model):
    """
    Represents a domain.
    """
    domain = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.domain + " | " + self.brand.brand


class DomainProfile(models.Model):
    """
    Represents a domain profile.

    Attributes:
        domain (Domain): The associated domain.
        brand (Brand): The associated brand.
        registrar (str): The registrar of the domain.
        nameservers (str): The nameservers of the domain.
        expires (date): The expiration date of the domain.
        created (date): The creation date of the domain.
        updated (date): The last updated date of the domain.
        status (str): The status of the domain.
    """
    domain = models.OneToOneField(Domain, on_delete=models.CASCADE)
    registrar = models.CharField(max_length=30)


class Location(models.Model):
    """
    Represents a physical location.

    Attributes:
        name (str): The name of the location.
        street_address (str): The street address of the location.
        city (str): The city where the location is situated.
        county (str): The county where the location is situated.
        state (str): The state where the location is situated. Must be one of the choices in `US_STATE_CHOICES`.
    """
    location = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    state = models.CharField(max_length=2, choices=US_STATE_CHOICES)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class LocationProfile(models.Model):
    """
    Represents a location profile.

    Attributes:
        phone_country_code (str): The country code for the phone number.
        phone_number (str): The phone number.
        fax_country_code (str): The country code for the fax number.
        fax_number (str): The fax number.
        location (Location): The associated location.
        brand (Brand): The associated brand.
        description (str): The description of the location profile.
    """
    phone_country_code = models.CharField(max_length=2)
    phone_number = models.CharField(max_length=10)
    fax_country_code = models.CharField(max_length=2)
    fax_number = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)


class PersonAccount(models.Model):
    """
    Represents a relationship between a person and an account.
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)
