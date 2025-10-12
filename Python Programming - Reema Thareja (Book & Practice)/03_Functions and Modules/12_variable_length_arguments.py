def func(name,*fav_subjects): # Here fav_subjects is a variable-length parameter and it must be written in the last
    print("\n",name,"likes to read")
    for subject in fav_subjects:
        print(subject)

func("Nishant","Python","DSA","Mathematics")
func("Rohit","Mathematics","Geography","English","Sanskrit","Spanish")
func("Ram","Python")
func("Sweta")