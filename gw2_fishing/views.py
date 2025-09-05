from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Fish, Time, FishHole, Daily

def fish_list(request):
    fishes = Fish.objects.select_related('item', 'bait__item', 'achievement').all()

    data = []
    for fish in fishes:
        fish_data = {
            "model": "gw2_fishing.fish",
            "pk": fish.pk,
            "fields": {
                "item": {
                    "id": fish.item.api_id,
                    "name": fish.item.name,
                    "rarity": fish.item.rarity,
                    "icon": fish.item.icon,
                },
                "power_min": fish.power_min,
                "power_max": fish.power_max,
                "bait": None,
                "bait_any": fish.bait_any,
                "achievement": None,
                "specialization": fish.specialization,
                "strange_diet_achievement": fish.strange_diet_achievement,
                "times": [],
                "holes": [],
                "daily_catch": fish.daily_catch
            }
        }

        # Bait
        if fish.bait:
            fish_data["fields"]["bait"] = {
                "pk": fish.bait.pk,
                "item": {
                    "id": fish.bait.item.api_id,
                    "name": fish.bait.item.name,
                    "rarity": fish.bait.item.rarity,
                    "icon": fish.bait.item.icon,
                },
                "power": fish.bait.power,
            }

        # Achievement
        if fish.achievement:
            fish_data["fields"]["achievement"] = {
                "pk": fish.achievement.pk,
                "name": fish.achievement.name,
                "achievement_id": fish.achievement.achievement_id,
                "repeat_achievement_id": fish.achievement.repeat_achievement_id,
            }

        # Times
        times = Time.objects.filter(fish=fish)
        for time in times:
            fish_data["fields"]["times"].append({
                "moment": time.moment,
                "frequency": time.frequency,
            })

        # Holes
        fishholes = FishHole.objects.filter(fish=fish).select_related('hole')
        for fh in fishholes:
            fish_data["fields"]["holes"].append({
                "pk": fh.hole.pk,
                "hole": fh.hole.name,
                "frequency": fh.frequency,
            })

        data.append(fish_data)

    return JsonResponse(data, safe=False)


def daily_list(request):
    query = Daily.objects.order_by('-date')[:7]
    data = serializers.serialize('json', query, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')
