"""THE MAIN MOTIVE OF THIS PROGRAM OR PROJECT IS TO MAKE BASIC CALCULATIONS
EASIER WHICH ARE NECESSARY FOR DAY TO DAY LIFE."""
"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

import math

# AS WE KNOW THAT ADDITION BASED CALCULATIONS ARE THE MOST BASIC CALCULATIONS OF DAY TO DAY LIFE.
# SO THIS FUNCTION WILL ADD THREE TYPES OF DATA TYPES MOSTLY THE BASIC REQUIREMENTS.

# THIS FUNCTION KEY WILL DO THE OPERACTIONS REGARDING ADDITION.
def add():
    print("1.INTEGER\n2.FLOAT\n3.MIXED")
    ch=int(input("Enter your choice [1,2,3]:"))
    
    # THE FIRST CHOICE IS INTEGER TYPE ADDITION.
    if ch==1:
        sum=0
        lst=[]
        n=int(input("enter total numbers to be added:"))
        for i in range(n):
            a= int(input("Enter number:"))
            k= lst.append(a)
        for num in lst:
            sum= sum + num
        print("Addition result=",sum)

    # THE SECOND CHOICE IS FLOAT i.e. DECIMAL TYPE ADDITION.
    elif ch==2:
        sum=0
        lst=[]
        n=int(input("enter total numbers to be added:"))
        for i in range(n):
            a= float(input("Enter number:"))
            k= lst.append(a)
        for num in lst:
            sum= sum + num 
        print("Addition result=",sum)

    # THE THIRD CHOICE WILL ACCEPT BOTH TYPES AND DO ADDITION.   
    elif ch==3:
        sum=0
        lst=[]
        n=int(input("enter total numbers to be added:"))
        for i in range(n):
            a= eval(input("Enter number:"))
            k= lst.append(a)
        for num in lst:
            sum= sum + num 
        print("Addition result=",sum)
        
    else:
        print("Your input choice is invalid.\nPlease try again.")


# THIS FUNCTION KEY WILL DO THE OPERATIONS REGARDING SUBTRACTION.        
def subtract():
    print("1.INTEGER\n2.FLOAT\n3.MIXED")
    ch=int(input("Enter your choice [1,2,3]:"))

    # HERE IS THE SUBTRACTION OF INTEGER TYPE NUMBERS.
    if ch==1:
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        diff=b-a
        print("Subtraction result=",diff)

    # SIMILARLY HERE FLOAT i.e. DECIMAL TYPE NUMBER'S SUBTRACTION.      
    elif ch==2:
        a=float(input("Enter 1st decimal number:"))
        b=float(input("Enter 2nd decimal number:"))
        diff=b-a
        print("Subtraction result=",diff)

    # SUPPOSE YOU WANT TO DO BOTH INTEGER AND DECIMAL NUMBERS SUBTRACTION, U CAN DO HERE.        
    elif ch==3:
        a=eval(input("Enter 1st number:"))
        b=eval(input("Enter 2nd number:"))
        diff=b-a
        print("Subtraction result=",diff)
            
    else:
        print("Your input choice is invalid.\nPlease try again.")


# THIS FUNCTION KEY WILL DO THE OPERATIONS REGARDING MULTIPLICATIONS.
def multiply():
# AS LIKE ADDITION AND SUBTRACTION THE SAME CASE HAS BEEN DONE HERE.
# HERE FIRST CHOICE IS INTEGER TYPE
# SECOND ONE FLOAT OR DECIMAL TYPE
# AND THIRD ONE IS BOTH INTEGER AND FLOAT TYPE OPERATION.

    print("1.INTEGER\n2.FLOAT\n3.MIXED")
    ch=int(input("Enter your choice [1,2,3]:"))

    if ch==1:
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        mul=a*b
        print("Multiplication result=",mul)
        
    elif ch==2:
        a=float(input("Enter 1st decimal number:"))
        b=float(input("Enter 2nd decimal number:"))
        mul=a*b
        print("Multiplication result=",mul)
        
    elif ch==3:
        a=eval(input("Enter 1st number:"))
        b=eval(input("Enter 2nd number:"))
        mul=a*b
        print("Multiplication result=",mul)
        
    else:
        print("Your input choice is invalid.\nPlease try again.")

# THE DIVIDE AND AVERAGE FINDING FUNCTIONS CREATED HAVE THE SAME CONCEPT LIKE
# ADDITION, SUBTRACTION AND MULTIPLICATION.
# NO NEED TO EXPLAIN FURTHER.
# YOU CAN UNDERSTAND IT CLEARLY.


# THIS FUNCTION KEY WILL DO THE OPERATIONS REGARDING DIVISION.
def divide():
    print("1.INTEGER\n2.FLOAT\n3.MIXED")
    ch=int(input("Enter your choice [1,2,3]:"))
    
    if ch==1:
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        div=a/b
        print("Division result=",div)
            
    elif ch==2:
        a=float(input("Enter 1st decimal number:"))
        b=float(input("Enter 2nd decimal number:"))
        div=a/b
        print("Division result=",div)
            
    elif ch==3:
        a=eval(input("Enter 1st number:"))
        b=eval(input("Enter 2nd number:"))
        div=a/b
        print("Division result=",div)
            
    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION KEY WILL DO THE OPERATIONS RELATED TO FINDING AVERAGE OF NUMBERS GIVEN AS INPUT BY THE USER.
