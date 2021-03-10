from liste_etudiants import json_student_list
from classes_machine_groupes import Student, Project

student_list = []

def create_student_list(json_file):
    """ Retourne une liste d'objet avec le prénom, nom et la note de chaque étudiant.
    """
    student_list = [Student(student['first_name'], student['last_name'], student['score']) for student in json_file]
    return student_list

student_list = create_student_list(json_student_list)

def is_even_groups(list, group_size):
    """ Retourne vrai si la taille du groupe est un nombre pair
    """
    return len(list) % group_size == 0

def generate_heterogeneous_list(list, group_size):
    """ Récupère un élément aléatoire d'une liste d'apprenant et l'ajoute à une autre liste tant que sa taille n'excède pas la taille du groupe.
        Supprime l'élément récupéré de la liste principale et retourne la nouvelle liste générée.
    """
    my_new_list = sorted(list, key = lambda k: k.score)
    half = int(len(my_new_list) / 2)
    lower_bracket = my_new_list[0:half]
    upper_bracket = my_new_list[int(len(list) - 1):int(len(list) / 2 - 1):-1]

    generated_list = []
    groups = []
    if(len(list) > 0):
        if is_even_groups(list, group_size):
            i = 0
            while len(groups) < (len(list) // group_size):
                while len(generated_list) < group_size:
                    generated_list.append([lower_bracket[i].first_name, lower_bracket[i].score])
                    generated_list.append([upper_bracket[i].first_name, upper_bracket[i].score])
                    i += 1
                groups.append(generated_list)    
                generated_list = []
        else:
            heterogene_list = []
            for i,j in zip(lower_bracket,upper_bracket):
                heterogene_list.append(i)
                heterogene_list.append(j)
        
            i = group_size + 1
            for i in range(0, group_size + 1):
                generated_list.append([heterogene_list[i].first_name, heterogene_list[i].score])
            groups.append(generated_list)
            generated_list = []
            while(len(groups) < (len(list) // group_size)):
                while(len(generated_list) < group_size):
                    i += 1
                    generated_list.append([heterogene_list[i].first_name, heterogene_list[i].score])
                groups.append(generated_list)
                generated_list = []

    return groups
    
def generate_homogeneous_list(list, group_size):
    """ Tri croissant des étudiants selon leur note et création de groupes homogènes de la taille précisée en paramètre.
    """
    my_new_list = sorted(list, key = lambda k: k.score)
    generated_list = []
    groups = []
    if(len(list) > 0):
        if is_even_groups(list, group_size):
            i = 0
            while len(groups) < (len(list) // group_size):
                while len(generated_list) < group_size:
                    generated_list.append([my_new_list[i].first_name, my_new_list[i].score])
                    i += 1
                groups.append(generated_list)    
                generated_list = []
        else:
            i = group_size + 1
            for i in range(0, group_size + 1):
                generated_list.append([my_new_list[i].first_name, my_new_list[i].score])
            groups.append(generated_list)
            generated_list = []
            while(len(groups) < (len(list) // group_size)):
                while(len(generated_list) < group_size):
                    i += 1
                    generated_list.append([my_new_list[i].first_name, my_new_list[i].score])
                groups.append(generated_list)
                generated_list = []

    return groups