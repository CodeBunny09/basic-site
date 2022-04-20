from django.shortcuts import render
from account.models import UserMeta, Organization

# Create your views here.

def organization_stats(req, id=None):
    
    organizations = Organization.objects.all()

    context = {'organizations': organizations}
    
    if not id:
        return render(req, 'organization.html', context)
    else:
        organization = Organization.objects.get(id=id)
        employees = UserMeta.objects.filter(works_for = organization)
        
        context.update(
            {
                'organizations': organizations,
                'organization': organization,
                'employees' : employees,
            }
        )
        return render(req, 'organization.html', context)