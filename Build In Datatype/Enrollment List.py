cet_students = {"Shubham", "Ankit", "Aditya", "Gautam"}
jee_students = {"Praveen", "Manav", "Aditya", "Gautam"}
neet_students = {"Omkar", "Utkarsh", "Shubham", "Manav"}

print("CET Students:", cet_students)
print("JEE Students:", jee_students)
print("NEET Students:", neet_students)

all_students = cet_students.union(jee_students, neet_students)
print("\nStudents appearing in any of the exams (Union):", all_students)

common_students = cet_students.intersection(jee_students, neet_students)
print("Students appearing in all exams (Intersection):", common_students)

cet_not_jee = cet_students.difference(jee_students)
print("Students appearing in CET but not in JEE (Difference):", cet_not_jee)

jee_not_neet = jee_students.difference(neet_students)
print("Students appearing in JEE but not in NEET (Difference):", jee_not_neet)

neet_not_cet = neet_students.difference(cet_students)
print("Students appearing in NEET but not in CET (Difference):", neet_not_cet)