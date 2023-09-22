import numpy as np
import wget

data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades=np.array(data)

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

student_data = np.array([study_hours, grades])

# liste *2 = dédoublement de la liste et array *2 = multiplication des valeurs par 2 
"""print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)"""

#détermine la taille d'une array par son nom
"""n= grades.shape
print(n)"""

#comme pour les listes le [0] indique le 1er élément d'une array
"""k=grades[0]
print(k)"""

#valeur moyenne d'une array avec mean()
"""n=grades.mean()
print(n)"""

"""print(student_data)
k=student_data.shape
print(k)"""

#chercher la 1ere valeur de la 1ere liste
"""k=student_data[0][0]
print(k)"""


#chercher la valeur moyenne de chaque array
"""avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()"""

#{:.2f} sert à afficher uniquement deux nombres après la virgule et le \ à aller à la ligne
"""print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))"""

"""--------------------------------------Partie Pandas------------------------------------------------------"""


import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

#print(df_students) 


"""--------------------------------------Partie DataFrame------------------------------------------------------"""

#permet d'avoir les info de la 5eme collone 
"""h=df_students.loc[5]
print(h)"""

#permet d'avoir les infos de la 1ere à la 5eme collone  (0 à 5)
"""h=df_students.loc[0:5]
print(h)"""

#permet d'avoir les infos de la 1ere à la 5eme collone  (0 à 4) par la position
"""h=df_students.iloc[0:5]
print(h)"""

#va chercher les infos des colonnes  1 et 2 et de la ligne 0 
"""h=df_students.iloc[0,[1,2]]
print(h)"""

#va chercher l'élément 0 dans le colonne nomée : Grade
"""h=df_students.loc[0,'Grade']
print(h)"""

#va chercher les infos en fonction du nom
"""h=df_students.loc[df_students['Name']=='Aisha']
print(h)"""

#same as before mais écrit d'une manière différente
"""df_students[df_students['Name']=='Aisha']"""

#same as before but w/ query fonction
"""df_students.query('Name=="Aisha"')"""

#prendre les données d'un site
wget.download("https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv")
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
h=df_students
print(h)

n=df_students.isnull()
print(n)