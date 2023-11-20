# Generated by Django 4.2.7 on 2023-11-20 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_legal_name', models.CharField(max_length=30)),
                ('entity_type', models.CharField(choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Partnership', 'Partnership'), ('Limited Liability Company', 'Limited Liability Company'), ('Corporation', 'Corporation'), ('Cooperative', 'Cooperative'), ('Nonprofit', 'Nonprofit'), ('Trust', 'Trust'), ('Estate', 'Estate'), ('Other', 'Other')], max_length=30)),
                ('entity_state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('VI', 'U.S. Virgin Islands'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='AccountProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aware_clientid', models.IntegerField()),
                ('ein_number', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.account')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('street_address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('county', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('VI', 'U.S. Virgin Islands'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('country', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.account')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PersonProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField()),
                ('social_security_number', models.CharField(max_length=11)),
                ('mobile_phone_country_code', models.CharField(max_length=2)),
                ('mobile_phone_number', models.CharField(max_length=10)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clover.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.account')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='accounts',
            field=models.ManyToManyField(through='clover.PersonAccount', to='clover.account'),
        ),
        migrations.CreateModel(
            name='LocationProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_country_code', models.CharField(max_length=2)),
                ('phone_number', models.CharField(max_length=10)),
                ('fax_country_code', models.CharField(max_length=2)),
                ('fax_number', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.brand')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clover.location')),
            ],
        ),
        migrations.CreateModel(
            name='DomainProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registrar', models.CharField(max_length=30)),
                ('nameservers', models.CharField(max_length=30)),
                ('expires', models.DateField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('status', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.brand')),
                ('domain', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clover.domain')),
            ],
        ),
        migrations.CreateModel(
            name='BrandProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='brand_logos')),
                ('primary_color', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=30)),
                ('secondary_color', models.CharField(max_length=6)),
                ('acccent_color', models.CharField(max_length=6)),
                ('extra_color', models.CharField(max_length=6)),
                ('primary_font', models.CharField(max_length=30)),
                ('seconary_font', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clover.brand')),
            ],
        ),
    ]
