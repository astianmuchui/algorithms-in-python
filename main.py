#grading system algorithm
math = 80
eng = 90
swahili = 90
chem = 90
phy = 70
geography = 50
aviation = 60
bio = 92
total = math+eng+swahili+chem+phy+geography+aviation+bio
mean = total/8
print(mean)
#Define grades

def grade():
    print("")    
aggregate = mean
if aggregate <= 34: 
    print("E")
if aggregate>=35 and aggregate<=39 :
    print("D-")
if aggregate>=40 and aggregate<=44:
    print("D (plain)")
if aggregate>=45 and aggregate<=49:
    print("D +")
if aggregate >= 50 and aggregate<=54:
    print("C -")
if aggregate >= 55 and aggregate<=59:
    print("C")
if aggregate >= 60 and aggregate<=64:
    print("C+")
if aggregate>= 65 and aggregate<=69:
    print("B-")
if aggregate>=70 and aggregate<=74:
    print("B (Plain)")
if aggregate>=75 and aggregate<=79:
    print("B +")
if aggregate>=80 and aggregate<=84:
    print("A-")
if aggregate> 85 :
    print("A")                    

grade()