# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Approach(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'approach'

    def __str__(self):
        full_path = [self.name]

        k=self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Specialty(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = 'specialty'

    def __str__(self):
        full_path = [self.name]

        k=self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Entry(models.Model):
    email = models.EmailField(primary_key=True)
    irisLink = models.TextField(default="")
    approach = models.ForeignKey('Approach', null=True, blank=True)
    specialty = models.ForeignKey('Specialty', null=True, blank=True)
    faculty = models.CharField(default="", max_length=200)
    status = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(Entry, self).save(*args, **kwargs)
        bs = Approach.objects.get(name="biologicalsystem")
        cc = Approach.objects.get(name="criticalcare")
        ch = Approach.objects.get(name="childhealth")
        mb = Approach.objects.get(name="mobility")
        i = Specialty.objects.get(name="imaging")
        mo = Specialty.objects.get(name="modelling")
        ds = Specialty.objects.get(name="datasecurity")
        hf = Specialty.objects.get(name="humanfactors")

        if self.approach == bs and self.specialty == i:
            email = Entry.objects.get(email=self.email)
            obj = Bsi.objects.create(email=email)
            obj.save()
        elif self.approach == bs and self.specialty == mo:
            email = Entry.objects.get(email=self.email)
            obj = Bsm.objects.create(email=email)
            obj.save()
        elif self.approach == bs and self.specialty == ds:
            email = Entry.objects.get(email=self.email)
            obj = Bsds.objects.create(email=email)
            obj.save()
        elif self.approach == bs and self.specialty == hf:
            email = Entry.objects.get(email=self.email)
            obj = Bshf.objects.create(email=email)
            obj.save()
        elif self.approach == cc and self.specialty == i:
            email = Entry.objects.get(email=self.email)
            obj = Cci.objects.create(email=email)
            obj.save()
        elif self.approach == cc and self.specialty == mo:
            email = Entry.objects.get(email=self.email)
            obj = Ccm.objects.create(email=email)
            obj.save()
        elif self.approach == cc and self.specialty == ds:
            email = Entry.objects.get(email=self.email)
            obj = Ccds.objects.create(email=email)
            obj.save()
        elif self.approach == cc and self.specialty == hf:
            email = Entry.objects.get(email=self.email)
            obj = Cchf.objects.create(email=email)
            obj.save()
        elif self.approach == ch and self.specialty == i:
            email = Entry.objects.get(email=self.email)
            obj = Chi.objects.create(email=email)
            obj.save()
        elif self.approach == ch and self.specialty == mo:
            email = Entry.objects.get(email=self.email)
            obj = Chm.objects.create(email=email)
            obj.save()
        elif self.approach == ch and self.specialty == ds:
            email = Entry.objects.get(email=self.email)
            obj = Chds.objects.create(email=email)
            obj.save()
        elif self.approach == ch and self.specialty == hf:
            email = Entry.objects.get(email=self.email)
            obj = Chhf.objects.create(email=email)
            obj.save()
        elif self.approach == mb and self.specialty == i:
            email = Entry.objects.get(email=self.email)
            obj = Mi.objects.create(email=email)
            obj.save()
        elif self.approach == mb and self.specialty == mo:
            email = Entry.objects.get(email=self.email)
            obj = Mm.objects.create(email=email)
            obj.save()
        elif self.approach == mb and self.specialty == ds:
            email = Entry.objects.get(email=self.email)
            obj = Mds.objects.create(email=email)
            obj.save()
        elif self.approach == mb and self.specialty == hf:
            email = Entry.objects.get(email=self.email)
            obj = Mhf.objects.create(email=email)
            obj.save()
        else:
            pass

    def get_app_list(self):           #for now ignore this instance method,
        k = self.approach
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
            return breadcrumb[-1:0:-1]

    def get_spc_list(self):           #for now ignore this instance method,
        k = self.specialty
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
            return breadcrumb[-1:0:-1]

class Bsi(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Bsm(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Bsds(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Bshf(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Cci(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Ccm(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Ccds(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Cchf(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Chi(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Chm(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Chds(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Chhf(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Mi(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Mm(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Mds(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Mhf(models.Model):
    email = models.ForeignKey('Entry', null=True, blank=True)

    def __str__(self):
        return str(self.email)
