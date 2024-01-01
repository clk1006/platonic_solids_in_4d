
from math import *
import random 
import numpy as np
from matplotlib import pyplot as plt #für die graphiken
import time

def interpol(daten, x):
    L = 0
    for i in range(len(daten)):
        L += daten[i][1]*lagrange(daten, i, x)

    return L    

def lagrange(daten, i, x):
    L = 1
    for j in range(len(daten)):
        if j != i:
            L = L * (x-daten[j][0])/(daten[i][0]-daten[j][0])
    return L        

# x Werte und eine Liste, die zu jeden x-Werte eine Liste der y-Werte enthällt
def graph_off(x, y_werte ,vergleich = False):
    y_listen = []
    Summe = list([])
    for i in range(len(y_werte[0])):
        y_listen += [[]]
        for j in y_werte:
            y_listen[i] += [j[i]]
            #if i == 0:
                #Summe += [sum(j)]
    #print(x,y_listen)

    #Das Bild
    plt.figure(figsize=(12,8))

    farben = [ 'dimgray' , 'silver', 'lightcoral', 'firebrick', 'darkred' ,'red', 'orangered' , 'darkorange', 'gold', 'yellow' , 'yellowgreen' , 'limegreen', 'forestgreen' , 'darkgreen' , 'teal' , 'royalblue' , 'navy' , 'indigo']

    for y in range(len(y_listen)):
        plt.plot(x,y_listen[y], label = "Bereich " + str(y+1) , color = farben[y])

    
    #plt.plot(x, Summe , label = "Summe" , color = 'black')
    plt.xlabel('Winkel')
    plt.ylabel('Punkte')
    #plt.ylim(10,-10)

    if vergleich:
        x = np.linspace(0,2*pi,200)
        x_2 = np.linspace(0,pi,100)
        vergleich = []
        vergleich_2 = []
        vergleich_3 = []


        a_liste = []
        for i in x_2:
            a = acos(-cos(i)**2)
            a_2 = acos(cos(i)**2)
            #a = acos(- 1 / sqrt(tan(i)**2+2))
            a_liste.append(a)
            vergleich.append(100_000/(4*pi)* ( a + 2*(pi/2-i)))
            vergleich_2.append(100_000/(4*pi)*((-2*(pi/2-i) + a)))
            vergleich_3.append(100_000/(4*pi)* (a_2))
            #vergleich.append(100_000/(4*pi)* (acos(-1/tan(a)**2) + 2*acos(1/tan(a)) -pi))

        plt.plot(x_2, vergleich , label = 'Vergleich', color = 'black')
        plt.plot(x_2, vergleich_2 , color = 'black')
        plt.plot(x_2, vergleich_3 , color = 'black')
        #plt.plot(x, 50_000*((pi-x)/pi)**2, label = '$((x-pi)/pi)^2$', color= 'indigo')
        #plt.plot(x_2,50_000*(x_2/pi)**2, label = "$(x/pi)^2$", color = 'purple')
        #plt.plot(x_2, 50_000*(x_2/pi)*(pi-x_2)/pi, label = "$(x/pi)*(pi-x)/pi$", color = 'black')

    plt.legend()    
    plt.savefig('el_20231229_03_37.png')    
    plt.show()    

