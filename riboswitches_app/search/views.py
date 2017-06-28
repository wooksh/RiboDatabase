from django.shortcuts import render
from django.http import JsonResponse

from collections import OrderedDict

from database.models import Record, Ligand, Gene, Organism, Aptamer, Article


def index(request):
    context = {'breadcrumbs': []}
    return render(request, 'search/index.html', context)


def genes(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for g in Gene.objects.filter(name__icontains=term):
        print(g)
        l.append({'name':g.name, 'url':"/search/gene/{}".format(g.name)},)

    return JsonResponse(l, safe=False)


def organisms(request):
    term = request.GET['term']
    limit = request.GET['limit']
    l = []

    for o in Organism.objects.filter(scientific_name__icontains=term):
        l.append({'name':o.scientific_name, 'url':"/search/organism/{}".format(o.scientific_name.replace(' ', '_'))},)

    return JsonResponse(l, safe=False)


def ligands(request):
    term = request.GET['term'] # ligand name
    limit = request.GET['limit']
    lig = []

    for l in Ligand.objects.filter(name__icontains=term):
        lig.append({'name':l.name, 'url':"/browser/ligand/{}/".format(l.name)},)
    
    return JsonResponse(lig, safe=False)


def record(request, riboswitch_name):
    l = []
    context = OrderedDict()

    for a in Aptamer.objects.all():
        if a.switch.id == int(riboswitch_name[2:]):
            pos = a.position
            struct = a.structure
        else:
            pos = 'No position found'
            struct = 'No structure found'

    # Odrzucamy z nazwy dwie pierwsze litery "RS", a część liczbową konwertujemy do Integera
    for r in Record.objects.filter(id=int(riboswitch_name[2:])):
        context['Name'] = r.name()
        context['Organism'] = r.gene.organism.scientific_name
        context['Class'] = r.family.ribo_class.name
        context['Family'] = r.family.name
        lig = r.family.ribo_class.ligands.all()

        if not lig.exists():
            context['Ligand'] = 'None'
        else:
            lig_list = [str(l) for l in list(lig)]
            context['Ligand'] = ', '.join(lig_list)
            
        context['Gene'] = r.gene.name
        context['Promoter'] = r.promoter
        context['Aptamer position'] = pos
        context['Aptamer structure'] = struct
        context['Shine-Dalgarno'] = r.shinedalgarno
        context['Terminator'] = r.terminator
        context['Mechanism'] = r.get_mechanism_display()
        context['Effect'] = r.get_effect_display()
        context['Sequence'] = r.sequence
        articles = r.articles.all()

        temp = 0
        if r.terminator != None:
            terminator_length = r.terminator.end - r.terminator.start
            l2=[]
            for i in r.sequence:
                l2.append(i)
            sequence_length = len(l2)
            temp = (terminator_length/sequence_length)*100

    if not articles.exists():
        context['Articles (Pubmed ID)'] = 'No articles found'
    else:
        newlist = [str(t) for t in list(articles)]
        context['Articles (Pubmed ID)'] = ', '.join(newlist)

    

    l.append(context)
    test = {
        'l': l,
        'name': context['Name'],
        'temp': temp,
    }

    print(context)

    return render(request, 'search/record.html', test)