import copy
import time

from linear_genetic_programming._instruction import Instruction
from linear_genetic_programming._program_multi import ProgramMulti
from linear_genetic_programming._statistics import Statistics
from linear_genetic_programming._two_input_boolean_funcs_new import TwoInputBooleanFuncsNew
class EM:
    RANDOM_WALK_STEP = 1000
    def get_dict(self, target_pheno):
        res_dict_conv = {}
        res_dict_nove = {}
        res_dict_hill = {}
        time1 = 0
        time2 = 0
        time3 = 0
        for i in range(10):
            visited = [False] * 16
            sequence = []
            for m in range(4):
                instr = Instruction()
                instr.makeRandInstr(4, 2, 2)
                sequence.append(instr)

            start = time.time()
            prog_con = ProgramMulti()
            prog_con.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog_con)
            prog_update = copy.deepcopy(prog_con)
            find = False
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_update)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_conv[pheno_cur] = res_dict_conv.get(pheno_cur, []) + [j]
                    find = True
                    break
            if not find:
                res_dict_conv.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time1 += end - start

            start = time.time()
            prog2 = ProgramMulti()
            prog2.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog2)
            prog_cur = copy.deepcopy(prog2)
            find = False
            visited[pheno_cur] = True
            for j in range(self.RANDOM_WALK_STEP):
                prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                while visited[TwoInputBooleanFuncsNew.phenotype(prog_update)] and TwoInputBooleanFuncsNew.phenotype(
                        prog_update) != TwoInputBooleanFuncsNew.phenotype(prog_cur):
                    prog_update = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncsNew.phenotype(prog_update) == target_pheno:
                    res_dict_nove[pheno_cur] = res_dict_nove.get(pheno_cur, []) + [j]
                    find = True
                    break
                prog_cur = prog_update
            if not find:
                res_dict_nove.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time2 += end - start


            start = time.time()
            prog3 = ProgramMulti()
            prog3.makeDetermProg(sequence)

            pheno_cur = TwoInputBooleanFuncsNew.phenotype(prog3)
            prog_cur = copy.deepcopy(prog3)
            find = False
            j = 0
            while j < self.RANDOM_WALK_STEP:
                neibor = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                while neibor.fitness(target_pheno) < prog_cur.fitness(target_pheno):
                    neibor = TwoInputBooleanFuncsNew.one_step_mutation(prog_cur)
                if TwoInputBooleanFuncsNew.phenotype(neibor) == target_pheno:
                    res_dict_hill[pheno_cur] = res_dict_hill.get(pheno_cur, []) + [j]
                    find = True
                    break
                j += 1
                prog_cur = neibor
            if not find:
                res_dict_hill.get(pheno_cur, []) + [self.RANDOM_WALK_STEP + 1]
            end = time.time()
            time3 += end - start
        return res_dict_conv, res_dict_nove, res_dict_hill, time1, time2, time3

    @staticmethod
    def get_avg(dic):
        avg = {}
        for key1, value1 in dic.items():
            for key2, value2 in value1.items():
                avg[(key1, key2)] = [Statistics.mean(value2), len(value2)]
        return avg

if __name__ == "__main__":
    final_dict = {}
    res_ran = {}
    res_hill = {}
    res_nove = {}
    time_ran = 0
    time_nove = 0
    time_hill = 0
    for i in range(16):
        print(i)
        hill_climbing = EM()
        res_ran[i] = hill_climbing.get_dict(i)[0]
        res_nove[i] = hill_climbing.get_dict(i)[1]
        res_hill[i] = hill_climbing.get_dict(i)[2]
        time_ran += hill_climbing.get_dict(i)[3]
        time_nove += hill_climbing.get_dict(i)[4]
        time_hill += hill_climbing.get_dict(i)[5]

    print(EM.get_avg(res_ran))
    print(time_ran)
    print(EM.get_avg(res_nove))
    print(time_nove)
    print(EM.get_avg(res_hill))
    print(time_hill)

