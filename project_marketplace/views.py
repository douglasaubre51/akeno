from django.shortcuts import render

from .models import Project

# Create your views here.
def get_project_marketplace_page(request):
    projects = Project.objects.all().values()

    context = {
            'projects': projects
            }

    return render(
            request,
            'project-marketplace.html',
            context
            )


def view_selected_project(request, project_id):
    print(project_id)
    project = Project.objects.get(id = project_id)

    context = {
        'project': project
    }

    return render(
        request,
        'view-project.html',
        context
    )
