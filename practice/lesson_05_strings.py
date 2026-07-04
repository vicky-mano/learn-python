# Lesson 05: Strings

first_name = "Vignesh"
last_name = "Manoharan"
role = "Senior Tableau Developer"
tool = "Tableau"
learning = "Python"

full_name = first_name + " " + last_name
print("Full name:", full_name)

print("First Name:", first_name)
print("Last Name:", last_name)
print("Role:", role)
print("Tool:", tool)
print("Learning:", learning)

sentence = "I am learning python for automation and data work"
print("Sentence:", sentence)

print("First Character of First Name:", first_name[0])
print("Second Character of First Name:", first_name[1])
print("Last Character of First Name:", first_name[-1])

print("First three Character of First Name:", first_name[0:3])
print("Characters from Index onwards:", first_name[3:])

print("Uppercase First Name:", first_name.upper())
print("Lowercase Role:", role.lower())
print("Title Role:", role.title())

print("Length of Full Name:", len(full_name))

message = "  Python is useful  "
print("Original message:", message)
print("Cleaned message:", message.strip())

updated_sentence = sentence.replace("python", "python programming")
print("Updated Sentence:", updated_sentence)

print("Split Full Name:", full_name.split(" "))
print("Does Sentence Contains Python?", "python" in sentence)

intro = "My name is " + full_name + ". I am learning " + learning + "."
print("Intro:", intro)

company = "Heidelsoft"
client = "Solute"

work_summary = company + " works with " + client
print("Work Summary:", work_summary)

professional_intro = (
    "My name is "
    + full_name
    + ". I work as a "
    + role
    + ". I am learning "
    + learning
    + " ."
)
print("Professional Intro:", professional_intro)

raw_skill = "  tableau cloud  "
clean_skill = raw_skill.strip().title()

print("Raw Skill:", raw_skill)
print("Clean Skill:", clean_skill)
