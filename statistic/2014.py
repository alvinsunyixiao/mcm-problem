import numpy as np
import matplotlib.pyplot as plt

data1_15 = [[],[]]
data2_15 = [[],[]]
data1_20 = [[],[]]
data2_20 = [[],[]]
data1_25 = [[],[]]
data2_25 = [[],[]]


data1_15[0] = [306.66, 310.46, 308.08, 312.9, 317.6, 318.52, 324.88, 326.04, 327.5, 338.76, 337.36, 336.46, 356.96, 358.04, 402.66, 407.02, 401.58, 406.5, 415.72, 413.56, 413.82, 422.84, 429.24, 439.98, 447.14, 447.02, 460.12, 457.18, 458.5, 459.68, 466.36, 473.86, 474.84, 483.28, 494.46, 495.46, 521.3, 513.76, 529.06, 520.34, 524.36, 527.32, 525.3, 530.24, 531.88, 544.56, 544.72, 549.48, 548.96, 545.5, 560.76, 556.04, 577.84, 573.3, 590.02, 593.06, 588.2, 590.72, 588.56, 603.54, 600.52]
data2_15[0] = [306.18, 314.28, 310.52, 311.04, 316.3, 323.2, 325.5, 324.72, 327.12, 337.98, 340.56, 345.2, 356.68, 351.36, 393.66, 393.5, 406.86, 407.22, 408.32, 416.82, 416.86, 430.42, 433.46, 448.08, 456.88, 444.88, 457.24, 456.76, 465.5, 471.88, 465.62, 473.74, 477.64, 488.74, 501.68, 494.78, 525.34, 520.74, 518.28, 512.7, 524.24, 530.78, 532.34, 535.7, 523.98, 538.84, 533.54, 548.68, 551.56, 554.1, 556.24, 569.3, 578.56, 584.06, 588.88, 586.56, 596.1, 600.3, 591.44, 583.66, 605.06]

data1_20[0] = [333.56, 346.74, 340.82, 349.34, 360.94, 395.9, 400.6, 409.48, 406.74, 413.44, 408.02, 416.4, 439.28, 445.8, 443.22, 437.56, 445.62, 461.84, 450.48, 470.92, 466.76, 473.96, 495.12, 490.28, 501.44, 488.94, 501.88, 503.58, 511.24, 516.44, 526.3, 533.28, 513.28, 523.06, 556.66, 535.84, 542.52, 550.8, 550.8, 547.82, 560.54, 557.38, 579.6, 574.52, 578.5, 591.16, 594.4, 574.36, 595.24, 602.36, 605.26, 615.02, 616.88, 624.08, 605.28, 629.76, 642.72, 629.9, 634.3, 650.82, 641.56]
data2_20[0] = [339.24, 341.12, 341.68, 348.46, 356.56, 388.76, 398.48, 398.96, 409.9, 411.86, 409.84, 424.76, 429.12, 438.38, 446.16, 442.96, 440.6, 455.9, 452.5, 456.76, 482.76, 481.66, 498.34, 492.42, 491.28, 502.96, 500.92, 511.54, 515.14, 513.66, 517.38, 512.6, 525.52, 529.36, 542.76, 531.6, 543.22, 539.78, 551.82, 563.68, 568.42, 556.28, 567.56, 573.24, 563.28, 572.34, 578.02, 574.9, 591.92, 605.18, 586.1, 597.44, 603.7, 602.42, 614.88, 617.12, 614.96, 616.52, 632.66, 649.68, 644.0]

