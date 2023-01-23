from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pizza': {
        'тесто, кг': 0.3,
        'колбаса, г': 100,
        'сыр, г': 100,
        'грибы, г': 50,
    },
}


def dish_view(request, dish):
    context = {}
    context['recipe'] = DATA.get(dish).copy()
    servings = int(request.GET.get('servings', '1'))

    for name, amount in context['recipe'].items():
        context['recipe'][name] = amount * servings

    return render(request, 'calculator/index.html', context)
