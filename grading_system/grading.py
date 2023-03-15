import cls

cls.a

class grades:
    new={}
    student={}
    grades={}

    def grading_system(self):

        end_grade=False

        name=input("enter the details in the order ('branch_exam_year') for the name of the file\n").lower()
        class_name=input("enter the class name\n").upper()
        with open(str(name+'.txt'), 'w') as file:
            

            while end_grade is False:
                
                cls.a
                num=int(input("enter the number of students u wanna grade:\n"))
                
                for k in range(0,num):
                    
                    cls.a

                    name=input(f"enter the name of student {k+1} :\n")
                    name_1=name
                    length=len(name)
                    spaces=''
                    if length <10:
                        for i in range(length,10):
                            spaces+=" "
                        name+=spaces

                    mark=int(input(f"enter the marks of {name_1}:\n"))

                    self.student[name]=mark

                cls.a 

                for i in self.student:

                    if self.student[i] > 90:
                        self.grades[i]=f"excellent              \t         {self.student[i]}"

                    elif self.student[i]>80:
                        self.grades[i]=f"distinction            \t         {self.student[i]}"

                    elif self.student[i]>60:
                        self.grades[i]=f"average                \t         {self.student[i]}"

                    elif self.student[i]>50:
                        self.grades[i]=f"need improvement       \t         {self.student[i]}"

                    else:
                        self.grades[i]=f"needs heavy improvement\t         {self.student[i]}"
                file.write(f"CLASS :\t{class_name}\n")    
                file.write("   NAME     |        GRADING           |\tAVERAGE MARKS\n")
                for item in self.grades:
                    
                    file.write(f"{item} \t: {self.grades[item]}\n")
                    
                end=input("press C to continue grading and Q to exit \n").lower()

                if end == 'q':

                    end_grade=True

                if end=='c':

                    ask=input("do you want to start grading a different class ('D') or the same class('S') : \n").lower()

                    

                    if ask == 'd':
                        class_name=input("enter the class name\n").upper()
                        file.write("\n-----------------------------------------------------------\nclass break\n-----------------------------------------------------------\n\n")
                        
                    else:
                        class_name += "edit"
                        
                    cls.a
            self.student = {}


student=grades()
student.grading_system()
