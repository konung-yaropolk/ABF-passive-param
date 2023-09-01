# Parameters:

FIGURE_W = 4  # widtn in inches
FIGURE_H = 4  # Height in inches

X_TICKS = 'sweeps'    # time or sweeps on X axis

SHOW_STATS = False
SHOW_GRAPH = False
SAVE_GRAPH = True
SAVE_FORMAT = 'png'   # png, svg, pdf, eps

DIRECTORY = 'D:/Lab Work Files/Patch-clamp data'    # full path to directory with files, leave empty if you run this script in it

FILES_LIST = [
    
# Список імен abf файлів без росширення, в лапках, розділені комами; номер трейсу для нарізки (починаючи з нульового)




# # MCU Project:
# 
# # 2M Ca:
# 
# ['/MCU_Project_Yariks_data/2021_04_15/2021_04_15_0000_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_19/2021_04_19_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M1/2021_04_20_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M1/2021_04_20_0002_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_20_M2/2021_04_20_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0010_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0018_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0024_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0025_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0000_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0018_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_23/2021_04_23_0019_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_25/2021_04_25_0015_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0006_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0022_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0025_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0027_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_26/2021_04_26_0028_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_30/2021_04_30_0013_baselined.abf', 11],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0001_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_04/2021_05_04_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_06/2021_05_06_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_06/2021_05_06_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0000_baselined.abf', 15],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0004_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_07/2021_05_07_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M1/2021_05_10_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0029_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0031_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0034_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0038_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0043_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_10_0045_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_10_M2/2021_05_11_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0030_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0032_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0049_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0051_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0055_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0062_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0064_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0069_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0071_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0002_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0005_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0019_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0025_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0027_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0032_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0034_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0038_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0042_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0046_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_12_0052_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_12/2021_05_13_0023_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0038_baselined.abf', 11],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0046_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0053_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_13/2021_05_13_0055_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0002_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0015_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_14/2021_05_14_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0015_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0026_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0037_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0039_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0053_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0054_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_19_0057_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_19/2021_05_20_0000_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0023_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0024_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0030_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_20_M2/2021_05_20_0031_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0009_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_27/2021_05_27_0025_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0019_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0031_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0033_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0034_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0039_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0042_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0046_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0026_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0028_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_05_31/2021_05_31_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_31/2021_05_31_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_01_M2/2021_06_01_0018_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0019_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0027_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0033_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0034_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0038_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0039_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0048_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0050_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0057_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0058_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0029_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0034_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0035_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0002_baselined.abf', 11],
# ['/MCU_Project_Yariks_data/2021_06_04/2021_06_04_0011_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0015_baselined.abf', 17],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0025_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0026_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0030_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0033_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0037_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0040_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0041_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0001_baselined.abf', 7],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0018_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0027_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0037_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0043_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0044_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0057_baselined.abf', 11],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0062_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0065_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0071_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0072_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0075_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_11/2021_05_11_0075_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_04_22/2021_04_22_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0040_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0041_baselined.abf', 12],
# 
# 
# 
#
# # 1M Ca:
# 
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0025_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_05_28/2021_05_28_0036_baselined.abf', 9],
# ['/MCU_Project_Yariks_data/2021_05_29/2021_05_29_0029_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0030_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0031_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0052_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0053_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0059_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_02_0060_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0015_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_02/2021_06_03_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_03_0037_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_03/2021_06_04_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_05_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_05_M2/2021_06_06_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0023_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0035_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_07_0043_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0000_baselined.abf', 14],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0015_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0030_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0031_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0039_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0040_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0046_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_07/2021_06_08_0047_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2021_06_08/2021_06_08_0077_baselined.abf', 12],
# 
# 
# 
# 
# # 2M & 1M in 2022:
# 
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0004_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0005_baselined.abf', 9],
# ['/MCU_Project_Yariks_data/2022_09_14/2022_09_14_0006_baselined.abf', 13],
# 
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0002_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0008_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0012_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_19/2022_09_19_0022_baselined.abf', 12],
# 
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0002_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0005_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0011_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0015_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0023_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0033_baselined.abf', 13],
# ['/MCU_Project_Yariks_data/2022_09_20/2022_09_20_0034_baselined.abf', 13],
# 
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0005_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_21/2022_09_21_0007_baselined.abf', 12],
# 
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0007_baselined.abf', 4],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_22/2022_09_22_0021_baselined.abf', 4],
# 
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0001_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0006_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0007_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0014_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0015_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0020_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0021_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0026_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0028_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0032_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0033_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_29_0036_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0000_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0003_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0004_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0009_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0010_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0013_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0016_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0017_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0023_baselined.abf', 12],
# ['/MCU_Project_Yariks_data/2022_09_29/2022_09_30_0024_baselined.abf', 12],
#
#
#
#
# # 2M & 1M & 4M in 2023:
#
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0008.abf', 14],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0014.abf', 22],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0018.abf', 23],
# ['/MCU_Project_Yariks_data/2023_02_08/2023_02_08_0019.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0006.abf', 22],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2023_02_16/2023_02_16_0012.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_04_07/2023_04_07_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_07/2023_04_07_0007.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0003.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_10/2023_04_10_0007.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0003.abf', 22],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0004.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_20/2023_04_20_0010.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0001.abf', 18],
# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_04_27/2023_04_27_0024.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0012.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0013.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0014.abf', 23],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0015.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0022.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_03/2023_05_03_0024.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0001.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0002.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0003.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_05/2023_05_05_0004.abf', 12],
#
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0001.abf', 14],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0002.abf', 17],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0006.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0007.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0008.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0009.abf', 11],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0017.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0018.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0019.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0024.abf', 14],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0026.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0027.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0028.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0029.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0033.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0034.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0035.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0036.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0043.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0044.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0045.abf', 30],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0046.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0048.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0049.abf', 13],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0050.abf', 23],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0051.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0055.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0057.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0058.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_08_0059.abf', 25],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0000.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0005.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0006.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0007.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_08/2023_05_09_0008.abf', 13],
#
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0007.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0008.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0009.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0010.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0015.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0016.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0018.abf', 12],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0019.abf', 6],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0020.abf', 22],
# ['/MCU_Project_Yariks_data/2023_05_10/2023_05_10_0021.abf', 12],





]