def average():
    print("1.INTEGER\n2.FLOAT\n3.MIXED")
    ch=int(input("Enter your choice [1,2,3]:"))
    
    if ch==1:
        count=0
        n=int(input("Enter the no.of entries you want to calculate:"))
        for i in n:
            entries=int(input("Enter the number:"))
            count+=entries
            avrg=count/n
            print("Average result=",avrg)
        
    elif ch==2:
        count=0
        n=int(input("Enter the no.of entries you want to calculate:"))
        for i in n:
            entries=float(input("Enter the number:"))
            count+=entries
            avrg=count/n
            print("Average result=",avrg)
        
    elif ch==3:
        count=0
        n=int(input("Enter the no.of entries you want to calculate:"))
        for i in n:
            entries=eval(input("Enter the number:"))
            count+=entries
            avrg=count/n
            print("Average result=",avrg)
        
    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION KEY WILL DO THE OPERATIONS RELATED TO FINDING PERCENTAGE OF THE GIVEN ENTRIES
def percentage():
# HERE YOU HAVE TO PUT THE NUMBER OF ENTRIES MEANS
# AS MUCH AS YOU WANT TO TAKE OUT THE OVERALL PERCENTAGE, IT
# MIGHT BE MARKS OR DATAS OR ANYTHING.
# JUST PUT THE ENTRIES AND GET THE PERCENTAGE OF THE ENTRIES.
    sum=0
    n=int(input("Enter the no.of entries:"))
    for i in n:
        entries=eval(input("Enter the number:"))
        sum+=entries
        total=int(input("Enter total entity:"))
        perc=float((sum/total)*100)
        print("Percentage result=",perc,"%")



# THIS FUNCTION KEY WILL DO THE OPERATIONS RELATED TO FINDING FACTORIAL OF A NUMBER.
def factorial():
# THIS FUNCTION WILL GIVE THE PRODUCT OF THE FACTORIAL OF ANY NUMBER.
# SUPPOSE IF YOU WILL ENTER 5 SO THE FACTORIAL OF 5= 5*4*3*2*1=120,
# LIKE THAT YOU WILL GIVE THE NUMBERS AND THIS FUNCTION WILL RETURN YOU
# THE PRODUCT OF THE FACTORIAL OF THE NUMBER.

    num=int(input("Enter number to be factorialised:"))
    n=num
# HERE I HAVE TO DECLARE ONE DUPLICATE VARIABLE 'n'OF "num",
# THE REASON IS THAT THERE IS WHILE LOOP WHERE n-=1 GIVEN,
# IF I HAVE WRITTEN IT AS num-=1 THEN IN PRINT PART num WILL
# REDUCE TO 1 AND IT WILL DISPLAY "Factorial of 1 is ---".
    if (n==1 or n==0):
        print(1)
    else:
        fact=1
        while n>1:
            fact*=n
            n-=1 
    print("Factorial of",num,"is",fact)



# THIS FUNCTION KEY WILL DO THE OPERATIONS RELATED TO FINDING AREA OF DIFFERENT SHAPES AS PER THE SELECTED CHOICE.
def area():
# I GUESS WE ALL KNOW HOW TO FIND OUT THE AREA OF SOME SHAPES.
# BUT IN CASE OF URGENT, THIS FUNCTION WILL HELP YOU TO FIND OUT THE
# AREA OF THE SHAPES QUICKLY.
# ALL YOU HAVE TO DO IS TO ENTER THE DESIRED DETAILS WHICH WILL BE ASKED.
# AND YOU WILL GET THE RESULT IN ONE SECOND.
    print("1.SQUARE\n2.RECTANGLE\n3.CIRCLE\n4.TRIANGLE\n5.PARALLELOGRAM\n6.RHOMBUS\n7.TRAPEZIUM\n8.ELLIPSE")
    ch=int(input("Enter choice[1,2,..,8]:"))
    
    if ch==1:
        side=eval(input("Enter side length:"))
        ar=float(side*side)
        print("SQUARE Area result=",ar,"sq.units")
        
    elif ch==2:
        length=eval(input("Enter length of rectangle:"))
        width=eval(input("Enter width of rectangle:"))
        ar=float(length*width)
        print("RECTANGLE Area result=",ar,"sq.units")
        
    elif ch==3:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        ar=float(3.14*radius*radius)
        print("CIRCLE Area result=",ar,"sq.units")
        
    elif ch==4:
        base=eval(input("Enter base length:"))
        height=eval(input("Enter height length:"))
        ar=float([base*height]*1/2)
        print("TRIANGLE Area result=",ar,"sq.units")
        
    elif ch==5:
        base=eval(input("Enter base length:"))
        height=eval(input("Enter height length:"))
        ar=float(base*height)
        print("PARALLELOGRAM Area result=",ar,"sq.units")
        
    elif ch==6:
        d1=eval(input("Enter 1st diagonal length:"))
        d2=eval(input("Enter 2nd diagonal length:"))
        ar=float([d1*d2]*1/2)
        print("RHOMBUS Area result=",ar,"sq.units")
        
    elif ch==7:
        a=eval(input("Enter side1 length:"))
        b=eval(input("Enter side2 length:"))
    # a and b are the parallel sides of the trapezium.
        height=eval(input("Enter height length:"))
        ar=float(height*[a+b]*1/2)
        print("TRAPEZIUM Area result=",ar,"sq.units")
        
    elif ch==8:
        b=eval(input("Enter length of semi minor axis:"))
        ar=float(3.14*b)
        print("ELLIPSE Area result=",ar,"sq.units")
    
    else:
        print("Your input choice is invalid.\nPlease try again.")


# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO FINDING PERIMETER OF DIFFERENT SHAPES AS DONE IN CASE OF FINDING AREAS.
def perimeter():
# AS LIKE FINDING AREA OF THOSE SHAPES YOU CAN ALSO FIND PERIMETER OF THOSE 
# AND THE INTERESTING FACT IS THAT, AS YOU DID IN THE PREVIOUS FUNCTION THE SAME
# WORK YOU WILL DO IN THIS FUNCTION AND WILL GET THE RESULT.
    print("1.SQUARE\n2.RECTANGLE\n3.CIRCLE\n4.TRIANGLE\n5.PARALLELOGRAM\n6.RHOMBUS\n7.TRAPEZIUM\n8.ELLIPSE")
    ch=int(input("Enter choice[1,2,..,8]:"))
    
    if ch==1:
        side=eval(input("Enter side length:"))
        peri=float(4*side)
        print("SQUARE Perimeter result=",peri,"units")
        
    elif ch==2:
        length=eval(input("Enter length of rectangle:"))
        width=eval(input("Enter width of rectangle:"))
        peri=float(2*[length+width])
        print("RECTANGLE Perimeter result=",peri,"units")
        
    elif ch==3:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        peri=float(2*3.14*radius)
        print("CIRCLE Perimeter result=",peri,"units")
        
    elif ch==4:
        a=eval(input("Enter side1 length:"))
        b=eval(input("Enter side2 length:"))
        c=eval(input("Enter side3 length:"))
        peri=float(a+b+c)
        print("TRIANGLE Perimeter result=",peri,"units")
        
    elif ch==5:
        a=eval(input("Enter opposite side1 length:"))
        b=eval(input("Enter opposite side2 length:"))
        peri=float(2*[a+b])
        print("PARALLELOGRAM Perimeter result=",peri,"units")
        
    elif ch==6:
        a=eval(input("Enter side of rhombus length:"))
        peri=float(4*a)
        print("RHOMBUS Perimeter result=",peri,"units")
        
    elif ch==7:
        a=eval(input("Enter side1 length:"))
        b=eval(input("Enter side2 length:"))
        c=eval(input("Enter side3 length:"))
        d=eval(input("Enter side4 length:"))
        peri=float(a+b+c+d)
        print("TRAPEZIUM Perimeter result=",peri,"units")
        
    elif ch==8:
        a=eval(input("Enter length of semi major axis:"))
        b=eval(input("Enter length of semi minor axis:"))
        peri=float(3.14*(a+b))
        print("ELLIPSE Perimeter result=",peri,"units")
    
    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO FINDING VOLUME OF DIFFERENT SHAPES AS LIKE DONE IN ABOVE 2 CASES.
