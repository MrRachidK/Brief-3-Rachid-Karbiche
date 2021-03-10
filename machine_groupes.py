#-*- coding: utf-8 -*-
import random

json_student_list = [{
        "last_name": "Fayeulle",
        "first_name": "Mickael",
        "score": 0
    },
    {
        "last_name": "Delobel",
        "first_name": "Joséphine",
        "score": 0
    },
    {
        "last_name": "Karbiche",
        "first_name": "Rachid",
        "score": 0
    },
    {
        "last_name": "Faby",
        "first_name": "Kévin",
        "score": 0
    },
    {
        "last_name": "Vansteenkiste",
        "first_name": "Julien",
        "score": 0
    },
    {
        "last_name": "De smedt",
        "first_name": "Marie",
        "score": 0
    },
    {
        "last_name": "Minéo",
        "first_name": "Valentin",
        "score": 0
    },
    {
        "last_name": "Meyer",
        "first_name": "Tanguy",
        "score": 0
    },
    {
        "last_name": "Sauer",
        "first_name": "Camille",
        "score": 0
    },
    {
        "last_name": "Dupont",
        "first_name": "Pierrette",
        "score": 0
    },
    {
        "last_name": "Durand",
        "first_name": "Romain",
        "score": 0
    },
    {
        "last_name": "Leroy",
        "first_name": "Adrien",
        "score": 0
    },
    {
        "last_name": "Fostier",
        "first_name": "Marine",
        "score": 0
    },
    {
        "last_name": "Gallel",
        "first_name": "Nacyme",
        "score": 0
    },
    {
        "last_name": "Vasseur",
        "first_name": "Leïla",
        "score": 0
    },
    {
        "last_name": "Ponce",
        "first_name": "Pierre",
        "score": 0
    }
]

student_list = []
count = 1

class Student():
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

    def display_student(self):
        return("Nom : {0} \nPrenom : {1}".format(self.last_name, self.first_name))

    def change_student_score(self):
        """ Modification ou non de la note de l'étudiant sur la compétence projet et enregistrement de la nouvelle valeur. 
        """
        new_score_choice = str(input('Voulez-vous changer la note de {0} ?(Y/N)'.format(self.first_name)))
        if(new_score_choice.lower() == 'y'):
            try:
                new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
                if new_score >= 1 and new_score <= 5:
                    self.score = new_score
                    print('Changement de la note effectué.')
                else:
                    while(new_score < 1 or new_score > 5):
                        print('Veuillez indiquer un entier compris entre 1 et 5')
                        new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
            except ValueError:
                print('Veuillez indiquer un entier compris entre 1 et 5')
                new_score = int(input("Quelle est la note de {0} ?".format(self.first_name)))
        elif(new_score_choice.lower() != ('n' and '')):
                print('Erreur de saisie, veuillez tapez \'y\' pour modifier la note ou \'n\' pour passer')
                new_score_choice = str(input('Voulez-vous changer la note de {0} ?(Y/N)'.format(self.first_name)))



class Project():
    def __init__(self, project_name, project_skill, project_distribution, project_group_size):
        self.project_name = project_name
        self.project_skill = project_skill
        self.project_distribution = project_distribution
        self.project_group_size = project_group_size

    def display_project(self):
        """
            Affichage du projet, de sa compétence, du niveau demandé pour les groupes et de leur taille
        """
        distribution = ''
        if(self.project_distribution.lower() == 'hm'):
            distribution = 'Homogène'
        if(self.project_distribution.lower() == 'ht'):
            distribution = 'Hétérogène'

        return("Nom du projet : {0} \nCompétence associée : {1} \nNiveau des groupes : {2} \nTaille des groupes : {3} \n------"
               .format(self.project_name, self.project_skill, distribution, self.project_group_size))


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


if __name__ == '__main__':


    project_name = str(input('Le nom de votre projet : '))
    project_skill = str(input('La compétence du projet : '))

    for student in student_list:
        print(student.display_student())
        student.change_student_score()
        print("Note : {0}".format(student.score))
        print('\n------')

    project_distribution = str(input('La répartition souhaitée (Hm pour Homogène, Ht pour hétérogène) : '))


    while(project_distribution.lower() != 'hm' and project_distribution.lower() != 'ht'):
        print('Erreur de saisie, indiquez "hm" pour une répartition homogène et "ht" pour une répartition hétèrogène des groupes')
        project_distribution = str(input('La répartition souhaitée (Hm pour Homogène, Ht pour hétérogène) : '))

    try:
        project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
        while (project_group_size > 5 or project_group_size < 2) and (type(project_group_size) != int):
            print('Erreur de saisie, veuillez indiquez un nombre entier compris entre 1 et 5.')
            project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
            
    except ValueError:
        print('Erreur de saisie, veuillez indiquez un nombre entier compris entre 1 et 5.')
        project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))

    # project_group_size = int(input("Combien d'apprenants dans vos groupes ? "))
    new_project = Project(project_name, project_skill, project_distribution, project_group_size)
    print(new_project.display_project())


    if project_distribution.lower() == "hm":
        print('------------')
        for student in generate_homogeneous_list(student_list, project_group_size):
            print(student)
        print('------------')
    elif project_distribution.lower() == "ht":
        print('------------')
        for student in generate_heterogeneous_list(student_list, project_group_size):
            print(student)
        print('------------')