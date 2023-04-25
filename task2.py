# В первом ящике находится 8 мячей, из которых 5 - белые. 
# Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

import formulae as f
# удачные варианты: 1) 2б + 1б 3ч 2) 1б 1ч + 2б 2 ч 3) 2ч + 3б 1ч
p1 = f.combinations(5,2) * f.combinations(5,1) * f.combinations(7,3)
p2 = f.combinations(5,1) * f.combinations(3,1) * f.combinations(5,2) * f.combinations(7,2)
p3 = f.combinations(3,2) * f.combinations(5,3) * f.combinations(7,1)
p_positive = p1 + p2 + p3

#все варианты достать мячи
p_all = f.combinations(8,2)*f.combinations(12,4)

#высчитываем вероятность положительных результатов
print(p_positive/p_all) # 0.3687