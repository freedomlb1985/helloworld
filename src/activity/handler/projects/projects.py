from django.db import transaction
from rest_framework import serializers
from container.models.projects import Project
from container.models.tagcontainers import TagContainer
from container.models.versions import Version
from container.serializers.tagcontainers import TagContainerSerializer
from activity.handler.activitydeco import container_deco, test_deco


class ProjectSerializer(serializers.ModelSerializer):
    containers = TagContainerSerializer(many=True)
    container_count = serializers.SerializerMethodField()
    last_modified = serializers.SerializerMethodField()

    def get_container_count(self, project):
        return TagContainer.objects.filter(
            deleted=False, project_id=project.pk).count()

    def get_last_modified(self, project):
        return project.get_last_modified_time().strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Project
        exclude = ('deleted', 'created', 'account')
        extra_kwargs = {'last_modified': {'read_only': True},
                        'containers': {'write_only': True}}

    @transaction.atomic
    @test_deco('create')
    @container_deco
    def create(self, validated_data):
        try:
            print self.__context__
        except Exception, e:
            print e
        
        print self.context()
        print validated_data
        containers_data = validated_data.pop('containers', None)
        account = validated_data.pop('account', None)
        print '@@@@@@@@@@@@@@@@@@@@@@'
        print type(validated_data)
        print validated_data
        print account
        print containers_data
        project = Project.objects.create(account=account, **validated_data)

        for container_data in containers_data:
            container = TagContainer.objects.create(project=project,
                                                    owner=account,
                                                    **container_data)
            init_version = Version.objects.create(owner=container,
                                                  version_number=1,
                                                  published=0)
            container.editing_version = init_version.version_number
            container.save()

        return project
