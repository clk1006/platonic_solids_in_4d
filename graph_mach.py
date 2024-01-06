
from math import *
import random 
import numpy as np
from matplotlib import pyplot as plt #für die graphiken
import time

# x Werte und eine Liste, die zu jeden x-Werte eine Liste der y-Werte enthällt
def graph_off(x, y_werte, vergleich = False):
    y_listen = []
    Summe = []
    for i in range(len(y_werte[0])):
        y_listen += [[]]
        for j in y_werte:
            y_listen[i] += [j[i]]
            if i == 0:
                Summe += [sum(j)]
    #print(x,y_listen)

    #Das Bild
    plt.figure(figsize=(12,8))

    farben = [ 'dimgray' , 'silver', 'lightcoral', 'firebrick', 'darkred' ,'red', 'orangered' , 'darkorange', 'gold', 'yellow' , 'yellowgreen' , 'limegreen', 'forestgreen' , 'darkgreen' , 'teal' , 'royalblue' , 'navy' , 'indigo']

    for y in range(len(y_listen)):
        plt.plot(x,y_listen[y], label = "Bereich " + str(y+1) , color = farben[y])

    if vergleich:

        berg_summe = []
        x = np.linspace(0,2*pi,200)
        for i in range(len(y_listen[3])):
            berg_summe.append(y_listen[2][i] + y_listen[3][i])
        plt.plot(x, berg_summe, color= 'green')

        x = np.linspace(0,pi,100)
        vergleich_aufwärts = []
        vergleich_abwärts = []
        vergleich_hügel = []
        vergleich_ungleicher_hügel = []

        for i in x:
            a = acos(cos(i)**2)
            vergleich_aufwärts.append(100_000/(4*pi)* (2*i - a)  ) # ( a + 2*(pi/2-i))) # = pi + a - 2*i 
            vergleich_abwärts.append(100_000/(4*pi)* (2*pi -2*i -a))
            vergleich_hügel.append(100_000/(4*pi)*a)
            vergleich_ungleicher_hügel.append(100_000/(4*pi)*(1/2*a + 2/(pi**2)*sin(2*i)))

        plt.plot(x, vergleich_aufwärts , label = 'Vergleich', color = 'black') 
        plt.plot(x, vergleich_abwärts , color = 'black')  
        plt.plot(x, vergleich_hügel , color = 'black') 
        plt.plot(x, vergleich_ungleicher_hügel , color = 'red')

           

         
    
    #plt.plot(x, Summe , label = "Summe" , color = 'black')
    plt.xlabel('Winkel')
    plt.ylabel('Punkte')
    #plt.ylim(10,-10)
    plt.legend()
    plt.savefig('el_20240106_07_01.png')
    plt.show()

def graph_vergleich(x, y_werte):
    y_listen = []
    Summe = []
    for i in range(len(y_werte[0])):
        y_listen += [[]]
        for j in y_werte:
            y_listen[i] += [j[i]]
            if i == 0:
                Summe += [sum(j)]
    #print(x,y_listen)

    #Das Bild
    plt.figure(figsize=(12,8))
    farben = [ 'dimgray' , 'silver', 'lightcoral', 'firebrick', 'darkred' ,'red', 'orangered' , 'darkorange', 'gold', 'yellow' , 'yellowgreen' , 'limegreen', 'forestgreen' , 'darkgreen' , 'teal' , 'royalblue' , 'navy' , 'indigo']

    x = np.linspace(0,pi,100)

    fehler = []
    sinus = []
    sin_arccos = []
    mittelwert = []
    random_idee = []
    for i in range(len(y_listen[1])):
        a = acos(cos(x[i])**2)
        fehler.append(y_listen[1][i] - 100_000/(4*pi)*a/2)
        sinus.append(100_000/(4*pi)*((2/pi)**2)*asin(sin(x[i])*cos(x[i])))
        random_idee.append(100_000/(1/2*pi**2)*(1/(4*pi))*(sin(acos(sin(x[i]-pi/2))*2 + pi)))
        
    x_2 = np.linspace(0,pi/2,100)    
    for i in range(len(x_2)):    
        sin_arccos.append(100_000/(1/2*pi**2) *(1/(4*pi))* (sin(acos(x_2[i]*2/pi)*2)))
        mittelwert.append(100_000/(1/2*pi**2) *(1/(4*pi))* (1/3* sin(acos(x_2[i]*2/pi)*2)) + 2/3* 100_000/(4*pi)*((2/pi)**2)*asin(sin(x_2[i])*cos(x_2[i])))


    plt.plot(x, fehler, color = farben[7])
    plt.plot(x, sinus, color = 'black')
    plt.plot(x_2,sin_arccos, color = 'red')
    #plt.plot(x_2, mittelwert, color = 'indigo')
    plt.plot(x, random_idee )

    plt.xlabel('Winkel')
    plt.ylabel('Punkte')
    #plt.ylim(10,-10)
    plt.legend()
    plt.savefig('el_20231227_02_04.png')
    plt.show()

    