'''
{(7, 3): 56.78973242345337, (12, 1): 37.89003246952151, (11, 11): 64.75188899574106, (7, 12): 65.44869458265784, (14, 4): 61.10211919621426, (13, 4): 141.81196172248804, (12, 12): 9.617694002337913, (0, 7): 17.45385897409515, (15, 1): 22.246942557134005, (1, 6): 49.8235294117647, (0, 10): 13.994089527275198, (3, 7): 30.513990105310697, (2, 5): 148.51361300024686, (1, 11): 63.90131176510574, (8, 5): 63.905297328870205, (5, 8): 37.366743256950045, (4, 0): 144.31146737483752, (10, 8): 30.6498636764314, (9, 0): 14022.712607023706, (6, 7): 13960.80246199604, (5, 5): 9.661794518553362, (11, 5): 147.40478192151176, (10, 7): 37.845615488145725, (6, 10): 14091.440337115218, (15, 11): 13.208759024656041, (14, 1): 56.676489390221285, (13, 7): 140.84232237409162, (0, 4): 10.66337871631009, (15, 4): 20.410377358490585, (1, 1): 19.070224027572657, (8, 15): 65.00515075532063, (4, 10): 145.51924658382995, (3, 2): 31.63555073838233, (9, 14): 14048.130899431675, (8, 2): 54.18820128037448, (5, 11): 37.18069021628583, (4, 5): 143.9576115043253, (10, 13): 34.203666551366254, (9, 3): 14079.217942675015, (6, 0): 14033.578338228446, (11, 0): 150.46644669391677, (7, 5): 56.81957441065323, (14, 15): 57.16049681425918, (12, 11): 34.39213259060587, (15, 14): 15.946700560067772, (14, 2): 59.87994812994813, (13, 10): 145.29923556628438, (0, 1): 13.03748416881154, (3, 12): 31.27524609735769, (1, 12): 63.729622935913675, (8, 12): 56.48643879191161, (4, 15): 148.70162505447988, (3, 1): 31.697879208891795, (2, 11): 139.17833298919402, (5, 14): 37.75910329706357, (10, 14): 32.111795063110165, (6, 13): 13841.476757055896, (11, 15): 140.9752458439564, (7, 8): 57.87246821024728, (14, 8): 60.14440217950036, (13, 0): 150.02410291070052, (12, 8): 30.558574941621377, (15, 13): 12.878599699740684, (13, 13): 66.38218510786353, (0, 14): 16.95109646865029, (3, 11): 32.98289662721479, (2, 1): 142.07902704261318, (1, 15): 65.17409137659699, (4, 12): 141.16101104922757, (2, 12): 145.34769854332515, (9, 4): 14209.3306395911, (5, 1): 31.506622448349024, (10, 3): 40.972800556097425, (7, 2): 64.0117375669991, (6, 14): 14032.902950454632, (12, 2): 33.74365867107808, (11, 10): 141.72762650316173, (7, 15): 63.92960644561519, (14, 5): 62.29021374850085, (13, 3): 147.6854511887609, (12, 13): 29.218417149791016, (15, 0): 18.53959988915608, (1, 5): 57.415736638438695, (0, 11): 16.703590738943614, (3, 6): 45.83529411764706, (2, 2): 67.63120759837183, (1, 10): 64.07471883628524, (4, 1): 140.96480516774287, (9, 7): 14001.269008264473, (6, 4): 13935.493122278293, (5, 4): 31.90550528424397, (11, 4): 135.6462066598009, (10, 4): 34.17961896929833, (7, 1): 61.76014684045537, (6, 11): 14053.522600787299, (12, 7): 37.56289469894884, (15, 10): 17.107638302899375, (0, 5): 13.853035287755194, (15, 7): 19.157373139238423, (1, 0): 60.596550921366024, (0, 8): 14.196023840458661, (4, 11): 136.1518016166598, (3, 5): 38.082101972426464, (2, 7): 148.7047477438406, (9, 13): 14068.86334891394, (8, 3): 63.46640653990172, (5, 10): 31.087080962307734, (10, 10): 9.706027789586749, (9, 2): 13896.677675757152, (6, 1): 14047.8048411811, (5, 7): 30.355896547456997, (11, 3): 144.70055818236924, (7, 4): 64.91468117339213, (14, 12): 57.234528852279446, (12, 4): 29.679933665008292, (15, 9): 14.018518518518519, (14, 3): 62.3727172420005, (0, 2): 10.570207820618, (3, 15): 35.54990814071848, (1, 3): 57.900909714491334, (8, 13): 61.520939387768955, (4, 8): 139.07545316911492, (3, 0): 35.39429584417912, (2, 8): 139.3439589743592, (9, 8): 14040.87995072374, (8, 0): 63.10836159555311, (5, 13): 32.37369146005509, (10, 15): 33.53059104344708, (6, 2): 14179.434770723712, (11, 14): 140.43874626250144, (7, 11): 57.70011757382945, (15, 12): 17.13379822292206, (13, 12): 141.89319994134988, (0, 15): 13.367074685335417, (3, 10): 40.88015010641877, (1, 14): 57.336868603499504, (8, 10): 56.58400217042346, (4, 13): 140.43155389323366, (2, 13): 137.6804392587508, (9, 11): 13912.286149373573, (5, 0): 35.41678762678478, (10, 0): 35.91488496397867, (6, 15): 14054.884424297828, (12, 3): 31.094707802038826, (11, 13): 132.64703068407027, (7, 14): 61.67475708253044, (14, 10): 56.9193111433357, (13, 2): 135.62158875979475, (12, 14): 31.89407459188291, (15, 3): 18.706532991268354, (13, 15): 141.02684331939344, (1, 4): 56.282758146569506, (0, 12): 14.124132294325765, (2, 3): 143.85514207478556, (8, 7): 56.937584276549664, (4, 2): 133.90812864703472, (2, 14): 146.9222189793195, (6, 5): 14083.23328628399, (5, 3): 38.11068591574435, (11, 7): 140.6403053372456, (10, 5): 31.077653964220257, (7, 0): 67.11681354141949, (6, 8): 14049.658713268396, (12, 0): 35.578259801183954, (11, 8): 146.26596798151536, (7, 13): 58.179313153250995, (14, 7): 59.07087833791124, (13, 5): 144.38522140722614, (1, 7): 60.65977837061359, (3, 4): 37.29170658272883, (2, 4): 133.4896406494124, (9, 12): 14083.60410053657, (8, 4): 54.56832781121105, (4, 7): 148.3123820464429, (10, 11): 29.869872225958304, (9, 1): 14083.492417816587, (11, 2): 142.08847222222235, (7, 7): 18.990790988324278, (14, 13): 53.15828936406554, (12, 5): 40.513829931358394, (15, 8): 21.674911588124022, (14, 0): 63.91141134435016, (13, 8): 146.30302028674123, (0, 3): 13.814657980456028, (15, 5): 18.736332702361643, (3, 14): 37.69561914928569, (1, 2): 56.600179014045715, (8, 14): 60.833609797055146, (3, 3): 9.476515397263949, (9, 15): 14077.601051947662, (8, 1): 60.09286170717125, (5, 12): 41.095649424703296, (4, 4): 67.07259825327502, (10, 12): 37.74111156058968, (6, 3): 14167.981945534008, (11, 1): 148.45568135035012, (7, 10): 65.01138037672176, (14, 14): 19.25488783700354, (12, 10): 37.83223702704219, (15, 15): 4.677089192012215, (13, 11): 134.1219478548764, (0, 0): 2.940535878667633, (3, 13): 36.458224722184106, (1, 13): 61.99282737891932, (8, 11): 60.82618055555555, (4, 14): 149.01588989549896, (2, 10): 142.17075492831518, (9, 10): 14079.08468363113, (5, 15): 35.54931534896419, (10, 1): 37.918148279383836, (6, 12): 14096.570521337682, (11, 12): 145.43855389332094, (14, 11): 52.86024029830134, (13, 1): 148.72033950301662, (12, 15): 33.28824859807297, (15, 2): 20.3679438232888, (13, 14): 140.88155459592846, (0, 13): 16.55808202239474, (3, 8): 37.40815990448544, (2, 0): 144.25062906879913, (1, 8): 60.5559454271502, (8, 8): 19.369330138556123, (4, 3): 147.3198963205051, (2, 15): 147.95546909847843, (9, 5): 13922.236315943535, (5, 2): 36.74721595955463, (10, 2): 29.856294374658656, (9, 9): 10818.114583333336, (14, 6): 58.294736842105266, (5, 9): 35.10465116279069, (15, 6): 16.555555555555557, (6, 9): 12210.923913043478, (13, 9): 138.2391304347826, (14, 9): 46.46236559139785, (9, 6): 12965.058823529407, (2, 9): 165.21839080459768, (1, 9): 46.554216867469876, (5, 6): 38.341176470588245, (2, 6): 140.53333333333336, (8, 6): 42.30666666666666, (0, 9): 15.23404255319149, (11, 9): 122.76923076923075, (6, 6): 10164.676767676769, (8, 9): 46.522222222222226, (4, 6): 99.60215053763443, (12, 9): 36.938775510204074, (7, 9): 51.597826086956545, (7, 6): 56.616161616161634, (3, 9): 38.24050632911391, (10, 9): 28.852272727272727, (11, 6): 131.31683168316835, (4, 9): 136.7931034482758, (13, 6): 136.70329670329673, (12, 6): 33.15384615384615, (0, 6): 14.7625, (10, 6): 34.774647887323944}
{(7, 3): 62.81898054921196, (12, 1): 35.32598189785806, (11, 11): 0.0, (7, 12): 58.71275722939636, (14, 4): 59.24469387755102, (13, 4): 141.5126403526899, (12, 12): 0.0, (0, 7): 15.879129221551967, (15, 1): 20.230265197709716, (0, 10): 13.273006169314652, (3, 7): 32.47989086289141, (2, 5): 133.06861824603752, (1, 11): 63.08206686930091, (8, 5): 57.77892949892633, (5, 8): 35.45380602226514, (4, 0): 148.0283734123021, (10, 8): 32.73085034501111, (9, 0): 10546.328362540478, (6, 7): 16052.843970006248, (5, 5): 0.0, (11, 5): 132.4507692134555, (10, 7): 35.067135761589405, (6, 10): 12757.903113798027, (15, 11): 13.092402464065708, (14, 1): 59.599478589317236, (13, 7): 142.48078829945436, (0, 4): 10.973519067650503, (15, 4): 19.89170908116793, (1, 1): 0.0, (8, 15): 53.92273039485658, (4, 10): 133.48332976046797, (3, 2): 32.897370242214556, (9, 14): 13916.552137632636, (8, 2): 54.941330937737554, (5, 11): 35.781798094185824, (4, 5): 147.67254698229098, (10, 13): 33.47068134893316, (9, 3): 12727.163225205188, (6, 0): 11478.959775227664, (11, 0): 114.36994576322726, (7, 5): 62.90928378985182, (14, 15): 60.32926889807265, (12, 11): 33.41660377358495, (15, 14): 16.254277468563178, (14, 2): 60.28252059975686, (13, 10): 134.2848676678564, (0, 1): 12.874899411946771, (3, 12): 33.373764378145125, (1, 12): 57.27672140755854, (8, 12): 61.448107968632556, (4, 15): 122.91948407390895, (3, 1): 33.37803715067578, (2, 11): 143.1838128751812, (5, 14): 35.537022892884316, (10, 14): 33.335929334125865, (6, 13): 13862.472310235571, (11, 15): 155.28716427523088, (7, 8): 61.98744494298769, (14, 8): 60.66571876030333, (13, 0): 114.18759662904276, (12, 8): 32.84192013242294, (15, 13): 13.28471742434711, (13, 13): 0.0, (0, 14): 15.572209501413042, (3, 11): 32.83667524725643, (2, 1): 141.47316317040432, (1, 15): 53.12141796585006, (8, 9): 48.37755102040814, (4, 12): 144.9323486099335, (2, 12): 133.44176091560414, (9, 4): 13781.296138810781, (5, 1): 33.46942706822981, (10, 3): 35.64557374104757, (7, 2): 62.47441860465116, (6, 14): 15039.378779808241, (12, 2): 33.546449969010396, (11, 10): 148.00380594174683, (7, 15): 58.15662470955156, (14, 5): 56.47990437603114, (13, 3): 132.12878669144513, (12, 13): 30.758082117037244, (15, 0): 17.604025552807933, (1, 5): 59.451343149376186, (0, 11): 16.15409198277059, (2, 2): 0.0, (1, 10): 57.83861538114262, (4, 1): 142.84947554263164, (9, 7): 13911.845074196213, (6, 4): 15978.706167280667, (5, 4): 32.13393901851475, (11, 4): 142.1836063326712, (10, 4): 33.182139699381096, (7, 1): 62.56810800874201, (6, 11): 13930.703665211668, (12, 7): 35.192074171316136, (15, 10): 16.977548767022455, (14, 6): 45.866666666666646, (0, 5): 13.576147715793024, (15, 7): 18.431580909768826, (1, 0): 59.85316808231506, (0, 8): 13.832673616148217, (4, 11): 144.23440181206672, (3, 5): 35.41663125405383, (2, 7): 142.6797806095095, (9, 13): 16063.579044747481, (8, 3): 57.70667805141109, (5, 10): 33.28262332593047, (10, 10): 0.0, (9, 2): 13829.60016403527, (6, 1): 13965.141376254562, (5, 7): 32.66522411128276, (11, 3): 144.58886160714312, (7, 4): 64.19937504245644, (14, 12): 58.865592663594896, (12, 4): 30.226240940790372, (14, 3): 56.310925690927284, (0, 2): 10.859171195652177, (3, 15): 32.81855181331198, (1, 3): 59.95053460889139, (8, 13): 61.51022362032415, (4, 8): 141.52142973989845, (3, 0): 33.22072565256445, (2, 8): 142.45873078275974, (9, 8): 16031.358072675674, (8, 0): 54.95975179527587, (5, 13): 32.704996251107545, (10, 15): 32.7741326904937, (6, 2): 16047.449976065103, (11, 14): 142.32932887161485, (7, 11): 58.31138862494909, (15, 12): 17.06381805496161, (13, 12): 148.2239514610188, (0, 15): 13.128566649734235, (3, 10): 35.99234114871588, (1, 14): 61.10418691202316, (8, 10): 61.22829321982502, (4, 13): 144.53028207964616, (2, 13): 142.6150074901268, (9, 11): 16100.530107231234, (5, 0): 33.178541922518704, (10, 0): 31.364922701456244, (6, 15): 11487.42997574918, (12, 3): 33.00199421900554, (11, 13): 137.99409665019226, (7, 14): 62.696611909650926, (14, 10): 58.72207561789047, (13, 2): 142.09686807095363, (12, 14): 33.295968838877144, (15, 3): 18.039271159610653, (13, 15): 156.14950277477752, (1, 4): 56.90774633619234, (0, 12): 13.409016208914903, (2, 3): 148.1584150611975, (8, 7): 60.722751973751656, (4, 2): 137.70642327751813, (2, 14): 141.33253657531426, (6, 5): 12677.77629916997, (5, 3): 35.357638303373655, (11, 7): 142.43635201715162, (10, 5): 32.950890144268634, (7, 0): 51.59199427843461, (6, 8): 13949.1975700819, (12, 0): 31.443989671218382, (11, 8): 140.2562559261244, (7, 13): 57.41174452905263, (14, 7): 60.1454643048846, (13, 5): 144.3580922683476, (1, 7): 61.28345092214383, (3, 4): 36.234843739124436, (2, 4): 137.34775476727506, (9, 12): 12783.013336034313, (8, 4): 53.544004400440045, (4, 7): 141.80133023083397, (10, 11): 30.564188956886476, (9, 1): 14933.854491216434, (11, 2): 141.5613817781449, (10, 6): 38.57303370786517, (7, 7): 0.0, (14, 13): 53.961938183290584, (12, 5): 35.73024863744874, (15, 8): 19.97525993506759, (14, 0): 49.3160963028965, (13, 8): 140.48508634222927, (0, 3): 13.609014698611052, (15, 5): 18.096463385706674, (3, 14): 35.59527542809991, (1, 2): 57.26956581384184, (8, 14): 61.92294527609386, (4, 9): 170.88172043010755, (3, 3): 0.0, (9, 15): 12524.705482423533, (8, 1): 61.469035323280316, (5, 12): 35.94720203406609, (4, 4): 0.0, (10, 12): 35.180477291605825, (6, 3): 12777.016587704271, (11, 1): 142.0093658014451, (7, 10): 58.72067414221446, (14, 14): 0.0, (12, 10): 35.094069322529776, (15, 15): 0.0, (13, 11): 139.1784847854715, (0, 0): 0.0, (3, 13): 35.901522424907434, (1, 13): 61.749024882313385, (8, 11): 61.111050290797124, (4, 14): 140.8910112590825, (2, 10): 145.14204500945596, (9, 10): 12877.26995175818, (5, 15): 32.866213796084736, (10, 1): 35.30119984304979, (6, 12): 12732.274722556416, (11, 12): 133.65037916403313, (14, 11): 53.15833504765824, (13, 1): 141.27246931096184, (12, 15): 32.91907378530234, (15, 2): 19.438739711240054, (13, 14): 141.94974325132526, (0, 13): 15.835581902425728, (3, 8): 35.521380827832395, (2, 0): 147.70319077078625, (1, 8): 61.19153134635149, (8, 8): 0.0, (4, 3): 133.35931650834672, (2, 15): 122.90036145694955, (9, 5): 12752.70537051003, (5, 2): 35.712281415209404, (10, 2): 31.331604449600764, (3, 6): 36.72340425531913, (0, 6): 11.102803738317757, (15, 6): 20.556701030927837, (5, 6): 38.480392156862735, (11, 9): 129.88421052631574, (14, 9): 43.66363636363636, (9, 6): 14118.043956043955, (15, 9): 13.434782608695652, (13, 9): 110.11764705882354, (6, 9): 14242.815217391304, (1, 9): 39.472527472527474, (12, 6): 36.69565217391306, (4, 6): 100.89473684210526, (7, 9): 57.87341772151899, (2, 9): 141.76136363636374, (11, 6): 137.02247191011233, (1, 6): 51.116504854368934, (2, 6): 104.55445544554455, (5, 9): 35.7979797979798, (8, 6): 44.712500000000006, (7, 6): 42.72527472527473, (3, 9): 32.42424242424242, (0, 9): 19.49999999999999, (10, 9): 35.10416666666668, (12, 9): 30.582278481012658, (13, 6): 130.4943820224719, (9, 9): 0.0, (6, 6): 0.0}
{(7, 3): 31.01091715343665, (12, 1): 23.077568436675463, (11, 11): 0.0, (7, 12): 41.10084826695132, (14, 4): 36.36483829412159, (13, 4): 76.11015490533563, (12, 12): 0.0, (0, 7): 13.234676768304043, (15, 1): 16.084832640289804, (0, 10): 10.353074940054704, (3, 7): 10.324715955870246, (2, 5): 99.31290351607319, (1, 11): 40.46105961161105, (8, 5): 47.15701874817126, (5, 8): 22.43956853675007, (4, 0): 96.3726086490541, (10, 8): 10.615198561180836, (9, 0): 2256.9746339192993, (6, 7): 2276.050525448171, (5, 5): 0.0, (11, 5): 81.50490839176663, (10, 7): 22.63218771338121, (6, 10): 2243.2156352668108, (15, 11): 5.264717934708371, (14, 1): 36.47048657545516, (13, 7): 74.89953275837216, (0, 4): 4.778556219520578, (15, 4): 13.445995392329586, (1, 1): 0.0, (8, 15): 47.65091152118218, (4, 10): 95.27243141684458, (3, 2): 9.995067141682652, (9, 14): 2242.2103337625445, (8, 2): 35.704918032786885, (5, 11): 20.819002342565792, (4, 5): 97.05280550462861, (10, 13): 18.766536964980517, (9, 3): 2246.9394416574837, (6, 0): 2243.0749938419526, (11, 0): 83.95173036601234, (7, 5): 30.617659636723758, (14, 15): 33.16684768105057, (12, 11): 18.99515192898602, (15, 14): 8.34662664967313, (14, 2): 36.16818457802058, (13, 10): 80.52156240927252, (0, 1): 7.653447135653468, (3, 12): 19.901673287046957, (1, 12): 44.424301983422794, (8, 12): 37.054950239255966, (4, 15): 98.56319591010644, (3, 1): 11.614232054288506, (2, 11): 89.54887165997503, (5, 14): 22.76718578271777, (10, 14): 12.042896650619696, (6, 13): 2267.1506961506934, (11, 15): 72.60906643562224, (7, 8): 36.071905358499855, (14, 8): 37.78497382736322, (13, 0): 84.07972292810165, (12, 8): 10.638720990201142, (15, 13): 5.283489309379052, (13, 13): 0.0, (0, 14): 13.025771927666375, (3, 11): 10.943630744423537, (2, 1): 92.46034307943799, (1, 15): 45.49961804314881, (4, 12): 89.20580608793694, (2, 12): 95.04110772129758, (9, 4): 2235.994995887028, (5, 1): 11.58340743191548, (10, 3): 26.41720006749537, (7, 2): 36.938019909995845, (6, 14): 2265.3523445054784, (12, 2): 18.831578213264507, (11, 10): 76.38216317508055, (7, 15): 40.25040267089601, (14, 5): 39.38098713313722, (13, 3): 81.54387179630355, (12, 13): 8.425733077555504, (15, 0): 13.723686917016195, (1, 5): 38.162221546158285, (0, 11): 11.836443771090146, (2, 2): 0.0, (1, 10): 44.26289436968361, (4, 1): 91.54057648745825, (9, 7): 2246.5999381825695, (6, 4): 2140.2421687572846, (5, 4): 10.326474433968745, (11, 4): 75.0755114524571, (10, 4): 19.011600298487217, (7, 1): 36.69912194321351, (6, 11): 2236.0894264373346, (12, 7): 22.71361685524773, (15, 10): 11.416794340302813, (0, 5): 9.807785096331882, (15, 7): 12.295176149537312, (1, 0): 42.080344988177984, (0, 8): 9.389748509839164, (4, 11): 90.57532467532472, (3, 5): 22.743412395829807, (2, 7): 102.27287027071777, (9, 13): 2108.3704387043867, (8, 3): 47.006223062466994, (5, 10): 19.942653905554227, (10, 10): 0.0, (9, 2): 2209.955555555551, (6, 1): 2247.3914353655086, (5, 7): 10.364299061582381, (11, 3): 77.85339826524095, (7, 4): 36.67643425748016, (14, 12): 34.87828836330088, (12, 4): 9.043172898161524, (14, 3): 39.790096987113245, (0, 2): 4.791501300123172, (3, 15): 22.584951803705113, (1, 3): 38.002985479712244, (8, 13): 39.849513558269415, (4, 8): 87.73183624964143, (3, 0): 22.62372626836857, (2, 8): 87.57761286332719, (9, 8): 2285.236760316968, (8, 0): 48.62160538064694, (5, 13): 10.894671366369474, (10, 15): 20.54073055457479, (6, 2): 2154.5550554016554, (11, 14): 73.78042920217685, (7, 11): 32.68077952377686, (15, 12): 11.564397952972469, (13, 12): 77.29558147358989, (0, 15): 10.296561372963557, (3, 10): 26.429522278313055, (1, 14): 40.218781527311705, (8, 10): 36.83529253711292, (4, 13): 90.15709908069459, (2, 13): 89.40059224571313, (9, 11): 2141.5885108983475, (5, 0): 22.71855154347021, (10, 0): 23.429129830737136, (6, 15): 2254.4544398113326, (12, 3): 19.996817471295387, (11, 13): 64.9373105538715, (7, 14): 38.13598218519971, (14, 10): 34.947902988676034, (13, 2): 75.95573591597322, (12, 14): 12.077587441927106, (15, 3): 13.07194787921143, (13, 15): 73.16945831804306, (1, 4): 35.14922941136541, (0, 12): 10.347336960171942, (2, 3): 97.73941437167193, (8, 7): 42.552739470741656, (4, 2): 77.60340815767861, (2, 14): 96.77638906075981, (6, 5): 2260.095828128338, (5, 3): 22.7026887512344, (11, 7): 75.03648068669519, (10, 5): 19.95747864440843, (7, 0): 42.55238785535962, (6, 8): 2241.592457945657, (12, 0): 23.434843339298393, (11, 8): 81.92092324782432, (7, 13): 32.37076502732237, (14, 7): 34.61230972319617, (13, 5): 78.1445011778763, (1, 7): 41.909988457416155, (3, 4): 20.812272133177398, (2, 4): 78.12902353259389, (9, 12): 2241.7017437418563, (8, 4): 36.450563896768884, (4, 7): 101.64208496584543, (10, 11): 8.310864775543921, (9, 1): 2276.589548368359, (11, 2): 75.88690025469806, (7, 7): 0.0, (14, 13): 31.34930343187224, (12, 5): 26.284137006202158, (15, 8): 15.589492708463169, (14, 0): 41.12222833550276, (13, 8): 81.83165606799612, (0, 3): 9.76898773177974, (15, 5): 13.18933790568406, (3, 14): 22.817957977675622, (1, 2): 35.29516678012248, (8, 14): 42.804205453496984, (3, 3): 0.0, (9, 15): 2228.732032822412, (8, 1): 43.937658430022836, (5, 12): 26.455758924057054, (4, 4): 0.0, (10, 12): 22.6374561393675, (6, 3): 2250.018950224827, (11, 1): 84.39726959641993, (7, 10): 41.24680985257182, (14, 14): 0.0, (12, 10): 22.635183078603838, (15, 15): 0.0, (13, 11): 65.23508508166468, (0, 0): 0.0, (3, 13): 20.664081104987396, (1, 13): 40.68562585969739, (8, 11): 40.43825917956539, (4, 14): 97.81233565912345, (2, 10): 89.44387772297809, (9, 10): 2251.9704338836004, (5, 15): 22.444216959133065, (10, 1): 23.211661011338258, (6, 12): 2247.431493916404, (11, 12): 80.52834250983994, (7, 9): 26.483870967741936, (14, 11): 31.355724137931034, (13, 1): 84.13538252211018, (12, 15): 20.44222603779902, (15, 2): 13.463975367772838, (13, 14): 74.55304782744614, (0, 13): 11.804818125981024, (3, 8): 22.51192036703261, (2, 0): 96.7103627336631, (1, 8): 39.79983864628363, (8, 8): 0.0, (4, 3): 98.35744547308956, (2, 15): 98.61117065102246, (9, 5): 2261.105330987414, (5, 2): 20.864710732444657, (10, 2): 9.00553354283372, (10, 9): 13.750000000000002, (13, 6): 76.40196078431374, (4, 6): 39.230769230769255, (14, 9): 22.434782608695652, (12, 9): 11.550458715596333, (14, 6): 9.461538461538463, (15, 9): 6.548672566371682, (9, 6): 2217.731707317073, (0, 9): 8.499999999999998, (2, 9): 81.24468085106382, (11, 6): 76.01470588235294, (5, 6): 13.309278350515465, (2, 6): 26.851485148514858, (8, 9): 8.475609756097562, (13, 9): 36.130434782608695, (6, 6): 0.0, (1, 6): 27.766666666666666, (3, 6): 11.919191919191917, (8, 6): 33.89108910891091, (3, 9): 14.01785714285714, (6, 9): 2127.366336633664, (9, 9): 0.0, (4, 9): 75.27380952380953, (11, 9): 28.17894736842105, (12, 6): 13.972222222222221, (5, 9): 15.010416666666666, (1, 9): 13.88888888888889, (15, 6): 9.755813953488373, (7, 6): 6.386363636363637, (10, 6): 14.71951219512195, (0, 6): 5.252873563218389}
'''