data1_25[0] = [407.76, 408.78, 408.7, 412.56, 404.76, 412.66, 423.56, 438.58, 432.82, 434.18, 447.96, 452.46, 454.14, 457.16, 485.04, 475.1, 479.22, 478.38, 499.98, 484.66, 493.98, 508.78, 506.04, 502.0, 525.32, 523.42, 530.7, 528.52, 529.24, 541.68, 555.82, 544.4, 559.12, 546.26, 565.82, 554.44, 566.56, 570.82, 579.82, 590.62, 595.94, 596.16, 608.42, 595.44, 588.58, 607.12, 607.86, 600.92, 620.54, 612.98, 647.44, 625.5, 644.2, 637.74, 646.38, 660.82, 671.82, 666.6, 682.06, 673.32, 685.5]
data2_25[0] = [404.06, 407.04, 405.28, 422.6, 411.04, 417.92, 426.14, 431.02, 432.86, 445.08, 445.06, 454.22, 452.62, 460.12, 484.24, 479.68, 479.14, 477.02, 486.5, 494.14, 492.54, 498.24, 502.24, 519.06, 512.92, 524.38, 523.18, 515.36, 538.76, 537.86, 534.88, 544.32, 561.58, 572.22, 556.54, 567.32, 559.94, 563.74, 555.96, 580.6, 589.84, 609.28, 601.44, 611.24, 613.02, 616.34, 606.52, 606.86, 620.44, 641.42, 628.74, 628.98, 641.38, 644.02, 634.38, 652.88, 652.36, 659.46, 677.86, 666.0, 682.58]

data1_15[1] = [11.14, 11.9, 12.06, 11.84, 12.3, 12.44, 14.5, 13.6, 14.42, 15.52, 15.2, 15.88, 17.84, 16.9, 31.92, 33.14, 32.68, 32.36, 33.98, 33.8, 35.0, 36.64, 36.56, 44.44, 50.64, 49.7, 52.8, 53.6, 50.82, 52.14, 54.94, 55.36, 55.86, 62.88, 62.42, 69.1, 89.82, 88.7, 93.92, 89.62, 93.16, 92.18, 93.74, 92.38, 94.4, 92.62, 99.2, 97.68, 101.18, 100.18, 104.12, 114.24, 122.92, 128.0, 132.4, 134.76, 129.88, 132.32, 148.0, 148.3, 150.82]
data2_15[1] = [11.78, 11.78, 12.42, 13.4, 13.44, 14.18, 14.78, 13.08, 15.42, 15.8, 15.26, 14.38, 18.9, 19.62, 31.36, 32.24, 32.24, 31.22, 34.0, 33.0, 37.94, 38.28, 37.52, 45.18, 52.6, 51.06, 51.84, 52.36, 54.72, 55.5, 53.72, 53.7, 54.16, 65.02, 66.92, 65.18, 91.66, 89.58, 88.66, 91.54, 91.32, 91.26, 92.26, 94.06, 92.92, 94.2, 94.54, 99.14, 99.18, 103.76, 102.3, 115.3, 123.32, 125.1, 128.4, 130.54, 130.4, 133.06, 150.48, 143.16, 152.56]

data1_20[1] = [16.54, 16.76, 15.7, 17.6, 24.0, 39.02, 40.1, 39.88, 40.4, 41.88, 43.6, 44.84, 53.98, 64.78, 62.38, 61.34, 60.96, 65.0, 63.2, 69.32, 70.48, 76.1, 100.54, 102.44, 101.48, 100.36, 99.58, 100.74, 103.5, 101.42, 108.98, 108.7, 110.48, 119.76, 134.96, 131.98, 137.58, 141.88, 138.92, 158.72, 160.46, 160.46, 167.7, 160.82, 166.72, 169.44, 169.44, 166.7, 172.44, 178.48, 176.66, 185.04, 193.68, 193.46, 196.24, 212.74, 223.54, 219.96, 218.16, 224.38, 222.16]
data2_20[1] = [16.36, 16.3, 18.18, 18.58, 22.56, 39.84, 40.4, 38.46, 41.36, 41.46, 39.88, 47.18, 53.12, 59.5, 59.52, 59.52, 59.42, 62.58, 64.26, 66.38, 76.62, 78.2, 100.62, 100.84, 97.1, 102.46, 99.84, 102.88, 101.82, 102.96, 104.4, 108.84, 110.1, 121.0, 132.88, 127.34, 136.32, 135.56, 140.8, 164.84, 160.96, 163.24, 164.84, 165.2, 157.6, 166.32, 166.04, 165.98, 173.28, 178.2, 172.28, 177.0, 189.28, 182.62, 194.58, 208.56, 213.42, 211.64, 214.64, 229.88, 225.74]

