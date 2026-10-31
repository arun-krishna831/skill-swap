from django.shortcuts import render, redirect,get_object_or_404
from .forms import SkillForm
from django.contrib.auth.decorators import login_required
from .models import Skill,SkillExchangeRequest

@login_required
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.user = request.user
            skill.save()
            return redirect('add_skill')

    else:
        form = SkillForm()

    return render(request, 'skills/add_skill.html', {'form': form})


@login_required
def my_skills(request):
    skills = Skill.objects.filter(user=request.user)

    return render(request, 'skills/my_skills.html', {
        'skills': skills
    })

@login_required
def browse_skills(request):
    skills = Skill.objects.exclude(user=request.user)

    skill_type = request.GET.get('type')

    if skill_type in ['teach', 'learn']:
        skills = skills.filter(skill_type=skill_type)

    return render(request, 'skills/browse_skills.html', {
        'skills': skills,
        'selected_type': skill_type,
    })

@login_required
def send_request(request, skill_id):
    requested_skill = get_object_or_404(Skill, id=skill_id)

    if request.method == 'POST':
        offered_skill_id = request.POST.get('offered_skill')

        offered_skill = get_object_or_404(
            Skill,
            id=offered_skill_id,
            user=request.user,
            skill_type='teach'
        )

        SkillExchangeRequest.objects.create(
            sender=request.user,
            receiver=requested_skill.user,
            offered_skill=offered_skill,
            requested_skill=requested_skill
        )

        return redirect('browse_skills')

    my_skills = Skill.objects.filter(
        user=request.user,
        skill_type='teach'
    )

    return render(request, 'skills/send_request.html', {
        'requested_skill': requested_skill,
        'my_skills': my_skills
    })

@login_required
def incoming_requests(request):
    requests = SkillExchangeRequest.objects.filter(
        receiver=request.user
    ).order_by('-created_at')

    return render(request, 'skills/incoming_requests.html', {
        'requests': requests
    })

@login_required
def respond_request(request, request_id):
    exchange = get_object_or_404(
        SkillExchangeRequest,
        id=request_id,
        receiver=request.user
    )

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'accept':
            exchange.status = 'accepted'
            exchange.save()
        elif action == 'reject':
            exchange.status = 'rejected'
            exchange.save()

        return redirect('incoming_requests')

    return redirect('incoming_requests')