def volume():
# IN CASE OF THIS FUNCTION YOU DO THE SAME, JUST ENTER THE DETAILS
# AND GET THE RESULT, BUT ONE THING IS THAT YOU SHOULD HAVE IDEA ABOUT
# PYRAMID AND PRISM BEFORE DEALING WITH THAT
# SO THAT IT WILL BE EASIER FOR YOU. THERE ARE VARIOUS 3-D SHAPES INCLUDED IN IT.
    print("1.CUBE\n2.CUBOID\n3.CONE\n4.CYLINDER\n5.SPHERE\n6.HEMISPHERE\n7.PYRAMID\n8.PRISM")
    ch=int(input("Enter choice[1,2,..,8]:"))
    
    if ch==1:
        side=eval(input("Enter side length:"))
        vol=float(side*side*side)
        print("CUBE Volume result=",vol,"cu.units")
        
    elif ch==2:
        length=eval(input("Enter length of cuboid:"))
        width=eval(input("Enter width of cuboid:"))
        height=eval(input("Enter height of cuboid:"))
        vol=float(length*width*height)
        print("CUBOID Volume result=",vol,"cu.units")
        
    elif ch==3:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        height=eval(input("Enter height length:"))
        vol=float([3.14*radius*radius*height]*1/3)
        print("CONE Volume result=",vol,"cu.units")
        
    elif ch==4:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        height=eval(input("Enter height length:"))
        vol=float(3.14*radius*radius*height)
        print("CYLINDER Volume result=",vol,"cu.units")
        
    elif ch==5:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        vol=float(4/3*[3.14*radius*radius*radius])
        print("SPHERE Volume result=",vol,"cu.units")
        
    elif ch==6:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        vol=float([3.14*radius*radius*radius]*2/3)
        print("HEMISPHERE Volume result=",vol,"cu.units")
        
    elif ch==7:
        print("PYRAMID OPERATIONS")
        print("a.SQUARE PYRAMID\nb.RECTANGULAR PYRAMID\nc.TRIANGULAR PYRAMID\nd.PENTAGONAL PYRAMID")
        ch=input("Enter choice[a,b,c,d]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            base_ar=float(side*side)
            height=eval(input("Enter height of pyramid:"))
            vol=float((1/3)*base_ar*height)
            print("SQUARE PYRAMID VOLUME result=",vol,"cu.units")
            
        elif ch=="b":
            length=eval(input("Enter length of rectangle:"))
            width=eval(input("Enter width of rectangle:"))
            base_ar=float(length*width)
            height=eval(input("Enter height of pyramid:"))
            vol=float((1/3)*base_ar*height)
            print("RECTANGULAR PYRAMID VOLUME result=",vol,"cu.units")
            
        elif ch=="c":
            base=eval(input("Enter base length:"))
            ht=eval(input("Enter height length:"))
            base_ar=float([base*ht]*1/2)
            height=eval(input("Enter height of pyramid:"))
            vol=float((1/3)*base_ar*height)
            print("TRIANGULAR PYRAMID VOLUME result=",vol,"cu.units")
            
        elif ch=="d":
            print("PENTAGONAL PYRAMID OPERATIONS")
            print("1.GIVEN ONLY 'SIDE' LENGHT\n2.GIVEN BOTH 'SIDE' AND 'APOTHEM' LENGTHS")
            ch=int(input("Enter choice[1,2]:"))
            if ch==1:
                side=eval(input("Enter side length:"))
                base_ar=float((1/4)*{math.sqrt(5*[5+2*math.sqrt(5)])}*side*side)
                height=eval(input("Enter height of pyramid:"))
                vol=float((1/3)*base_ar*height)
                print("PENTAGONAL PYRAMID VOLUME result=",vol,"cu.units")
            elif ch==2:
                side=eval(input("Enter length of side:"))
                apothem=eval(input("Enter apothem length of pentagon:"))
                base_ar=float((5/2)*side*apothem)
                height=eval(input("Enter height of pyramid:"))
                vol=float((1/3)*base_ar*height)
                print("PENTAGONAL PYRAMID VOLUME result=",vol,"cu.units")
            else:
                print("Your input choice is invalid.\nPlease try again.")
            
        else:
            print("Your input choice is invalid.\nPlease try again.")


    elif ch==8:
        print("PRISM OPERATIONS")
        print("a.SQUARE PRISM\nb.RECTANGULAR PRISM\nc.TRIANGULAR PRISM\nd.PENTAGONAL PRISM\ne.HEXAGONAL PRISM")
        ch=input("Enter choice[a,b,c,d,e]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            base_ar=float(side*side)
            height=eval(input("Enter height of prism:"))
            vol=float(base_ar*height)
            print("SQUARE PRISM VOLUME result=",vol,"cu.units")
            
        elif ch=="b":
            length=eval(input("Enter length of rectangle:"))
            width=eval(input("Enter width of rectangle:"))
            base_ar=float(length*width)
            height=eval(input("Enter height of prism:"))
            vol=float(base_ar*height)
            print("RECTANGULAR PRISM VOLUME result=",vol,"cu.units")
            
        elif ch=="c":
            base=eval(input("Enter base length:"))
            ht=eval(input("Enter height length:"))
            base_ar=float([base*ht]*1/2)
            height=eval(input("Enter height of prism:"))
            vol=float(base_ar*height)
            print("TRIANGULAR PRISM VOLUME result=",vol,"cu.units")
            
        elif ch=="d":
            print("PENTAGONAL PRISM OPERATIONS")
            print("1.GIVEN ONLY 'SIDE' LENGHT\n2.GIVEN BOTH 'SIDE' AND 'APOTHEM' LENGTHS")
            ch=int(input("Enter choice[1,2]:"))
            if ch==1:
                side=eval(input("Enter side length:"))
                base_ar=float((1/4)*{math.sqrt(5*[5+2*math.sqrt(5)])}*side*side)
                height=eval(input("Enter height of prism:"))
                vol=float(base_ar*height)
                print("PENTAGONAL PRISM VOLUME result=",vol,"cu.units")
            elif ch==2:
                side=eval(input("Enter length of side:"))
                apothem=eval(input("Enter apothem length of pentagon:"))
                base_ar=float((5/2)*side*apothem)
                height=eval(input("Enter height of prism:"))
                vol=float(base_ar*height)
                print("PENTAGONAL PRISM VOLUME result=",vol,"cu.units")
            else:
                print("Your input choice is invalid.\nPlease try again.")
            
        elif ch=="e":
            print("HEXAGONAL PRISM OPERATIONS")
            print("1.REGULAR HEXAGONAL PRISM\n2.GIVEN 'APOTHEM' LENGTH OF THE HEXAGONAL PRISM")
            ch=int(input("Enter choice[1,2]:"))
            if ch==1:
                side=eval(input("Enter side length:"))
                base_ar=float({3*(math.sqrt(3))*side*side}/2)
                height=eval(input("Enter height of prism:"))
                vol=float(base_ar*height)
                print("HEXAGONAL PRISM VOLUME result=",vol,"cu.units")
            elif ch==2:
                side=eval(input("Enter length of side:"))
                apothem=eval(input("Enter apothem length of hexagon:"))
                base_ar=float(apothem*6*side*(1/2))
                height=eval(input("Enter height of prism:"))
                vol=float(base_ar*height)
                print("HEXAGONAL PRISM VOLUME result=",vol,"cu.units")
            else:
                print("Your input choice is invalid.\nPlease try again.")
                
        else:
            print("Your input choice is invalid.\nPlease try again.")

    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO FINDING LATERAL SURFACE AREAS OF 3-D SHAPES. 
def lateral_surface_area():
# HERE LATERAL SURFACE AREA CAN BE FIND OUT BY GIVING SOME DESIRED DETAILS OF THE CHOOSEN 3-D SHAPE.
    print("LATERAL SURFACE AREA OPERATIONS")
    print("1.CUBE\n2.CUBOID\n3.CONE\n4.CYLINDER\n5.SPHERE\n6.HEMISPHERE\n7.PYRAMID\n8.PRISM")
    ch=int(input("Enter choice[1,2,..,8]:"))
    
    if ch==1:
        side=eval(input("Enter side length of cube:"))
        l_sur_ar=float(4*side*side)
        print("CUBE LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==2:
        length=eval(input("Enter length of cuboid:"))
        width=eval(input("Enter width of cuboid:"))
        height=eval(input("Enter height of cuboid:"))
        l_sur_ar=float(2*(length+width)*height)
        print("CUBOID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==3:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        slant_height=eval(input("Enter slant height length:"))
        l_sur_ar=float(3.14*radius*slant_height)
        print("CONE LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==4:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        height=eval(input("Enter height length:"))
        l_sur_ar=float(2*3.14*radius*height)
        print("CYLINDER LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==5:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        l_sur_ar=float(4*3.14*radius*radius)
        print("SPHERE LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==6:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        l_sur_ar=float([3.14*radius*radius*radius]*2/3)
        print("HEMISPHERE LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
        
    elif ch==7:
        print("PYRAMID LATERAL SURFACE AREA OPERATIONS")
        print("a.SQUARE PYRAMID\nb.RECTANGULAR PYRAMID\nc.TRIANGULAR PYRAMID\nd.PENTAGONAL PYRAMID\ne.HEXAGONAL PYRAMID")
        ch=input("Enter choice[a,b,c,d,e]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            base=eval(input("Enter base length:"))
            l_sur_ar=float((2*base*side)+(base*base))
            print("SQUARE PYRAMID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="b":
            length=eval(input("Enter length of base:"))
            width=eval(input("Enter width of base:"))
            height=eval(input("Enter height of pyramid:"))
            l_sur_ar=float((length+width)*(math.sqrt([height*height]+[(length/2)*(length/2)]))+(length*width))
            print("RECTANGULAR PYRAMID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="c":
            base=eval(input("Enter base length:"))
            ht=eval(input("Enter height length:"))
            base_ar=float([base*ht]*1/2)
            a=eval(input("Enter side1 length:"))
            b=eval(input("Enter side2 length:"))
            c=eval(input("Enter side3 length:"))
            peri=float(a+b+c)
            slant_length=eval(input("Enter slant_length of pyramid:"))
            l_sur_ar=float(base_ar+{(1/2)*peri*slant_length})
            print("TRIANGULAR PYRAMID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="d":
            side=eval(input("Enter side length:"))
            apothem=eval(input("Enter apothem length:"))
            slant_height=eval(input("Enter slant height of pyramid:"))
            l_sur_ar=float({(5/2)*(side*apothem)}+{(5/2)*(side*slant_height)})
            print("PENTAGONAL PYRAMID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="e":
            side=eval(input("Enter side length:"))
            apothem=eval(input("Enter apothem length:"))
            slant_height=eval(input("Enter slant height of pyramid:"))
            l_sur_ar=float({3*(side*apothem)}+{3*(side*slant_height)})
            print("HEXAGONAL PYRAMID LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
                        
        else:
            print("Your input choice is invalid.\nPlease try again.")
    
    elif ch==8:
        print("PRISM OPERATIONS")
        print("a.SQUARE PRISM\nb.RECTANGULAR PRISM\nc.TRIANGULAR PRISM\nd.PENTAGONAL PRISM\ne.HEXAGONAL PRISM")
        ch=input("Enter choice[a,b,c,d,e]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            height=eval(input("Enter height of prism:"))
            l_sur_ar=float((4*side*height))
            print("SQUARE PRISM LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="b":
            length=eval(input("Enter length of rectangle:"))
            width=eval(input("Enter width of rectangle:"))
            height=eval(input("Enter height of prism:"))
            l_sur_ar=float(2*height*(length+width))
            print("RECTANGULAR PRISM LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="c":
            a=eval(input("Enter side1 length:"))
            b=eval(input("Enter side2 length:"))
            c=eval(input("Enter side3 length:"))
            peri=float(a+b+c)
            height=eval(input("Enter height of prism:"))
            l_sur_ar=float(peri*height)
            print("TRIANGULAR PRISM LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="d":
            apothem=eval(input("Enter apothem length:"))
            base=eval(input("Enter base length:"))
            height=eval(input("Enter height of prism:"))
            l_sur_ar=float(5*base*(apothem+height))
            print("PENTAGONAL PRISM LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
            
        elif ch=="e":
            side=eval(input("Enter base edge length:"))
            height=eval(input("Enter height of prism:"))
            l_sur_ar=float(6*side*height)
            print("HEXAGONAL PRISM LATERAL SURFACE AREA result=",l_sur_ar,"sq.units")
                
        else:
            print("Your input choice is invalid.\nPlease try again.")

    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO FINDING TOTAL SURFACE AREA OF DIFFERENT SHAPES.
def total_surface_area():
# IN THIS FUNCTION YOU CAN FIND FIND OUT THE TOTAL SURFACE AREA OF THE DIFFERENT 3-D SHAPES GIVEN
# BY PROVIDING SOME DESIRED DETAILS OF THE CHOOSEN 3-D SHAPE.
    print("TOTAL SURFACE AREA OPERATIONS")
    print("1.CUBE\n2.CUBOID\n3.CONE\n4.CYLINDER\n5.SPHERE\n6.HEMISPHERE\n7.PYRAMID\n8.PRISM")
    ch=int(input("Enter choice[1,2,..,8]:"))
    
    if ch==1:
        side=eval(input("Enter side length of cube:"))
        t_sur_ar=float(6*side*side)
        print("CUBE TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==2:
        length=eval(input("Enter length of cuboid:"))
        width=eval(input("Enter width of cuboid:"))
        height=eval(input("Enter height of cuboid:"))
        t_sur_ar=float(2*{(length*width)+(width*height)+(length*height)})
        print("CUBOID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==3:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        slant_height=eval(input("Enter slant height length:"))
        t_sur_ar=float(3.14*radius*(slant_height+radius))
        print("CONE TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==4:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        height=eval(input("Enter height length:"))
        t_sur_ar=float(2*3.14*radius*(height+radius))
        print("CYLINDER TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==5:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        t_sur_ar=float(4*3.14*radius*radius)
        print("SPHERE TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==6:
        diameter=eval(input("Enter diameter length:"))
        radius=float(diameter/2)
        t_sur_ar=float([3.14*radius*radius*radius]*2/3)
        print("HEMISPHERE TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
        
    elif ch==7:
        print("PYRAMID TOTAL SURFACE AREA OPERATIONS")
        print("a.SQUARE PYRAMID\nb.RECTANGULAR PYRAMID\nc.TRIANGULAR PYRAMID\nd.PENTAGONAL PYRAMID\ne.HEXAGONAL PYRAMID")
        ch=input("Enter choice[a,b,c,d,e]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            slant_height=eval(input("Enter slant_height length:"))
            t_sur_ar=float((side*side)+(2*side*slant_height))
            print("SQUARE PYRAMID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="b":
            length=eval(input("Enter length of base:"))
            width=eval(input("Enter width of base:"))
            height=eval(input("Enter height of pyramid:"))
            t_sur_ar=float((length+width)*(math.sqrt([height*height]+[(length/2)*(length/2)]))+(length*width))
            print("RECTANGULAR PYRAMID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="c":
            side=eval(input("Enter side of triangular base length:"))
            height=eval(input("Enter height of triangular base length:"))
            slant_height=eval(input("Enter slant_height of pyramid:"))
            t_sur_ar=float({(1/2)*(side*height)}+(3/2)*(side*slant_height))
            print("TRIANGULAR PYRAMID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="d":
            side=eval(input("Enter side length of base:"))
            apothem=eval(input("Enter apothem length of base:"))
            height=eval(input("Enter height of pyramid:"))
            t_sur_ar=float((5/2)*side*{apothem+[math.sqrt([side*side]/4)]+(height*height)})
            print("PENTAGONAL PYRAMID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="e":
            side=eval(input("Enter side length:"))
            apothem=eval(input("Enter apothem length:"))
            slant_height=eval(input("Enter slant height of pyramid:"))
            t_sur_ar=float({3*(side*apothem)}+{3*(side*slant_height)})
            print("HEXAGONAL PYRAMID TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
                        
        else:
            print("Your input choice is invalid.\nPlease try again.")
    
    elif ch==8:
        print("PRISM OPERATIONS")
        print("a.SQUARE PRISM\nb.RECTANGULAR PRISM\nc.TRIANGULAR PRISM\nd.PENTAGONAL PRISM\ne.HEXAGONAL PRISM")
        ch=input("Enter choice[a,b,c,d,e]:")
        
        if ch=="a":
            side=eval(input("Enter side length:"))
            height=eval(input("Enter height of prism:"))
            t_sur_ar=float((2*side*side)+(4*side*height))
            print("SQUARE PRISM TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="b":
            length=eval(input("Enter length of rectangle:"))
            width=eval(input("Enter width of rectangle:"))
            height=eval(input("Enter height of prism:"))
            t_sur_ar=float(2*{(length*width)+(width*height)+(length*height)})
            print("RECTANGULAR PRISM TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="c":
            a=eval(input("Enter side1 length:"))
            b=eval(input("Enter side2 length:"))
            c=eval(input("Enter side3 length:"))
            peri=float(a+b+c)
            base=eval(input("Enter base length:"))
            ht=eval(input("Enter height length:"))
            base_ar=float([base*ht]*1/2)
            height=eval(input("Enter height of prism:"))
            t_sur_ar=float((2*base_ar)+(peri*height))
            print("TRIANGULAR PRISM TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="d":
            apothem=eval(input("Enter apothem length:"))
            base=eval(input("Enter base length:"))
            height=eval(input("Enter height of prism:"))
            t_sur_ar=float(5*base*(apothem+height))
            print("PENTAGONAL PRISM TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
            
        elif ch=="e":
            side=eval(input("Enter base edge length:"))
            apothem=eval(input("Enter apothem length:"))
            height=eval(input("Enter height of prism:"))
            t_sur_ar=float(6*side*(apothem+height))
            print("HEXAGONAL PRISM TOTAL SURFACE AREA result=",t_sur_ar,"sq.units")
                
        else:
            print("Your input choice is invalid.\nPlease try again.")
    
    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO CONVERTING DIFFERENT TEMPERATURE READINGS TO OTHER TEMPERATURE MEASURING UNIT.
def temp_converter():
# HERE IN THIS FUNCTION YOU CAN CONVERT ONE GIVEN TEMPRATURE TO ANOTHER TEMPRATURE OF YOUR CHOICE
# JUST ENTER THE GIVEN TEMPRATURE AND GET THE DESIRED CONVERTED FORM OF TEMPRATURE.
    print("TEMPRATURE CONVERTION OPERATIONS")
    print("a.CELSIUS TO KELVIN\nb.KELVIN TO CELSIUS\nc.FAHRENHEIT TO CELSIUS\nd.CELSIUS TO FAHRENHEIT\ne.FAHRENHEIT TO KELVIN\nf.KELVIN TO FAHRENHEIT")
    ch=input("Enter choice[a,b,c,d,e,f]:")
        
    if ch=="a":
        cel=eval(input("Enter celsius temprature:"))
        kelvin=float(cel+273.15)
        print("CELSIUS TO KELVIN result=",kelvin)
            
    elif ch=="b":
        kel=eval(input("Enter kelvin temprature:"))
        celsius=float(kel-273.15)
        print("KELVIN TO CELSIUS result=",celsius)
            
    elif ch=="c":
        fahr=eval(input("Enter fahrenheit temprature:"))
        celsius=float((fahr-32)*(5/9))
        print("FAHRENHEIT TO CELSIUS result=",celsius)
        
    elif ch=="d":
        cel=eval(input("Enter celsius temprature:"))
        fahrenheit=float(cel*(9/5)+32)
        print("CELSIUS TO FAHRENHEIT result=",fahrenheit)
            
    elif ch=="e":
        fahr=eval(input("Enter fahrenheit temprature:"))
        kelvin=float((fahr-32)*(5/9)+273.15)
        print("FAHRENHEIT TO KELVIN result=",kelvin)
            
    elif ch=="f":
        kel=eval(input("Enter kelvin temprature:"))
        fahrenheit=float((kel-273.15)*(9/5)+32)
        print("KELVIN TO FAHRENHEIT result=",fahrenheit)
            
    else:
        print("Your input choice is invalid.\nPlease try again.")



# THIS FUNCTION WILL DO THE OPERATION RELATED TO GENERATING TABLES TO MAKE IT EASIER TO REMEMBER ALL.
def table_generator():
# SUPPOSE YOU WANT THE ENTIRE TABLE CHART URGENTLY SO YOU CAN USE THIS FUNCTION TO GET THE ENTIRE TABLE CHART OF A NUMBER.
# IF YOU ARE A STUDENT AND YOU WANT TO LEARN SOME NUMBERS TABLE CHART SO YOU CAN USE THIS IN THAT CASE.
# HERE JUST YOU HAVE TO ENTER THE NUMBER AND THEN YOU WILL GET THE ENTIRE TABLE CHART.
    num=int(input("Enter number to generate table:"))
    for i in range(1,11):
        prod=num*i
        print(num,"x",i,"=",prod)



# THIS FUNCTION WILL CONVERT DEGREE VALUE TO ITS RADIAN VALUE.
def deg_rad():
    value=float(input("enter degree value:"))
    rad= float(value*(3.14/180))
    print("DEGREE TO RADIAN result=",rad)



# THIS FUNCTION WILL CONVERT RADIAN VALUE TO DEGREE VALUE.
def rad_deg():
    value=float(input("enter radian value:"))
    deg= float(value*(180/3.14))
    print("RADIAN TO DEGREE result=",deg)



# THIS FUNCTION WILL HELP YOU WITH FINDING DIFFERENT THETA VALUE IN TRIGONOMETRY.
def theta_value():
    degree= float(input("enter the degree value:"))
    print("1.sin\n2.cos\n3.tan\n4.cot\n5.sec\n6.cosec")
    options=int(input("choice{1,2....,6}:"))
    if options== 1:
        value= float(math.sin(degree))
        print("THE VALUE OF sin","(",degree,")","IS =",value)
    elif options== 2:
        value= float(math.cos(degree))
        print("THE VALUE OF cos","(",degree,")","IS =",value)
    elif options== 3:
        value= float(math.tan(degree))
        print("THE VALUE OF tan","(",degree,")","IS =",value)
    elif options== 4:
        value= float(math.cot(degree))
        print("THE VALUE OF cot","(",degree,")","IS =",value)
    elif options== 5:
        value= float(math.sec(degree))
        print("THE VALUE OF sec","(",degree,")","IS =",value)
    elif options== 6:
        value= float(math.cosec(degree))
        print("THE VALUE OF cosec","(",degree,")","IS =",value)
    else:
        print("INVALID INPUT")



# THIS FUNCTION WILL DO THE OPERATIONS RELATED TO FINDING SPEED, TIME AND DISTANCE USING EACH OTHER VALUES.
def minor_opns():
    print("1.SPEED USING DISTANCE & TIME\n2.DISTANCE USING SPEED & TIME\n3.TIME USING SPEED & DISTANCE")
    ch=int(input("enter your choice[1,2,3]:"))
    if ch== 1:
        distance= float(input("enter distance:"))
        time= float(input("enter time period taken:"))
        speed= float(distance/time)
        print("SPEED=",speed)
    elif ch== 2:
        speed= float(input("enter speed:"))
        time= float(input("enter time period taken:"))
        distance= float(speed*time)
        print("DISTANCE=",distance)
    elif ch==3:
        distance= float(input("enter distance:"))
        speed= float(input("enter total speed:"))
        time= float(distance/speed)
        print("TIME=",time)
    else:
        print("INVALID CHOICE")



# IF YOU WANT TO CALCULATE YOUR BMI VALUE THEN THIS FUNCTION WILL HELP YOU TO FINDING OUT THE BMI VALUE.
def bmi():
    print("FOR CALCULATING YOUR BMI SOME DATAS ARE REQUIRED. SO PROCEEDING TO COLLECT DATAS................")
    weight= float(input("Enter your weight in kg :"))
    height= float(input("Enter your height in m/cm :"))
    bmi= float(weight/[height*height])
    print("Your BMI is :",bmi)



# IF YOU DON'T KNOW THE VALUES OF DIFFERENT CONSTANTS THEN NO PROBLEM THIS FUNCTION WILL HELP YOU WITH THAT TO REMEMBER ALL THOSE.
def values():
    print("HERE ARE THE LIST OF SOME CONSTANTS WHOSE VALUES ARE LISTED BELOW......")
    print("---------------------------------------------------------------------------")
    print("Planck's Constant [h] = 63.63 x 10^-34 Js = 4.136 x 10^-15 eV.s")
    print("Gravitation Constant [G] = 6.67 x 10^-11 m^3 kg^-1 s^-2")
    print("Boltzmann Constant [k] = 1.38 x 10^-23 J/K")
    print("Molar gas Constant [R] = 8.314 J/{mol.k}")
    print("Avogadro's Number [NA] = 6.023 x 10^23/mol")
    print("Charge of Electron [e] = 1.602 x 10^-19 C")
    print("Permittivity of Vaccum [|E|] = 8.85 x 10^-12 F/m")
    print("Coulomb Constant [1/4.pi.ε0] = 9 x 10^9 N m^2/ C^2")
    print("Faraday Constant [F] = 96485 C/mol")
    print("Mass of Electron [Me] = 9.1 x 10^-31 kg")
    print("Mass of Proton [Mp] = 1.6726 x 10^-27 kg")
    print("Mass of Neutron [Mn] = 1.6749 x 10^-27 kg")
    print("Stefan-Boltzmann Constant [σ] = 5.67 x 10^-8 W/{m^2.K^4}")
    print("Rydberg Constant [R∞] = 1.097 x 10^7 m^-1")
    print("Bohr Magnetron [µB] = 9.27 x 10^-24 J/T")
    print("Bohr Radius [a0] = 0.529 x 10^-10 m")
    print("Standard Atmospheric Pressure [atm] = 1.01325 x 10^5 Pa")
    print("Wien Displacement Constant [b] = 2.9 x 10^-3 mK")
    print("Wave = ∆x ∆t wave = average velocity ∆x . displacement ∆t = elapsed time")
    print("Average Velocity [Vavg] = [Vi + Vf]^2")
    print("---------------------------------------------------------------------------")



# THIS FUNCTION WILL DO THE OPERATION RELATED TO FINDING SQUARE ROOT OF A GIVEN NUMBER.
def roots():
    number = float(input("Enter a number for finding root value:"))
    root = float(math.sqrt(number))
    print("Your resultant square root of the given input number is ",root)



#--------------------------------------------------### MAIN ###----------### PROGRAM ###--------------------------------------------------
# I HAVE TRIED TO GIVE DETAILINGS IN SOME DECLARED FUNCTIONS FOR MORE EASIER CALCULATIONS.

# HERE WHATEVER FUNCTIONS I HAVE CREATED IN THE ABOVE PART OF THE PROGRAM, JUST DECLARED ALL THOSE FOR EXECUTION.

print("####----CALCULATION----OPERATIONS----####")
print("WELCOME TO THE WORLD OF CALCULATION WHERE IT MAKES YOUR LIFE EASIER.")
while True:
    print("CHOOSE ONE OF THESE WHICH YOU WANT TO DO!")
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.AVERAGE\n6.PERCENTAGE\n7.FACTORIAL")
    print("8.AREA\n9.PERIMETER\n10.VOLUME\n11.LATERAL SURFACE AREA\n12.TOTAL SURFACE AREA\n13.TEMPRATURE CONVERTER")
    print("14.TABLE GENERATOR\n15.DEGREE TO RADIAN\n16.RADIAN TO DEGREE\n17.THETA VALUE OPERATION\n18.MINOR OPERATIONS\n19.BMI CALCULATION")

    ch=int(input("Enter choice[1,2,3,......,21]:"))
    if ch==1:
        add()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==2:
        subtract()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==3:
        multiply()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==4:
        divide()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==5:
        average()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==6:
        percentage()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==7:
        factorial()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==8:
        area()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==9:
        perimeter()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==10:
        volume()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==11:
        lateral_surface_area()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==12:
        total_surface_area()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==13:
        temp_converter()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==14:
        table_generator()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==15:
        deg_rad()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==16:
        rad_deg()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==17:
        theta_value()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==18:
        minor_opns()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==19:
        bmi()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==20:
        values()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    elif ch==21:
        roots()
        print("CALCULATION SUCCESSFUL. THANK YOU......................")
    else:
        print("Your input choice is invalid.\nPlease try again.")
        
    print("DO YOU WANT TO CONTINUE FURTHER?\nIF THEN...........")    
    a=input("CHOOSE[y/n/Y/N]:")
    if a=="y" or a=="Y":
        continue
    else:
        if a=="n" or a=="N":
            break
        else:
            print("Your input choice is invalid.\nPlease try again.")
            
""" SOME POINTS TO BE NOTED """
# IF YOU HAVE CLEARLY AND PATIENCLY READ THE ENTIRE PROGRAM THEN YOU HAVE NOTICED THAT
# I HAVE CONTINUOUSLY USED "ELSE" PART IN EVERY PART OF THE PROGRAM, I MEAN
# I HAVE USED THE SAME BECAUSE I HAVE GIVEN CHOICES SO IT'S NECESSARY, NOTHING ELSE CAN BE WRITTEN
# IN PLACE OF IT.


# This program is fully made based upon my own knowledge and ideas which i got during my [11 and 12] classes beside copy pasting it from anywhere.

# ONE THING I WILL TELL THAT, JUST RUN THE PROGRAM AND SEE THE MAGIC.


#--------------------## END ##----------## OF ##----------## THE ##----------## PROJECT ##--------------------
#--------------------## MADE BY ##--------------## BIMAN SHIL ##---## (AN INTERMEDIATE) ##--------------------
