import math


Height = float(input("Enter your height in cms: \n"))
Weight = float(input("Enter your weight in kgs: \n"))
Height = Height/100

BMI = Weight/(Height*Height)

print("Your BMI is", BMI)

if(BMI<18.5):
    print("Underweight")
    print("Follow the below diet plan")
    print('''7 a.m. – 8 a.m.	Overnight soaked almonds (6-7 pieces)''')
    print('''Breakfast	8 a.m. – 9 a.m.\n
    2 multigrain breads with low-fat butter and egg omelet (2 egg whites from 1 whole egg).
    Or
    A cup of corn flakes, oats with milk, or any cereal porridge (use full-fat milk).
    Or
    Poha, upma, or daliya khichdi with lots of veggies.
    Or
    2 chapatis with a cup of veggies and a cup of boiled sprouts
    Or
    2 protein (Cottage cheese/sprouts) stuffed parathas with chutney or pickles.
    Whole fruits or a glass of fresh vegetable juice with pulp.''')
    print('''
    After Breakfast	11 a.m. – 12 p.m.	
    A glass of full fat milk with a health drink of your choice or whey protein.''')
    print('''
    Lunch	1:30 p.m. – 2:30 p.m.	
    A small cup of rice and two chapatis.
    A cup of pulses (masoor, moong, chana).
    ½ cup of vegetable curry.
    3 oz chicken breast or a piece of fish/ eggs/ tofu/cottage cheese.
    Mixed salad made of cucumber, carrot, and tomatoes.
    A small cup of curd or yogurt.''')
    print('''
    Evening snack	5:30 p.m. – 6:30 p.m.	
    Veg sandwich with cheese.
    Or
    Baked potato with skin and avocado dip.
    Or
    Fistful mixture of roasted nuts.''')
    print('''
    Dinner	8:30 p.m. – 9:30 p.m.	
    ½ cup of brown rice and 1 cup of kidney beans/black beans/ mushroom curry.
    Mixed salad made of cucumber, carrot, and tomatoes.
    Before bed	10:30 p.m. – 11 p.m.	
    A glass of full fat milk.''')

elif(BMI>=18.5 and BMI<=24.9):
    print("Normal weight")
    print("Maintain your present diet and stay fit")

elif(BMI>24.9 and BMI<=29.9):
    print("Pre-obesity")
    print("7 a.m. Lemon juice in warm water; a tiny piece of raw ginger(To be chewed) ")
    print('''8 a.m. Breakfast made fresh with high-fibre cereals like oats 
    and bajra, topped by a spoonful of ground flax seed; a glass
    of milk or a bowl of curd; one fruit, e.g. diced papaya.''')
    print("10.30 a.m. About half a dozen almonds and some walnuts.")
    print('''1pm: A bowl of salad with olive oil drizzled on it; a small
    bowl of brown rice with stir-fried vegetables; one roti with daal.''')
    print('''3pm: A glass of chaas and a banana.\n
    5pm: A cup of green tea, and two multigrain biscuits.''') 
    print('''7pm: A small bowl of sprouts, or a very small helping of dry fruits.
    8pm: A bowl of daal, a few cubes of cottage cheese, two rotis, sauteed vegetables.
    10pm: A small glass of warm milk.''')


elif(BMI>29.9 and BMI<=34.9):
    print("Obesity class 1")
    print("7 a.m. Lemon juice in warm water; a tiny piece of raw ginger(To be chewed) ")
    print('''8 a.m. Breakfast made fresh with high-fibre cereals like oats 
    and bajra, topped by a spoonful of ground flax seed; a glass
    of milk or a bowl of curd; one fruit, e.g. diced papaya.''')
    print("10.30 a.m. About half a dozen almonds and some walnuts.")
    print('''1pm: A bowl of salad with olive oil drizzled on it; a small
    bowl of brown rice with stir-fried vegetables; one roti with daal.''')
    print('''3pm: A glass of chaas and a banana.\n
    5pm: A cup of green tea, and two multigrain biscuits.''') 
    print('''7pm: A small bowl of sprouts, or a very small helping of dry fruits.
    8pm: A bowl of daal, a few cubes of cottage cheese, two rotis, sauteed vegetables.
    10pm: A small glass of warm milk.''')

elif(BMI>34.9 and BMI<=39.9):
    print("Obesity class 2")
    print("7 a.m. Lemon juice in warm water; a tiny piece of raw ginger(To be chewed) ")
    print('''8 a.m. Breakfast made fresh with high-fibre cereals like oats 
    and bajra, topped by a spoonful of ground flax seed; a glass
    of milk or a bowl of curd; one fruit, e.g. diced papaya.''')
    print("10.30 a.m. About half a dozen almonds and some walnuts.")
    print('''1pm: A bowl of salad with olive oil drizzled on it; a small
    bowl of brown rice with stir-fried vegetables; one roti with daal.''')
    print('''3pm: A glass of chaas and a banana.\n
    5pm: A cup of green tea, and two multigrain biscuits.''') 
    print('''7pm: A small bowl of sprouts, or a very small helping of dry fruits.
    8pm: A bowl of daal, a few cubes of cottage cheese, two rotis, sauteed vegetables.
    10pm: A small glass of warm milk.''')

else:
    print("Obesity class 3")
    print("7 a.m. Lemon juice in warm water; a tiny piece of raw ginger(To be chewed) ")
    print('''8 a.m. Breakfast made fresh with high-fibre cereals like oats 
    and bajra, topped by a spoonful of ground flax seed; a glass
    of milk or a bowl of curd; one fruit, e.g. diced papaya.''')
    print("10.30 a.m. About half a dozen almonds and some walnuts.")
    print('''1pm: A bowl of salad with olive oil drizzled on it; a small
    bowl of brown rice with stir-fried vegetables; one roti with daal.''')
    print('''3pm: A glass of chaas and a banana.\n
    5pm: A cup of green tea, and two multigrain biscuits.''') 
    print('''7pm: A small bowl of sprouts, or a very small helping of dry fruits.
    8pm: A bowl of daal, a few cubes of cottage cheese, two rotis, sauteed vegetables.
    10pm: A small glass of warm milk.''')

x= print('''Do you want to calculate your body fat percentage if yes type 1 if no type 0''')
y=int(input("Your ans: \n"))
if(y==1):
    Age=int(input("Enter your age: \n"))
    BFP=(1.20 * BMI) + (0.23 * Age) - (math.log(10853519.8991,math.e))
    print("Your body fat percentage is ",BFP,"%")
elif(y==0):
    print("Try and go using the proper and periodic plan")

else:
    print("Only 0 and 1 accepted")