Daten = [[9920, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10080], [9509, 110, 101, 14, 60, 46, 53, 27, 25, 53, 48, 49, 16, 98, 97, 9694], [9060, 222, 229, 21, 125, 101, 110, 52, 55, 100, 115, 118, 23, 209, 216, 9244], [8682, 309, 300, 31, 173, 163, 178, 84, 92, 151, 153, 171, 31, 333, 345, 8804], [8258, 422, 410, 48, 212, 222, 242, 106, 119, 215, 209, 236, 45, 424, 446, 8386], [7825, 533, 521, 55, 272, 282, 291, 141, 149, 277, 268, 280, 55, 529, 545, 7977], [7410, 611, 628, 63, 335, 352, 350, 171, 180, 349, 332, 319, 71, 632, 626, 7571], [7006, 697, 730, 77, 383, 422, 396, 209, 211, 412, 393, 361, 86, 714, 739, 7164], [6602, 816, 825, 88, 424, 466, 456, 243, 246, 467, 440, 425, 95, 798, 852, 6757], [6216, 917, 926, 91, 453, 536, 505, 276, 283, 524, 509, 479, 107, 906, 959, 6313], [5818, 1016, 1005, 101, 504, 598, 558, 320, 322, 599, 570, 508, 120, 994, 1054, 5913], [5430, 1102, 1095, 126, 534, 656, 617, 360, 360, 662, 629, 559, 129, 1080, 1158, 5503], [5047, 1176, 1189, 143, 574, 720, 672, 399, 424, 719, 698, 585, 144, 1148, 1215, 5147], [4716, 1233, 1245, 167, 574, 790, 755, 440, 470, 806, 764, 593, 152, 1218, 1297, 4780], [4362, 1303, 1327, 185, 582, 853, 829, 479, 523, 876, 832, 607, 172, 1299, 1355, 4416], [4019, 1367, 1379, 202, 603, 925, 896, 529, 575, 936, 902, 636, 179, 1394, 1407, 4051], [3683, 1436, 1427, 213, 619, 984, 957, 601, 636, 1014, 970, 644, 203, 1405, 1453, 3755], [3378, 1484, 1472, 237, 598, 1048, 1038, 665, 712, 1059, 1045, 644, 231, 1453, 1485, 3451], [3082, 1513, 1516, 240, 584, 1128, 1106, 751, 781, 1119, 1104, 632, 251, 1507, 1527, 3159], [2828, 1528, 1526, 259, 572, 1199, 1170, 838, 856, 1183, 1174, 623, 285, 1529, 1567, 2863], [2577, 1542, 1533, 285, 549, 1256, 1246, 932, 953, 1254, 1221, 601, 308, 1559, 1596, 2588], [2345, 1535, 1558, 301, 531, 1319, 1297, 1034, 1038, 1313, 1302, 588, 341, 1559, 1605, 2334], [2100, 1526, 1579, 337, 510, 1373, 1345, 1150, 1153, 1387, 1356, 536, 378, 1576, 1606, 2088], [1906, 1497, 1553, 377, 478, 1437, 1391, 1281, 1281, 1432, 1423, 497, 408, 1561, 1600, 1878], [1703, 1484, 1535, 406, 450, 1472, 1440, 1430, 1432, 1468, 1468, 477, 433, 1544, 1578, 1680], [1528, 1450, 1509, 442, 422, 1506, 1471, 1592, 1577, 1515, 1518, 424, 456, 1531, 1552, 1507], [1374, 1426, 1452, 486, 394, 1525, 1516, 1747, 1776, 1524, 1567, 385, 470, 1502, 1521, 1335], [1225, 1394, 1388, 516, 371, 1535, 1548, 1943, 1965, 1565, 1582, 338, 500, 1457, 1473, 1200], [1082, 1353, 1358, 539, 356, 1524, 1552, 2156, 2180, 1569, 1578, 325, 531, 1412, 1416, 1069], [1001, 1273, 1301, 559, 323, 1535, 1551, 2377, 2422, 1556, 1576, 304, 565, 1368, 1348, 941], [899, 1198, 1248, 577, 286, 1536, 1556, 2620, 2679, 1531, 1558, 277, 589, 1313, 1292, 841], [807, 1136, 1175, 612, 260, 1511, 1523, 2896, 2961, 1506, 1520, 259, 614, 1235, 1219, 766], [722, 1057, 1111, 622, 240, 1472, 1492, 3204, 3258, 1478, 1481, 240, 643, 1149, 1135, 696], [656, 989, 1033, 637, 221, 1405, 1453, 3526, 3582, 1424, 1430, 227, 629, 1076, 1085, 627], [579, 928, 975, 659, 206, 1356, 1391, 3826, 3915, 1359, 1388, 203, 648, 995, 1008, 564], [518, 856, 910, 652, 184, 1308, 1353, 4139, 4224, 1321, 1329, 178, 653, 936, 936, 503], [471, 797, 841, 653, 168, 1232, 1284, 4474, 4586, 1278, 1273, 154, 626, 839, 873, 451], [417, 735, 773, 637, 151, 1183, 1239, 4785, 4980, 1191, 1187, 140, 589, 784, 799, 410], [369, 681, 713, 601, 140, 1095, 1125, 5196, 5321, 1112, 1137, 128, 565, 713, 746, 358], [327, 635, 644, 554, 129, 1021, 1047, 5563, 5694, 1030, 1074, 118, 518, 650, 665, 331], [296, 570, 569, 507, 108, 935, 962, 5973, 6081, 946, 977, 101, 489, 587, 608, 291], [261, 509, 502, 485, 89, 823, 867, 6384, 6487, 839, 895, 93, 436, 536, 551, 243], [228, 452, 426, 446, 74, 705, 766, 6823, 6904, 746, 784, 80, 405, 458, 497, 206], [198, 382, 346, 392, 67, 629, 669, 7237, 7321, 645, 694, 64, 369, 392, 412, 183], [160, 306, 291, 330, 61, 547, 566, 7659, 7714, 551, 608, 57, 339, 328, 347, 136], [132, 250, 240, 281, 45, 446, 471, 8055, 8147, 449, 486, 49, 287, 258, 296, 108], [102, 186, 190, 218, 33, 363, 352, 8476, 8619, 344, 365, 36, 209, 202, 226, 79], [69, 135, 129, 143, 22, 263, 248, 8911, 9041, 250, 255, 26, 162, 135, 155, 56], [40, 71, 70, 92, 16, 153, 149, 9329, 9466, 157, 143, 15, 93, 77, 91, 38], [13, 24, 25, 30, 8, 41, 41, 9738, 9883, 40, 46, 8, 23, 36, 32, 12], [15, 20, 21, 29, 6, 51, 45, 9733, 9890, 50, 52, 5, 26, 20, 22, 15], [37, 79, 67, 99, 20, 154, 165, 9299, 9476, 153, 158, 21, 76, 80, 74, 42], [70, 153, 133, 143, 25, 262, 279, 8855, 9034, 275, 274, 26, 138, 132, 124, 77], [95, 212, 189, 202, 36, 357, 378, 8451, 8604, 396, 370, 34, 206, 180, 185, 105], [122, 271, 259, 238, 52, 465, 470, 8043, 8191, 501, 466, 49, 255, 234, 250, 134], [159, 327, 312, 303, 55, 576, 580, 7608, 7768, 588, 586, 63, 302, 301, 311, 161], [191, 374, 385, 358, 65, 683, 657, 7207, 7373, 693, 657, 78, 338, 364, 382, 195], [226, 421, 445, 407, 85, 776, 753, 6807, 6964, 795, 763, 94, 384, 420, 431, 229], [255, 478, 504, 449, 88, 876, 870, 6400, 6536, 905, 855, 101, 464, 465, 484, 270], [294, 529, 567, 487, 93, 969, 969, 6012, 6093, 1016, 949, 117, 501, 531, 571, 302], [342, 588, 623, 528, 119, 1033, 1058, 5629, 5705, 1099, 1041, 127, 541, 595, 627, 345], [375, 647, 696, 543, 133, 1151, 1135, 5240, 5330, 1172, 1126, 136, 568, 666, 686, 396], [422, 709, 751, 570, 154, 1225, 1206, 4883, 4954, 1259, 1189, 150, 584, 730, 764, 450], [459, 794, 819, 579, 174, 1284, 1256, 4555, 4607, 1313, 1252, 161, 606, 801, 842, 498], [508, 862, 889, 596, 194, 1347, 1332, 4192, 4237, 1375, 1350, 175, 627, 862, 907, 547], [557, 932, 961, 605, 205, 1404, 1390, 3866, 3908, 1438, 1394, 185, 630, 934, 985, 606], [639, 999, 1005, 610, 225, 1455, 1466, 3521, 3588, 1482, 1426, 215, 645, 1014, 1035, 675], [707, 1074, 1076, 591, 244, 1494, 1498, 3236, 3293, 1518, 1494, 240, 647, 1059, 1082, 747], [788, 1145, 1163, 568, 245, 1524, 1538, 2949, 3007, 1547, 1528, 258, 627, 1144, 1149, 820], [882, 1209, 1227, 560, 270, 1534, 1542, 2696, 2731, 1573, 1532, 294, 618, 1209, 1220, 903], [983, 1281, 1289, 537, 292, 1543, 1538, 2457, 2456, 1605, 1563, 323, 603, 1265, 1275, 990], [1083, 1320, 1357, 517, 316, 1576, 1543, 2208, 2220, 1603, 1560, 353, 565, 1337, 1354, 1088], [1208, 1361, 1411, 499, 368, 1564, 1506, 2003, 1991, 1586, 1565, 399, 514, 1403, 1411, 1211], [1358, 1412, 1455, 471, 386, 1542, 1488, 1808, 1783, 1595, 1547, 419, 482, 1455, 1455, 1344], [1502, 1454, 1496, 431, 428, 1527, 1469, 1613, 1597, 1573, 1525, 447, 447, 1487, 1505, 1499], [1671, 1507, 1517, 399, 481, 1461, 1426, 1458, 1421, 1546, 1520, 461, 391, 1540, 1527, 1674], [1835, 1533, 1533, 384, 498, 1420, 1409, 1308, 1269, 1490, 1471, 487, 364, 1581, 1550, 1868], [2043, 1544, 1537, 360, 528, 1373, 1378, 1157, 1132, 1434, 1439, 517, 331, 1587, 1564, 2076], [2262, 1563, 1530, 340, 541, 1323, 1316, 1045, 1007, 1378, 1387, 554, 317, 1576, 1563, 2298], [2501, 1555, 1534, 302, 573, 1282, 1226, 947, 890, 1320, 1341, 588, 287, 1560, 1541, 2553], [2760, 1540, 1524, 274, 585, 1210, 1172, 855, 804, 1258, 1280, 609, 258, 1536, 1527, 2808], [3049, 1512, 1497, 248, 617, 1142, 1091, 764, 733, 1169, 1189, 628, 247, 1506, 1492, 3116], [3358, 1479, 1437, 231, 629, 1070, 1027, 689, 661, 1110, 1108, 646, 234, 1462, 1457, 3402], [3686, 1415, 1373, 217, 646, 1011, 960, 612, 592, 1049, 1038, 639, 216, 1412, 1393, 3741], [3992, 1368, 1323, 193, 664, 938, 888, 554, 530, 969, 962, 658, 185, 1357, 1346, 4073], [4324, 1292, 1268, 176, 665, 876, 823, 496, 474, 908, 887, 639, 163, 1305, 1311, 4393], [4623, 1264, 1205, 161, 647, 804, 773, 443, 429, 831, 818, 614, 148, 1229, 1241, 4770], [4997, 1176, 1144, 141, 616, 745, 707, 394, 386, 768, 759, 577, 133, 1166, 1153, 5138], [5384, 1081, 1053, 135, 583, 681, 659, 344, 349, 698, 677, 539, 122, 1112, 1085, 5498], [5772, 997, 977, 124, 525, 607, 608, 310, 305, 649, 610, 501, 108, 1021, 989, 5897], [6183, 907, 872, 102, 508, 526, 540, 282, 265, 573, 557, 468, 100, 945, 900, 6272], [6606, 821, 760, 79, 458, 463, 487, 246, 225, 520, 497, 424, 85, 851, 784, 6694], [7029, 714, 669, 76, 418, 390, 417, 207, 189, 456, 433, 375, 79, 739, 689, 7120], [7459, 616, 574, 65, 371, 316, 341, 178, 157, 393, 361, 348, 60, 639, 590, 7532], [7871, 514, 484, 52, 299, 270, 285, 145, 120, 322, 292, 297, 53, 538, 504, 7954], [8254, 419, 412, 36, 258, 212, 211, 118, 95, 262, 230, 251, 36, 441, 400, 8365], [8698, 307, 310, 28, 187, 150, 152, 88, 62, 187, 167, 187, 34, 308, 307, 8828], [9128, 189, 202, 18, 130, 100, 100, 53, 50, 122, 99, 135, 21, 200, 205, 9248], [9548, 93, 90, 11, 59, 48, 44, 27, 24, 62, 54, 61, 8, 103, 102, 9666], [9920, 0, 0, 0, 0, 0, 0, 0, 6, 13, 1, 0, 3, 5, 2, 10050]]  
  #Daten = np.array(Daten).reshape(int(len(Daten)/16),16).tolist()

Winkel = np.linspace(0,2*pi,100)
graph_off(Winkel, Daten)