import matplotlib.pyplot as plt
data_15 = [11.33, 11.23, 11.19, 11.09, 11.47, 11.32, 11.13, 11.35, 11.07, 11.43, 11.04, 11.02, 11.54, 11.61, 12.83, 13.02, 12.5, 12.27, 12.49, 12.89, 12.6, 12.96, 13.0, 13.16, 14.03, 13.78, 13.42, 13.88, 13.7, 13.57, 13.66, 14.15, 13.86, 14.1, 14.28, 14.78, 15.37, 15.57, 14.91, 15.44, 15.54, 15.56, 15.32, 15.0, 15.48, 15.55, 15.79, 15.25, 15.32, 15.44, 15.78, 16.1, 16.5, 16.94, 16.73, 16.53, 16.65, 16.87, 17.16, 17.37, 17.01]
data_20 = [11.28, 11.85, 11.63, 11.86, 12.0, 13.04, 13.23, 13.23, 12.91, 13.28, 13.19, 13.28, 13.82, 14.17, 14.16, 13.49, 14.16, 14.16, 14.35, 13.77, 14.78, 14.33, 15.46, 15.67, 15.65, 15.77, 15.61, 15.32, 15.3, 15.85, 15.38, 15.9, 15.8, 16.38, 16.81, 16.91, 16.74, 16.75, 16.68, 17.35, 17.48, 17.18, 17.34, 17.65, 17.35, 17.41, 17.39, 17.48, 17.56, 17.32, 17.56, 18.16, 17.67, 17.94, 18.2, 18.67, 18.72, 18.57, 18.74, 18.33, 18.55]
data_25 = [13.78, 13.55, 13.56, 13.94, 13.65, 13.66, 14.41, 14.13, 14.33, 14.33, 14.22, 14.46, 14.58, 14.64, 15.69, 15.77, 16.27, 16.09, 15.78, 15.92, 16.05, 16.08, 15.97, 16.54, 16.69, 17.04, 16.79, 17.63, 17.5, 17.63, 17.56, 17.67, 17.58, 17.43, 17.67, 17.77, 17.88, 17.57, 17.98, 17.92, 18.68, 18.54, 18.82, 18.57, 18.38, 18.71, 18.56, 18.89, 18.69, 18.77, 18.86, 18.82, 19.11, 18.96, 19.24, 19.26, 19.31, 19.43, 19.49, 19.39, 19.24]
explosiveness = [0.2, 0.21000000000000002, 0.22000000000000003, 0.23000000000000004, 0.24000000000000005, 0.25000000000000006, 0.26000000000000006, 0.2700000000000001, 0.2800000000000001, 0.2900000000000001, 0.3000000000000001, 0.3100000000000001, 0.3200000000000001, 0.3300000000000001, 0.34000000000000014, 0.35000000000000014, 0.36000000000000015, 0.37000000000000016, 0.38000000000000017, 0.3900000000000002, 0.4000000000000002, 0.4100000000000002, 0.4200000000000002, 0.4300000000000002, 0.4400000000000002, 0.45000000000000023, 0.46000000000000024, 0.47000000000000025, 0.48000000000000026, 0.49000000000000027, 0.5000000000000002, 0.5100000000000002, 0.5200000000000002, 0.5300000000000002, 0.5400000000000003, 0.5500000000000003, 0.5600000000000003, 0.5700000000000003, 0.5800000000000003, 0.5900000000000003, 0.6000000000000003, 0.6100000000000003, 0.6200000000000003, 0.6300000000000003, 0.6400000000000003, 0.6500000000000004, 0.6600000000000004, 0.6700000000000004, 0.6800000000000004, 0.6900000000000004, 0.7000000000000004, 0.7100000000000004, 0.7200000000000004, 0.7300000000000004, 0.7400000000000004, 0.7500000000000004, 0.7600000000000005, 0.7700000000000005, 0.7800000000000005, 0.7900000000000005, 0.8000000000000005]
plt.plot(explosiveness,data_15)
plt.plot(explosiveness,data_20)
plt.plot(explosiveness,data_25)
plt.show()


