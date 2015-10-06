# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import common.models
import django_otp.util


class Migration(migrations.Migration):

    dependencies = [
        ('two_factor', '0002_auto_20150110_0810'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoFactorEmailDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The human-readable name of this device.', max_length=64)),
                ('confirmed', models.BooleanField(default=True, help_text=b'Is this device ready for use?')),
                ('key', models.CharField(default=common.models.get_default_key, help_text=b'A hex-encoded secret key of up to 20 bytes.', max_length=80, validators=[django_otp.util.hex_validator])),
                ('user', models.ForeignKey(help_text=b'The user that this device belongs to.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwoFactorPhoneDevice',
            fields=[
                ('phonedevice_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='two_factor.PhoneDevice')),
            ],
            bases=('two_factor.phonedevice',),
        ),
    ]
