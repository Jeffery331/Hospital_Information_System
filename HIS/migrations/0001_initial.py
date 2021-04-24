# Generated by Django 3.2 on 2021-04-24 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='医生编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('age', models.SmallIntegerField(verbose_name='年龄')),
                ('id_num', models.CharField(max_length=11, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('department', models.SmallIntegerField(choices=[(0, '普通内科'), (1, '普通外科'), (2, '骨科'), (3, '儿科'), (4, '妇产科')], default=0, verbose_name='科室')),
                ('job_title', models.SmallIntegerField(choices=[(0, '普通'), (1, '专家')], default=0, verbose_name='职称')),
            ],
            options={
                'verbose_name': '医生',
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='护士编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('id_num', models.CharField(max_length=11, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='联系方式')),
            ],
            options={
                'verbose_name': '护士',
                'db_table': 'nurse',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='病人编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('id_num', models.CharField(max_length=11, verbose_name='身份证号')),
                ('phone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('emergency_contact', models.CharField(max_length=11, verbose_name='紧急联系人')),
                ('address', models.CharField(max_length=256, verbose_name='家庭住址')),
                ('status', models.SmallIntegerField(choices=[(0, '未住院'), (1, '已住院')], default=0, verbose_name='住院状态')),
            ],
            options={
                'verbose_name': '病人',
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='用户编号')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('attr', models.SmallIntegerField(choices=[(0, '病人'), (1, '医生'), (2, '护士'), (3, '财务人员'), (4, '药房人员')], default=0, verbose_name='人员属性')),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='挂号单编号')),
                ('department', models.SmallIntegerField(choices=[(0, '普通内科'), (1, '普通外科'), (2, '骨科'), (3, '儿科'), (4, '妇产科')], default=0, verbose_name='科室')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='挂号时间')),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.doctor', verbose_name='医生编号')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.patient', verbose_name='病人编号')),
            ],
            options={
                'verbose_name': '挂号单',
                'db_table': 'register',
            },
        ),
    ]
