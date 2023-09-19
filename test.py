import numpy as np

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