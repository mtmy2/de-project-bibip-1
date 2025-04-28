        # Запись в файл models_index.txt
with open('D:\YandexDisk\Документы\Обучение\DataAnalisys\Яндекс практикум\YaMyPract\de-project-bibip\de-project-bibip\src\models_index.txt', 'w+') as mi:
    line_number = str(len(mi.readlines())+1)
    if mi.readlines() == []:
        model_index_new = [f'"Lada",{line_number}'+'\n']
    else:
        model_index_new = mi.readlines().append(f'"Lada",{line_number}'+'\n')
    models_index_sorted = sorted(model_index_new)
    for line in models_index_sorted:
        mi.write(f'{line}\n')