def graph_vergleich(x, y_werte ):
    x = list(x)
    y_listen = []
    Summe = list([])
    for i in range(len(y_werte[0])):
        y_listen += [[]]
        for j in y_werte:
            y_listen[i] += [j[i]]
            

    #Das Bild
    plt.figure(figsize=(12,8))

    farben = [ 'dimgray' , 'silver', 'lightcoral', 'firebrick', 'darkred' ,'red', 'orangered' , 'darkorange', 'gold', 'yellow' , 'yellowgreen' , 'limegreen', 'forestgreen' , 'darkgreen' , 'teal' , 'royalblue' , 'navy' , 'indigo']

    x = x[0:100]
    for y in range(len(y_listen)):
        y_listen[y] = y_listen[y][0:100]
    print(len(y_listen[0]))  

    a_liste = []
    for i in x:
        a = acos(cos(i)**2)
        a_liste.append(a)

    for i in (3,4):
        show = []
        for f in range(len(y_listen[i])):
            show.append(y_listen[i][f] - (100_000/(4*pi)* (pi - (a_liste[f] + 2*(pi/2 - x[f])))))
        plt.plot(x, show, label = "Vergleich Bereich " + str(i+1) , color = farben[i])

    print(x[-1])
    for i in (0,7):
        show = []
        for f in range(len(y_listen[i])):
            show.append(y_listen[i][-(f+1)] - (100_000/(4*pi)* (pi - (acos(cos(pi-x[-(f+1)])**2) + 2*(pi/2 - (pi-x[-(f+1)]))))))
        plt.plot(x, show, label = "Vergleich Bereich " + str(i+1) , color = farben[i])

    dreihundertsechzehn = []
    for i in x: dreihundertsechzehn.append(316)
    plt.plot(x,dreihundertsechzehn, color = 'black')
    dreihundertsechzehn = []
    for i in x: dreihundertsechzehn.append(-316) 
    plt.plot(x,dreihundertsechzehn, color = 'black')


    """for i in range(len(y_listen)):
        if i == 0 or i == 7:
            show = []
            for f in range(len(y_listen[i])):
                show += [y_listen[i][f] - 50_000*((pi-x[f])/pi)**2]
            plt.plot(x, show, label = "Bereich 1")
        elif i == 3 or i == 4:
            show = []
            for f in range(len(y_listen[i])):
                show += [y_listen[i][f] - 50_000*(x[f]/pi)**2]
            plt.plot(x, show, label = "Bereich 4")
        else: 
            show = []
            for f in range(len(y_listen[i])):
                show += [y_listen[i][f] - 50_000*(x[f]/pi)*((pi-x[f])/pi)]
            plt.plot(x, show, label = "Bereich 2/3") 
    x = np.linspace(0,pi,100)
    plt.plot(x, interpol([(0,0),(pi,0),(pi/2,0),(4*pi/5,1_184.1),(pi/5,1_181.1)],x), label ='Interpol von Fehler', color= 'black')
    """
    plt.xlabel('Winkel')
    plt.ylabel('Punkte')        
    plt.legend()    
    plt.savefig('el_20231229_03_36.png')    
    plt.show()                 

    
Winkel = np.linspace(0,2*pi,200)    
"""with open('el_20231228_03.txt', "r") as speicher:
    speicher.readline()
    Daten = np.array(list(speicher.readline())).reshape(len(Winkel),8).tolist()"""
