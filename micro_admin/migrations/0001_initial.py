# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('username', models.CharField(unique=True, max_length=50)),
                ('email', models.EmailField(unique=True, max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('user_roles', models.CharField(max_length=20, choices=[(b'BranchManager', b'BranchManager'), (b'LoanOfficer', b'LoanOfficer'), (b'Cashier', b'Cashier')])),
                ('date_of_birth', models.DateField(default=b'2000-01-01', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=150, null=True)),
                ('mobile', models.CharField(default=b'0', max_length=10, null=True)),
                ('pincode', models.CharField(default=b'', max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('opening_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('phone_number', models.IntegerField()),
                ('pincode', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('created_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('account_number', models.CharField(unique=True, max_length=50)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(default=True, max_length=10, null=True)),
                ('gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('client_role', models.CharField(max_length=20, choices=[(b'FirstLeader', b'FirstLeader'), (b'SecondLeader', b'SecondLeader'), (b'GroupMember', b'GroupMember')])),
                ('occupation', models.CharField(max_length=200)),
                ('annual_income', models.BigIntegerField()),
                ('joined_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('mobile', models.CharField(default=True, max_length=20, null=True)),
                ('pincode', models.CharField(default=True, max_length=20, null=True)),
                ('photo', models.ImageField(null=True, upload_to=b'static/images/users')),
                ('signature', models.ImageField(null=True, upload_to=b'static/images/signatures')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(default=b'UnAssigned', max_length=50, null=True)),
                ('sharecapital_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('entrancefee_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('membershipfee_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('bookfee_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('insurance_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FixedDeposits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposited_date', models.DateField()),
                ('status', models.CharField(max_length=20, choices=[(b'Opened', b'Opened'), (b'Closed', b'Closed')])),
                ('fixed_deposit_number', models.CharField(unique=True, max_length=50)),
                ('fixed_deposit_amount', models.DecimalField(max_digits=19, decimal_places=6)),
                ('fixed_deposit_period', models.IntegerField()),
                ('fixed_deposit_interest_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('nominee_firstname', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_lastname', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('relationship_with_nominee', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_date_of_birth', models.DateField()),
                ('nominee_occupation', models.CharField(max_length=50, null=True, blank=True)),
                ('fixed_deposit_interest', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('maturity_amount', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('client', models.ForeignKey(to='micro_admin.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('account_number', models.CharField(unique=True, max_length=50)),
                ('activation_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(default=b'UnAssigned', max_length=50)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
                ('clients', models.ManyToManyField(to='micro_admin.Client', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='group_created_by', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupMeetings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.CharField(max_length=20)),
                ('group', models.ForeignKey(to='micro_admin.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LoanAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_no', models.CharField(unique=True, max_length=50)),
                ('interest_type', models.CharField(max_length=20, choices=[(b'Flat', b'Flat'), (b'Declining', b'Declining')])),
                ('status', models.CharField(max_length=20, choices=[(b'Applied', b'Applied'), (b'Withdrawn', b'Withdrawn'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')])),
                ('opening_date', models.DateField(auto_now_add=True)),
                ('approved_date', models.DateField(null=True, blank=True)),
                ('loan_issued_date', models.DateField(null=True, blank=True)),
                ('closed_date', models.DateField(null=True, blank=True)),
                ('loan_amount', models.DecimalField(max_digits=19, decimal_places=6)),
                ('loan_repayment_period', models.IntegerField()),
                ('loan_repayment_every', models.IntegerField()),
                ('loan_repayment_amount', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('total_loan_amount_repaid', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('loanpurpose_description', models.TextField()),
                ('annual_interest_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('interest_charged', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('total_interest_repaid', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('total_loan_paid', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('total_loan_balance', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('loanprocessingfee_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('no_of_repayments_completed', models.IntegerField(default=0)),
                ('client', models.ForeignKey(blank=True, to='micro_admin.Client', null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, to='micro_admin.Group', null=True)),
                ('loan_issued_by', models.ForeignKey(related_name='loan_issued_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('voucher_number', models.CharField(unique=True, max_length=50)),
                ('payment_type', models.CharField(max_length=25, choices=[(b'Loans', b'Loans'), (b'TravellingAllowance', b'TravellingAllowance'), (b'Paymentofsalary', b'Paymentofsalary'), (b'PrintingCharges', b'PrintingCharges'), (b'StationaryCharges', b'StationaryCharges'), (b'OtherCharges', b'OtherCharges'), (b'SavingsWithdrawal', b'SavingsWithdrawal'), (b'FixedWithdrawal', b'FixedWithdrawal'), (b'RecurringWithdrawal', b'RecurringWithdrawal')])),
                ('amount', models.DecimalField(max_digits=19, decimal_places=6)),
                ('interest', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('total_amount', models.DecimalField(max_digits=19, decimal_places=6)),
                ('totalamount_in_words', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
                ('client', models.ForeignKey(blank=True, to='micro_admin.Client', null=True)),
                ('group', models.ForeignKey(blank=True, to='micro_admin.Group', null=True)),
                ('staff', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('receipt_number', models.CharField(unique=True, max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('account_number', models.CharField(max_length=50)),
                ('sharecapital_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('entrancefee_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('membershipfee_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('bookfee_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('loanprocessingfee_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('savingsdeposit_thrift_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('fixeddeposit_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('recurringdeposit_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('loanprinciple_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('loaninterest_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('insurance_amount', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('savings_balance_atinstant', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('demand_loanprinciple_amount_atinstant', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('demand_loaninterest_amount_atinstant', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('principle_loan_balance_atinstant', models.DecimalField(default=0, null=True, max_digits=19, decimal_places=6, blank=True)),
                ('branch', models.ForeignKey(to='micro_admin.Branch')),
                ('client', models.ForeignKey(blank=True, to='micro_admin.Client', null=True)),
                ('group', models.ForeignKey(default=0, blank=True, to='micro_admin.Group', null=True)),
                ('staff', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecurringDeposits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deposited_date', models.DateField()),
                ('reccuring_deposit_number', models.CharField(unique=True, max_length=50)),
                ('status', models.CharField(max_length=20, choices=[(b'Opened', b'Opened'), (b'Closed', b'Closed')])),
                ('recurring_deposit_amount', models.DecimalField(max_digits=19, decimal_places=6)),
                ('recurring_deposit_period', models.IntegerField()),
                ('recurring_deposit_interest_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('nominee_firstname', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_lastname', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_gender', models.CharField(max_length=10, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('relationship_with_nominee', models.CharField(max_length=50, null=True, blank=True)),
                ('nominee_date_of_birth', models.DateField()),
                ('nominee_occupation', models.CharField(max_length=50, null=True, blank=True)),
                ('recurring_deposit_interest', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('maturity_amount', models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)),
                ('client', models.ForeignKey(to='micro_admin.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_no', models.CharField(unique=True, max_length=50)),
                ('status', models.CharField(max_length=20, choices=[(b'Applied', b'Applied'), (b'Withdrawn', b'Withdrawn'), (b'Approved', b'Approved'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')])),
                ('opening_date', models.DateField()),
                ('min_required_balance', models.DecimalField(max_digits=5, decimal_places=2)),
                ('savings_balance', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('annual_interest_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('total_deposits', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('total_withdrawals', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('fixeddeposit_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('fixeddepositperiod', models.IntegerField(null=True, blank=True)),
                ('recurringdeposit_amount', models.DecimalField(default=0, max_digits=19, decimal_places=6)),
                ('recurringdepositperiod', models.IntegerField(null=True, blank=True)),
                ('client', models.ForeignKey(blank=True, to='micro_admin.Client', null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, to='micro_admin.Group', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recurringdeposits',
            name='savings_account',
            field=models.ForeignKey(to='micro_admin.SavingsAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fixeddeposits',
            name='savings_account',
            field=models.ForeignKey(to='micro_admin.SavingsAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='centers',
            name='groups',
            field=models.ManyToManyField(to='micro_admin.Group', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, to='micro_admin.Branch', null=True),
            preserve_default=True,
        ),
    ]