data1_25[1] = [48.6, 45.9, 51.14, 49.6, 50.18, 54.62, 67.5, 70.96, 74.22, 68.34, 72.94, 73.42, 76.28, 84.84, 113.92, 112.5, 109.34, 112.16, 114.72, 111.96, 112.06, 118.14, 122.92, 126.2, 145.64, 152.72, 152.34, 170.64, 168.54, 170.72, 177.16, 172.02, 176.1, 174.22, 178.14, 176.46, 185.04, 186.92, 195.18, 205.46, 217.88, 220.4, 227.96, 223.2, 215.0, 227.72, 225.2, 223.26, 225.22, 230.0, 249.02, 240.02, 251.06, 244.06, 254.14, 272.56, 277.06, 273.54, 284.02, 282.08, 288.36]
data2_25[1] = [48.88, 49.36, 49.42, 50.08, 53.7, 55.54, 72.18, 73.0, 68.86, 74.76, 73.74, 74.68, 69.74, 83.46, 111.84, 112.12, 112.5, 113.32, 111.9, 116.72, 113.8, 121.1, 121.9, 132.24, 138.82, 147.06, 148.46, 166.32, 170.0, 172.28, 166.1, 174.16, 178.28, 187.22, 179.04, 181.44, 183.88, 185.52, 185.72, 203.58, 215.8, 227.18, 225.76, 231.56, 228.58, 228.46, 227.56, 220.18, 233.78, 247.94, 237.32, 240.7, 243.84, 248.9, 255.84, 267.62, 264.64, 272.18, 287.7, 279.76, 284.32]

data_15 = [[],[]]
data_20 = [[],[]]
data_25 = [[],[]]

for i in range(2):
    data1_15[i] = np.array(data1_15[i])
    data2_15[i] = np.array(data2_15[i])
    data1_20[i] = np.array(data1_20[i])
    data2_20[i] = np.array(data2_20[i])
    data1_25[i] = np.array(data1_25[i])
    data2_25[i] = np.array(data2_25[i])

    data_15[i] = (data1_15[i]+data2_15[i])/2
    data_20[i] = (data1_20[i]+data2_20[i])/2
    data_25[i] = (data1_25[i]+data2_25[i])/2



x = [0.2, 0.21000000000000002, 0.22000000000000003, 0.23000000000000004, 0.24000000000000005, 0.25000000000000006, 0.26000000000000006, 0.2700000000000001, 0.2800000000000001, 0.2900000000000001, 0.3000000000000001, 0.3100000000000001, 0.3200000000000001, 0.3300000000000001, 0.34000000000000014, 0.35000000000000014, 0.36000000000000015, 0.37000000000000016, 0.38000000000000017, 0.3900000000000002, 0.4000000000000002, 0.4100000000000002, 0.4200000000000002, 0.4300000000000002, 0.4400000000000002, 0.45000000000000023, 0.46000000000000024, 0.47000000000000025, 0.48000000000000026, 0.49000000000000027, 0.5000000000000002, 0.5100000000000002, 0.5200000000000002, 0.5300000000000002, 0.5400000000000003, 0.5500000000000003, 0.5600000000000003, 0.5700000000000003, 0.5800000000000003, 0.5900000000000003, 0.6000000000000003, 0.6100000000000003, 0.6200000000000003, 0.6300000000000003, 0.6400000000000003, 0.6500000000000004, 0.6600000000000004, 0.6700000000000004, 0.6800000000000004, 0.6900000000000004, 0.7000000000000004, 0.7100000000000004, 0.7200000000000004, 0.7300000000000004, 0.7400000000000004, 0.7500000000000004, 0.7600000000000005, 0.7700000000000005, 0.7800000000000005, 0.7900000000000005, 0.8]
'''
plt.plot(x,data_15[0],color='red')
plt.plot(x,data_20[0],color='green')
plt.plot(x,data_25[0],color='blue')
'''
plt.plot(x,data_15[1],color='red',linestyle='-')
plt.plot(x,data_20[1],color='green',linestyle='-')
plt.plot(x,data_25[1],color='blue',linestyle='-')
plt.show()