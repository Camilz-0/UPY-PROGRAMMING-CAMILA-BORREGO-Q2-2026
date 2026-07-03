# Required Structures
usuarios = {
    'cborrego': {'password': '1234', 'rol': 'alumno', 'nombre': 'Camila Borrego'},
    'gdiaz': {'password': '1234', 'rol': 'alumno', 'nombre': 'Gabriela Díaz'},
    'coliveira': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos Oliveira'},
    'lcroft': {'password': '1234', 'rol': 'alumno', 'nombre': 'Lara Croft'},
    'acaamal': {'password': '1234', 'rol': 'alumno', 'nombre': 'Angel Caamal'},
    'lbergvall': {'password': '1234', 'rol': 'alumno', 'nombre': 'Lucas Bergvall'},
    'dayala': {'password': '1234', 'rol': 'maestro', 'nombre': 'Diana Ayala'},
    'msanchez': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Margarita Sanchez'}
}

materias = (
    'Discrete Mathematics',
    'Programming',
    'English II',
    'Differential Calculus',
    'Probability and Statistics',
    'Computer and Server Architecture',
    'Socio-Emotional Skills and Conflict Management'
)

calificaciones = {
    'cborrego': {'Discrete Mathematics': 8.5, 'Programming': 8.0, 'English II': 9.0, 'Differential Calculus': 9.8, 'Probability and Statistics': 8.3, 'Computer and Server Architecture': 9.0, 'Socio-Emotional Skills and Conflict Management': 9.5},
    'gdiaz': {'Discrete Mathematics': 9.0, 'Programming': 8.8, 'English II': 9.4, 'Differential Calculus': 7.8, 'Probability and Statistics': 9.1, 'Computer and Server Architecture': 8.9, 'Socio-Emotional Skills and Conflict Management': 9.8},
    'coliveira': {'Discrete Mathematics': 7.5, 'Programming': 8.0, 'English II': 8.5, 'Differential Calculus': 7.0, 'Probability and Statistics': 7.8, 'Computer and Server Architecture': 6.2, 'Socio-Emotional Skills and Conflict Management': 8.9},
    'lcroft': {'Discrete Mathematics': 9.5, 'Programming': 9.8, 'English II': 9.2, 'Differential Calculus': 9.0, 'Probability and Statistics': 9.6, 'Computer and Server Architecture': 9.4, 'Socio-Emotional Skills and Conflict Management': 10.0},
    'acaamal': {'Discrete Mathematics': 8.2, 'Programming': 6.9, 'English II': 8.8, 'Differential Calculus': 6.0, 'Probability and Statistics': 6.4, 'Computer and Server Architecture': 8.1, 'Socio-Emotional Skills and Conflict Management': 9.0},
    'lbergvall': {'Discrete Mathematics': 8.8, 'Programming': 9.0, 'English II': 8.5, 'Differential Calculus': 7.5, 'Probability and Statistics': 8.9, 'Computer and Server Architecture': 8.7, 'Socio-Emotional Skills and Conflict Management': 9.2}
}

# INPUT
logged_in = False
current_user = ""

while not logged_in:
    username = input("User: ")
    password = input("Password: ")
    
    if username in usuarios and usuarios[username]['password'] == password:
        logged_in = True
        current_user = username
        role = usuarios[username]['rol']
        name = usuarios[username]['nombre']
        print(f"Bienvenid@!, {name} ({role if role != 'maestro' else 'professor'})")
    else:
        print("Credenciales incorrectas. Intente de nuevo.")

# PROCESS & OUTPUT
if role == 'alumno':
    print("=======================================")
    print("  School Report")
    print("=======================================")
    
    approved = set()
    pending = set()
    
    for materia in materias:
        grade = calificaciones[current_user][materia]
        print(f"{materia:<45} : {grade}")
        if grade >= 8.0:
            approved.add(materia)
        else:
            pending.add(materia)
            
    print(f"Approved: {approved}")
    print(f"Pending : {pending}")

elif role == 'maestro':
    print("=======================================")
    print("  Students")
    print("=======================================")
    for user, data in usuarios.items():
        if data['rol'] == 'alumno':
            print(f"User: {user:<10} | Student: {data['nombre']}")
            
    student_to_grade = input("\nStudent to grade (username): ")
    if student_to_grade in calificaciones:
        print("Subjects:")
        for materia in materias:
            print(materia)
            
        subject_to_grade = input("\nSubject to grade: ")
        if subject_to_grade in materias:
            new_grade_str = input("New grade: ")
            new_grade = float(new_grade_str)
            
            old_grade = calificaciones[student_to_grade][subject_to_grade]
            confirm = input(f"\nDo you confirm (yes/no)?\n{subject_to_grade}: {old_grade} ==> {new_grade}\n")
            
            if confirm.lower() == 'yes':
                calificaciones[student_to_grade][subject_to_grade] = new_grade
                print("\nGrade updated!")
                print(calificaciones[student_to_grade])
            else:
                print("\nWrite other thing to exit")
        else:
            print("Materia no válida.")
    else:
        print("Estudiante no encontrado.")

elif role == 'coordinador':
    print("=======================================")
    print("  Professors")
    print("=======================================")
    for user, data in usuarios.items():
        if data['rol'] == 'maestro':
            print(f"User: {user:<10} | Professor: {data['nombre']}")
            
    print("\n=======================================")
    print("  Students")
    print("=======================================")
    for user, data in usuarios.items():
        if data['rol'] == 'alumno':
            print(f"User: {user:<10} | Student: {data['nombre']}")
            
    print("\n=======================================")
    print("  Records")
    print("=======================================")
    
    # Print table header
    header = f"{'SUBJECTS':<35} | "
    for student in calificaciones.keys():
        header += f"{student:<8} | "
    print(header)
    print("-" * len(header))
    
    # Print subject rows
    for materia in materias:
        row = f"{materia[:33]:<35} | "
        for student in calificaciones.keys():
            grade = calificaciones[student][materia]
            row += f"{grade:<8} | "
        print(row)