Daten = [[50216, 0, 0, 0, 0, 0, 0, 49784], [49310, 344, 383, 123, 182, 382, 377, 48899], [48261, 676, 710, 267, 325, 698, 736, 48327], [47461, 989, 1010, 453, 480, 1088, 1067, 47452], [46340, 1387, 1427, 541, 579, 1455, 1429, 46842], [45678, 1708, 1752, 710, 753, 1729, 1827, 45843], [44785, 2098, 2104, 905, 941, 2122, 2118, 44927], [44009, 2428, 2445, 1022, 1113, 2460, 2580, 43943], [42998, 2792, 2857, 1194, 1228, 2861, 2866, 43204], [42412, 3200, 3113, 1363, 1325, 3238, 3262, 42087], [41232, 3517, 3455, 1498, 1579, 3536, 3574, 41609], [40497, 3882, 3826, 1620, 1689, 3928, 4012, 40546], [39534, 4204, 4148, 1784, 1857, 4199, 4159, 40115], [39023, 4498, 4545, 1954, 2030, 4536, 4547, 38867], [38054, 4794, 4804, 2069, 2151, 4986, 4972, 38170], [37214, 5322, 5200, 2300, 2331, 5139, 5198, 37296], [36534, 5459, 5484, 2354, 2481, 5597, 5637, 36454], [35488, 5943, 5932, 2554, 2668, 5813, 5965, 35637], [34590, 6208, 6244, 2858, 2818, 6161, 6247, 34874], [33912, 6534, 6444, 3034, 2936, 6574, 6473, 34093], [33201, 6767, 6724, 3130, 3192, 7028, 6833, 33125], [32079, 7108, 7313, 3276, 3356, 7250, 7224, 32394], [31308, 7481, 7587, 3580, 3620, 7591, 7587, 31246], [30814, 7907, 7598, 3842, 3733, 7708, 7707, 30691], [29914, 8115, 8091, 3883, 3979, 7964, 8001, 30053], [28817, 8288, 8368, 4251, 4124, 8603, 8351, 29198], [28207, 8660, 8625, 4388, 4394, 8587, 8543, 28596], [27628, 8844, 8755, 4627, 4604, 8899, 9082, 27561], [26456, 9189, 9352, 4826, 4901, 9237, 9319, 26720], [25772, 9541, 9377, 4937, 5122, 9459, 9628, 26164], [25143, 9586, 9821, 5267, 5349, 9814, 9724, 25296], [24397, 9924, 9982, 5530, 5498, 9984, 10174, 24511], [23724, 10156, 10195, 5854, 5883, 10366, 10038, 23784], [22781, 10500, 10473, 6117, 6189, 10565, 10484, 22891], [22537, 10607, 10634, 6350, 6481, 10703, 10556, 22132], [21524, 10882, 10889, 6721, 6731, 10757, 11033, 21463], [21034, 11278, 10924, 6900, 6908, 11407, 11141, 20408], [19996, 11370, 11176, 7246, 7359, 11254, 11357, 20242], [19613, 11474, 11412, 7502, 7672, 11458, 11492, 19377], [18668, 11643, 11545, 7847, 8096, 11863, 11468, 18870], [18021, 11913, 11830, 8277, 8286, 11783, 11903, 17987], [17451, 11919, 11793, 8645, 8861, 12141, 11954, 17236], [16626, 12140, 11907, 9210, 9113, 12084, 12092, 16828], [16363, 12064, 11922, 9479, 9509, 12316, 12227, 16120], [15596, 12245, 12147, 9771, 9868, 12272, 12315, 15786], [14909, 12303, 12365, 10277, 10291, 12172, 12436, 15247], [14663, 12370, 12334, 10698, 10681, 12293, 12267, 14694], [13984, 12273, 12450, 11188, 11220, 12250, 12518, 14117], [13435, 12548, 12456, 11499, 11616, 12468, 12358, 13620], [12748, 12370, 12497, 12026, 12316, 12473, 12635, 12935], [12401, 12557, 12513, 12668, 12840, 12404, 12398, 12219], [11913, 12622, 12360, 13019, 13132, 12553, 12505, 11896], [11504, 12432, 12247, 13619, 13657, 12531, 12515, 11495], [10900, 12353, 12495, 14233, 14156, 12419, 12411, 11033], [10292, 12449, 12177, 14919, 14770, 12424, 12385, 10584], [10133, 12307, 12036, 15254, 15396, 12268, 12468, 10138], [9651, 12273, 12039, 16102, 15839, 12031, 12236, 9829], [9291, 12134, 12162, 16330, 16590, 11950, 12162, 9381], [8870, 11867, 12189, 17156, 17130, 11962, 12024, 8802], [8586, 11605, 11872, 17898, 17912, 11763, 11894, 8470], [8234, 11623, 11513, 18480, 18743, 11723, 11507, 8177], [7748, 11437, 11559, 19364, 18948, 11635, 11551, 7758], [7404, 11372, 11302, 19630, 19757, 11536, 11344, 7655], [7046, 10977, 11104, 20699, 20620, 11157, 11243, 7154], [6793, 11149, 11014, 21174, 21048, 11079, 11012, 6731], [6527, 10698, 10807, 22044, 21708, 10805, 10908, 6503], [6174, 10464, 10580, 22436, 22805, 10657, 10666, 6218], [6037, 10316, 10185, 23342, 23281, 10590, 10360, 5889], [5782, 10114, 10007, 24157, 23933, 10184, 10075, 5748], [5578, 9768, 9789, 24764, 24983, 9813, 9847, 5458], [5186, 9562, 9475, 25699, 25695, 9658, 9561, 5164], [4961, 9230, 9391, 26175, 26516, 9399, 9459, 4869], [4653, 8924, 9014, 27397, 27186, 8972, 9042, 4812], [4496, 8829, 8807, 28050, 27680, 8857, 8730, 4551], [4253, 8442, 8466, 28671, 28718, 8644, 8577, 4229], [4050, 8185, 8186, 29313, 29538, 8320, 8311, 4097], [3853, 7845, 7842, 30439, 30229, 7982, 7992, 3818], [3623, 7564, 7610, 31105, 31082, 7778, 7626, 3612], [3455, 7227, 7264, 31735, 32128, 7364, 7351, 3476], [3333, 7119, 7077, 32519, 32693, 6969, 7051, 3239], [3036, 6593, 6673, 33511, 33663, 6744, 6561, 3219], [2873, 6396, 6210, 34377, 34532, 6367, 6356, 2889], [2635, 5993, 6103, 35383, 35118, 6068, 5986, 2714], [2547, 5721, 5665, 35896, 36292, 5705, 5692, 2482], [2354, 5377, 5435, 36721, 36864, 5524, 5303, 2422], [2189, 5012, 5119, 37532, 37617, 5178, 5085, 2268], [2055, 4680, 4708, 38416, 38661, 4649, 4710, 2121], [1908, 4363, 4435, 39323, 39282, 4367, 4370, 1952], [1741, 4041, 4058, 39969, 40331, 4047, 4072, 1741], [1543, 3611, 3688, 40971, 41225, 3719, 3718, 1525], [1399, 3390, 3356, 42077, 41529, 3397, 3340, 1512], [1212, 3062, 2949, 42568, 42761, 3125, 3059, 1264], [1063, 2660, 2665, 43726, 43387, 2612, 2752, 1135], [974, 2314, 2223, 44524, 44433, 2266, 2300, 966], [846, 1941, 2005, 45107, 45346, 1955, 1965, 835], [657, 1542, 1572, 46248, 46106, 1536, 1619, 720], [487, 1173, 1283, 46922, 47059, 1247, 1291, 538], [377, 814, 888, 47552, 48230, 901, 858, 380], [206, 542, 490, 48469, 48920, 538, 579, 256], [47, 145, 149, 49258, 49935, 184, 200, 82], [46, 172, 168, 49427, 49712, 186, 196, 93], [202, 505, 511, 48760, 48740, 507, 531, 244], [353, 835, 907, 48165, 47558, 925, 894, 363], [488, 1216, 1256, 46870, 47171, 1233, 1261, 505], [684, 1583, 1590, 45962, 46293, 1614, 1618, 656], [795, 1920, 1911, 45245, 45428, 1970, 1924, 807], [921, 2390, 2331, 44531, 44284, 2274, 2212, 1057], [1134, 2550, 2639, 43789, 43566, 2600, 2614, 1108], [1265, 2938, 3046, 42496, 42926, 3028, 3006, 1295], [1390, 3363, 3263, 41701, 41984, 3373, 3409, 1517], [1531, 3652, 3731, 40817, 41164, 3707, 3754, 1644], [1721, 4076, 3962, 40317, 40111, 4141, 3942, 1730], [1877, 4272, 4296, 39423, 39323, 4437, 4437, 1935], [1986, 4789, 4732, 38183, 38752, 4793, 4692, 2073], [2170, 4987, 5064, 37391, 37920, 5105, 5158, 2205], [2385, 5369, 5437, 36858, 36821, 5366, 5309, 2455], [2588, 5674, 5560, 35912, 36034, 5841, 5790, 2601], [2699, 6008, 6272, 35063, 35169, 5973, 6053, 2763], [2932, 6379, 6404, 34532, 34121, 6312, 6423, 2897], [3142, 6639, 6635, 33570, 33480, 6724, 6660, 3150], [3324, 7037, 6980, 32779, 32707, 6954, 7009, 3210], [3553, 7277, 7304, 31886, 31877, 7230, 7467, 3406], [3594, 7477, 7701, 31122, 31133, 7680, 7618, 3675], [3980, 7872, 7985, 29930, 30444, 7899, 8033, 3857], [3992, 8329, 8184, 29726, 29400, 8028, 8193, 4148], [4309, 8520, 8549, 28474, 28742, 8574, 8517, 4315], [4546, 8622, 8769, 27787, 28038, 8959, 8832, 4447], [4652, 9070, 8965, 27082, 27339, 9021, 9169, 4702], [4968, 9426, 9262, 26320, 26402, 9281, 9430, 4911], [5221, 9717, 9568, 25406, 25565, 9601, 9643, 5279], [5520, 9939, 9884, 24569, 24640, 9957, 9933, 5558], [5823, 10063, 9995, 23990, 24306, 9977, 10167, 5679], [6019, 10430, 10277, 23435, 23319, 10197, 10325, 5998], [6287, 10783, 10572, 22443, 22393, 10584, 10611, 6327], [6614, 10909, 10834, 21786, 21660, 10570, 10924, 6703], [6930, 10925, 10994, 21225, 21224, 11104, 10822, 6776], [7103, 11189, 11338, 20561, 20544, 11159, 10957, 7149], [7466, 11256, 11339, 19770, 19971, 11471, 11261, 7466], [7849, 11564, 11375, 19012, 19174, 11545, 11537, 7944], [8275, 11587, 11667, 18376, 18477, 11820, 11526, 8272], [8399, 11863, 11863, 17753, 17898, 11941, 11780, 8503], [8673, 12016, 11933, 17182, 17133, 12061, 12056, 8946], [9167, 12118, 12047, 16570, 16503, 12110, 12133, 9352], [9611, 12234, 12046, 15992, 16065, 12059, 12296, 9697], [10116, 12332, 12213, 15382, 15256, 12414, 12188, 10099], [10474, 12457, 12345, 14586, 14756, 12435, 12526, 10421], [10925, 12378, 12389, 14198, 14252, 12232, 12587, 11039], [11512, 12450, 12364, 13683, 13792, 12443, 12378, 11378], [11786, 12372, 12368, 13334, 13075, 12643, 12563, 11859], [12522, 12461, 12342, 12595, 12620, 12631, 12391, 12438], [12803, 12323, 12655, 12117, 12301, 12485, 12401, 12915], [13213, 12504, 12483, 11739, 11694, 12569, 12502, 13296], [14052, 12375, 12501, 11044, 11269, 12564, 12338, 13857], [14429, 12231, 12438, 10625, 10839, 12316, 12418, 14704], [15169, 12233, 12292, 10306, 10308, 12467, 12293, 14932], [15665, 12092, 12196, 9869, 10041, 12255, 12088, 15794], [16178, 12009, 12104, 9562, 9528, 12119, 12167, 16333], [16617, 12020, 11959, 9105, 9158, 12047, 12224, 16870], [17425, 11885, 11908, 8600, 8675, 11872, 12089, 17546], [17994, 11652, 11799, 8223, 8355, 12014, 11595, 18368], [18746, 11500, 11794, 7936, 8017, 11615, 11804, 18588], [19420, 11358, 11401, 7442, 7710, 11508, 11674, 19487], [20249, 11396, 11279, 7275, 7195, 11289, 11445, 19872], [20618, 11100, 11053, 6910, 6981, 11324, 11282, 20732], [21400, 10820, 10852, 6710, 6788, 11083, 10869, 21478], [22154, 10731, 10705, 6405, 6435, 10767, 10602, 22201], [22732, 10518, 10411, 6024, 6169, 10586, 10537, 23023], [23845, 10154, 10328, 5801, 5918, 10247, 10250, 23457], [24663, 9774, 10075, 5621, 5610, 9873, 9949, 24435], [25274, 9608, 9562, 5325, 5275, 9736, 9741, 25479], [26032, 9409, 9414, 5182, 5063, 9721, 9281, 25898], [26870, 9127, 9135, 4763, 4898, 9139, 9304, 26764], [27396, 8894, 8974, 4544, 4611, 9098, 9020, 27463], [28345, 8587, 8582, 4419, 4575, 8657, 8561, 28274], [28828, 8489, 8186, 4262, 4259, 8455, 8458, 29063], [30228, 7805, 8068, 3951, 4023, 8175, 8039, 29711], [30526, 7804, 7734, 3714, 3783, 7889, 7751, 30799], [31677, 7477, 7342, 3518, 3510, 7423, 7541, 31512], [32175, 7220, 7231, 3416, 3449, 6974, 7234, 32301], [33061, 6896, 6857, 3157, 3192, 6953, 6804, 33080], [33785, 6647, 6483, 3035, 3048, 6532, 6608, 33862], [34563, 6221, 6166, 2886, 2816, 6156, 6230, 34962], [35590, 5822, 5813, 2679, 2762, 5823, 6011, 35500], [36364, 5521, 5528, 2414, 2515, 5581, 5455, 36622], [37361, 5210, 5165, 2211, 2288, 5145, 5251, 37369], [38327, 4720, 4875, 2239, 2147, 4952, 4872, 37868], [38611, 4640, 4458, 2002, 1947, 4604, 4681, 39057], [39745, 4202, 4177, 1788, 1866, 4217, 4192, 39813], [40609, 3837, 3845, 1724, 1654, 3783, 4038, 40510], [41393, 3551, 3523, 1454, 1551, 3507, 3613, 41408], [42044, 3117, 3163, 1320, 1397, 3263, 3177, 42519], [43021, 2893, 2755, 1177, 1205, 2801, 2924, 43224], [44067, 2525, 2415, 983, 984, 2496, 2505, 44025], [45004, 2104, 2041, 864, 892, 2128, 2138, 44829], [45493, 1754, 1737, 705, 749, 1794, 1838, 45930], [46599, 1377, 1452, 543, 630, 1480, 1461, 46458], [47544, 1046, 1076, 453, 430, 1054, 1114, 47283], [48212, 712, 687, 286, 322, 718, 748, 48315], [49133, 325, 325, 135, 173, 353, 356, 49200], [50069, 0, 0, 0, 31, 36, 32, 49832]] 
print(type(Daten))   
graph_off(Winkel, Daten, True) 
#graph_vergleich(Winkel, Daten)


