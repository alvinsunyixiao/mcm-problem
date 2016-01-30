import matplotlib.pyplot as plt

x = []
b = 0.1
while b<4.01:
    x.append(b)
    b += 0.01
for ele in x:
    if (ele<1.01 and ele>=1.0) or (ele<2.01 and ele>=2.0) or (ele<3.01 and ele>=3.0):
        x.remove(ele)

data = [40, 49, 48, 52, 55, 58, 81, 80, 55, 76, 81, 96, 85, 79, 90, 87, 87, 112, 107, 105, 114, 105, 108, 104, 107, 115, 117, 118, 111, 118, 104, 120, 131, 136, 123, 117, 102, 115, 122, 160, 123, 114, 135, 134, 123, 143, 147, 142, 150, 138, 144, 144, 145, 147, 154, 140, 153, 144, 125, 143, 122, 136, 126, 139, 136, 165, 155, 152, 140, 153, 131, 153, 148, 156, 148, 156, 173, 158, 106, 141, 181, 188, 152, 143, 165, 169, 158, 148, 131, 155]+[145, 164, 144, 149, 149, 149, 177, 160, 131, 170, 173, 168, 162, 176, 153, 178, 156, 156, 166, 168, 145, 151, 137, 158, 155, 163, 147, 143, 142, 165, 148, 177, 158, 137, 147, 159, 135, 151, 167, 141, 146, 164, 178, 172, 131, 147, 138, 165, 177, 130, 138, 167, 146, 143, 179, 170, 175, 157, 135, 168, 166, 169, 134, 157, 149, 177, 200, 165, 149, 183, 187, 161, 164, 144, 148, 163, 136, 168, 155, 139, 152, 160, 147, 141, 190, 182, 168, 152, 158, 190, 154, 171, 163, 189, 159, 180, 175, 151, 143]+[152, 171, 157, 148, 169, 149, 173, 145, 165, 168, 147, 142, 148, 172, 194, 161, 164, 146, 126, 153, 133, 162, 156, 150, 171, 163, 154, 141, 150, 166, 165, 191, 137, 171, 164, 189, 182, 175, 162, 147, 162, 165, 147, 158, 187, 161, 184, 150, 177, 153, 190, 136, 163, 153, 158, 177, 162, 171, 147, 156, 129, 160, 161, 163, 176, 164, 168, 129, 156, 169, 133, 159, 155, 175, 152, 167, 153, 166, 178, 161, 176, 142, 148, 192, 162, 164, 189, 151, 155, 186, 176, 158, 173, 172, 188, 168, 168, 148, 200, 212]+[166, 159, 154, 177, 199, 168, 173, 179, 151, 172, 138, 165, 171, 153, 166, 122, 164, 182, 150, 162, 169, 169, 157, 202, 174, 179, 158, 163, 156, 157, 159, 158, 143, 158, 167, 174, 152, 166, 153, 148, 183, 162, 131, 156, 154, 155, 163, 161, 186, 147, 136, 139, 140, 181, 157, 157, 152, 141, 159, 135, 153, 170, 166, 181, 151, 144, 163, 148, 165, 170, 135, 168, 164, 148, 180, 186, 173, 159, 178, 158, 162, 167, 177, 160, 162, 160, 200, 164, 153, 168, 156, 141, 135, 162, 171, 162, 180, 155, 153, 160]
print len(x),len(data)
plt.plot(x,data)
plt.show()
