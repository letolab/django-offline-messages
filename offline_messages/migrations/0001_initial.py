# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OfflineMessage'
        db.create_table(u'offline_messages_offlinemessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'])),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=20)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('read', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('meta', self.gf('jsonfield.fields.JSONField')(default={}, null=True, blank=True)),
        ))
        db.send_create_signal(u'offline_messages', ['OfflineMessage'])


    def backwards(self, orm):
        # Deleting model 'OfflineMessage'
        db.delete_table(u'offline_messages_offlinemessage')
