from random import choice
class Tank:
    def __init__(self,name,ammo,durability,damage) -> None:
        self.name = name
        self.ammo = ammo
        self.durability = durability
        self.damage = damage
        pass
  
tanks = []
choices = ["Attack","Dodge"]
for _ in range(2): 
    input_tank = input("ชื่อ กระสุน ความคงทน ดาเมจ (เว้นวรรค): ").split()
    input_name = input_tank[0]
    input_ammo = int(input_tank[1]) 
    input_durability = int(input_tank[2])  
    input_damage = int(input_tank[3])  
    tanks.append(Tank(input_name, input_ammo, input_durability, input_damage))

tank1 ,tank2 = tanks

P1 = choice([tank1, tank2])
P2 = tank2 if P1 == tank1 else tank1
print(f"{P1.name} เริ่มก่อน")

while tank1.durability > 0 and tank2.durability > 0:
    for i in range(len(choices)):
            print(f"{i+1})"+ choices[i])
    round = int(input("Select your choices(0 to exit):"))
    if round == 0 :
        break

    if round == 1:
        print(f"{P1.name} ยิง {P2.name}")
        P2.durability -= P1.damage
        P1.ammo -= 1
        print(f"{P2.name} ความคงทนเหลือ {P2.durability}",)
    else:
        P2.durability += 2
        print(f"{P2.name} ความคงทนเหลือ {P2.durability}",)
    P1, P2 = P2, P1

if tank1.durability > tank2.durability:
    print(f"{tank1.name} ชนะเกม!")
elif tank1.durability == tank2.durability:
    print(f"เสมอ!!")
else:
    print(f"{tank2.name} ชนะเกม!")