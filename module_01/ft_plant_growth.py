class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def ft_get_info():
## a finir : get info de quoi ???

## a finir : utiliser get info
def ft_growth(plantname: str):
    count = 1
    print("=== Day", count, "===")
    print(plantname.name+": ", plantname.height,"cm, ",plantname.age," days old", sep="")
    for count in range(1,9):
        plantname.height += 1
        plantname.age += 1
    print("=== Day", count, "===")
    print(plantname.name+": ", plantname.height,"cm, ",plantname.age," days old", sep="")
    print("Growth this week: +", count,"cm", sep="")

def main():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    plantname = ft_get_info("Rose")
    ft_growth(plantname)

if __name__=="__main__":
    main()